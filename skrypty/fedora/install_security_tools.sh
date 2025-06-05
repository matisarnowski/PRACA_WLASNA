#!/bin/bash

# Ten skrypt instaluje i konfiguruje podstawowe narzędzia bezpieczeństwa
# na Fedorze 41.  URUCHAMIAJ Z UPRAWNIENIAMI ROOT-a (sudo).

# 1. Aktualizacja systemu (ZAWSZE na początku)
echo "Aktualizacja systemu..."
sudo dnf update -y
if [ $? -ne 0 ]; then
  echo "Błąd podczas aktualizacji systemu. Przerwanie."
  exit 1
fi

# 2. Instalacja pakietów
echo "Instalacja pakietów..."
sudo dnf install -y setroubleshoot-server clamav clamav-update clamav-server clamav-server-systemd rkhunter chkrootkit aide lynis nmap tcpdump firejail rpmdevtools

if [ $? -ne 0 ]; then
  echo "Błąd podczas instalacji pakietów. Przerwanie."
  exit 1
fi

# 3. Konfiguracja ClamAV
echo "Konfiguracja ClamAV..."
# Uruchomienie usług i włączenie ich przy starcie
sudo systemctl enable --now clamav-freshclam.service
sudo systemctl enable --now clamav-clamonacc.service

# Pierwsza aktualizacja bazy wirusów (może potrwać)
sudo freshclam
if [ $? -ne 0 ]; then
  echo "Błąd podczas aktualizacji bazy wirusów ClamAV. Sprawdź połączenie z internetem."
  # Nie przerywamy, bo to może być tymczasowy problem z siecią.
fi

# 4. Konfiguracja Rkhunter
echo "Konfiguracja Rkhunter..."
# Pierwsze uruchomienie i utworzenie bazy danych (po instalacji świeżego systemu to jest OK)
sudo rkhunter --propupd
if [ $? -ne 0 ]; then
  echo "Błąd podczas inicjalizacji bazy danych Rkhunter."
  exit 1
fi

# 5. Konfiguracja AIDE
echo "Konfiguracja AIDE..."
# Inicjalizacja bazy danych AIDE
sudo aide --init
if [ $? -ne 0 ]; then
    echo "Błąd podczas inicjalizacji bazy danych AIDE."
    exit 1
fi
# Przeniesienie nowej bazy
sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

# 6. Konfiguracja crona (automatyczne zadania)

# ClamAV - aktualizacja bazy co 2 godziny
echo "Konfiguracja crona dla ClamAV (aktualizacja)..."
(sudo crontab -l ; echo "0 */2 * * * /usr/bin/freshclam --quiet") | sudo crontab -

# ClamAV - pełne skanowanie (codziennie o 3:00).  ZAPIS DO LOGU, *NIE* USUWANIE.
echo "Konfiguracja crona dla ClamAV (skanowanie)..."
(sudo crontab -l; echo "0 3 * * * /usr/bin/clamscan -r / --log=/var/log/clamav/clamscan.log") | sudo crontab -
# Dodaj opcje do clamscan wedle uznania, np. --move=/katalog/kwarantanny
# Upewnij się, że katalog /var/log/clamav istnieje i ma odpowiednie uprawnienia:
sudo mkdir -p /var/log/clamav
sudo chown clamscan:clamscan /var/log/clamav
sudo chmod 750 /var/log/clamav

# Rkhunter - codzienne skanowanie
echo "Konfiguracja crona dla Rkhunter..."
(sudo crontab -l ; echo "0 4 * * * /usr/bin/rkhunter -c --cronjob --report-warnings-only") | sudo crontab -

# Chkrootkit - codzienne skanowanie
echo "Konfiguracja crona dla Chkrootkit..."
(sudo crontab -l ; echo "30 4 * * * /usr/sbin/chkrootkit 2>&1 | mail -s \"Chkrootkit Daily Report\" root") | sudo crontab -
 # Wysyłanie raportu na root@localhost. Upewnij się, że masz skonfigurowaną pocztę.
 # Alternatywnie, zapisuj do pliku:  >> /var/log/chkrootkit.log

# AIDE - codzienne sprawdzanie
echo "Konfiguracja crona dla AIDE..."
(sudo crontab -l; echo "0 5 * * * /usr/sbin/aide --check") | sudo crontab -
# Wyniki AIDE są zapisywane do logu (zwykle /var/log/aide/aide.log).

# 7. Włączenie SELinux (na wszelki wypadek - powinno być już włączone)
echo "Sprawdzanie i ewentualne włączenie SELinux..."
if [ "$(sestatus | grep 'Current mode' | awk '{print $3}')" != "enforcing" ]; then
  sudo setenforce 1
  sudo sed -i 's/SELINUX=.*$/SELINUX=enforcing/g' /etc/selinux/config
  echo "SELinux został przełączony w tryb enforcing.  Wymagany restart."
fi

echo "Skrypt zakończony. Zalecany restart systemu."
