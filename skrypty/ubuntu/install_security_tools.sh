#!/bin/bash

# Ten skrypt instaluje i konfiguruje podstawowe narzędzia bezpieczeństwa
# na Ubuntu. URUCHAMIAJ Z UPRAWNIENIAMI ROOT-a (sudo).

# 1. Aktualizacja systemu (ZAWSZE na początku)
echo "Aktualizacja systemu..."
sudo apt update && sudo apt upgrade -y
if [ $? -ne 0 ]; then
  echo "Błąd podczas aktualizacji systemu. Przerwanie."
  exit 1
fi

# 2. Instalacja pakietów
echo "Instalacja pakietów..."
# Nazwy pakietów dostosowane do Ubuntu
# Usunięto setroubleshoot-server (specyficzne dla SELinux/Fedory) oraz rpmdevtools (specyficzne dla RPM)
sudo apt install -y clamav clamav-daemon clamav-freshclam rkhunter chkrootkit aide lynis nmap tcpdump firejail
if [ $? -ne 0 ]; then
  echo "Błąd podczas instalacji pakietów. Przerwanie."
  exit 1
fi

# 3. Konfiguracja ClamAV
echo "Konfiguracja ClamAV..."
# Uruchomienie usług i włączenie ich przy starcie
# Na Ubuntu, clamav-daemon obsługuje główny silnik skanowania, a freshclam aktualizacje
sudo systemctl enable --now clamav-freshclam.service
sudo systemctl enable --now clamav-daemon.service # Zamiast clamav-clamonacc.service, to jest główny demon

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
sudo aideinit # W nowszych wersjach aide na Ubuntu, używa się aideinit, które robi oba kroki
if [ $? -ne 0 ]; then
    echo "Błąd podczas inicjalizacji bazy danych AIDE (aideinit). Sprawdź, czy pakiet 'aide-common' jest zainstalowany."
    # Jeśli aideinit nie jest dostępne, spróbuj starych poleceń:
    # sudo aide --init
    # if [ $? -ne 0 ]; then
    #     echo "Błąd podczas inicjalizacji bazy danych AIDE (--init)."
    #     exit 1
    # fi
    # sudo mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db # Zwróć uwagę na ścieżkę .gz lub bez
    # Lub jeśli plik to .gz:
    # sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
    exit 1 # Zakończ, jeśli inicjalizacja się nie udała
fi
echo "Baza AIDE zainicjalizowana. Nowa baza danych powinna znajdować się w /var/lib/aide/aide.db (lub aide.db.gz)."
echo "Może być konieczne ręczne skopiowanie np. sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db"
echo "Sprawdź dokumentację AIDE dla Twojej wersji Ubuntu."


# 6. Konfiguracja crona (automatyczne zadania)

# ClamAV - aktualizacja bazy co 2 godziny
echo "Konfiguracja crona dla ClamAV (aktualizacja)..."
(sudo crontab -l 2>/dev/null | grep -v '/usr/bin/freshclam' ; echo "0 */2 * * * /usr/bin/freshclam --quiet") | sudo crontab -

# ClamAV - pełne skanowanie (codziennie o 3:00).  ZAPIS DO LOGU, *NIE* USUWANIE.
echo "Konfiguracja crona dla ClamAV (skanowanie)..."
(sudo crontab -l 2>/dev/null | grep -v '/usr/bin/clamscan' ; echo "0 3 * * * /usr/bin/clamscan -r / --log=/var/log/clamav/clamscan.log --exclude-dir=/sys/ --exclude-dir=/proc/ --exclude-dir=/dev/") | sudo crontab -
# Dodaj opcje do clamscan wedle uznania, np. --move=/katalog/kwarantanny
# Upewnij się, że katalog /var/log/clamav istnieje i ma odpowiednie uprawnienia:
sudo mkdir -p /var/log/clamav
sudo chown clamav:clamav /var/log/clamav # Zmieniono użytkownika/grupę na clamav
sudo chmod 750 /var/log/clamav

# Rkhunter - codzienne skanowanie
echo "Konfiguracja crona dla Rkhunter..."
(sudo crontab -l 2>/dev/null | grep -v '/usr/bin/rkhunter' ; echo "0 4 * * * /usr/bin/rkhunter --update && /usr/bin/rkhunter --cronjob --report-warnings-only") | sudo crontab -

# Chkrootkit - codzienne skanowanie
echo "Konfiguracja crona dla Chkrootkit..."
(sudo crontab -l 2>/dev/null | grep -v '/usr/sbin/chkrootkit' ; echo "30 4 * * * /usr/sbin/chkrootkit 2>&1 | mail -s \"Chkrootkit Daily Report $(hostname)\" root") | sudo crontab -
 # Wysyłanie raportu na root@localhost. Upewnij się, że masz skonfigurowaną pocztę (np. pakiet mailutils).
 # Alternatywnie, zapisuj do pliku:  >> /var/log/chkrootkit.log

# AIDE - codzienne sprawdzanie
echo "Konfiguracja crona dla AIDE..."
(sudo crontab -l 2>/dev/null | grep -v '/usr/bin/aide' ; echo "0 5 * * * /usr/bin/aide --check") | sudo crontab - # Ścieżka może być /usr/bin/aide
# Wyniki AIDE są zapisywane do logu (zwykle /var/log/aide/aide.log).

# 7. Informacja o AppArmor (zamiast SELinux)
echo "Informacja o bezpieczeństwie systemu..."
echo "Ubuntu domyślnie używa AppArmor zamiast SELinux."
echo "Możesz zarządzać profilami AppArmor za pomocą narzędzi takich jak 'aa-status', 'aa-complain', 'aa-enforce'."
echo "Jeśli potrzebujesz narzędzi do debugowania AppArmor, rozważ instalację 'apparmor-utils'."
# Poniższa sekcja SELinux została zakomentowana, gdyż nie jest standardowa dla Ubuntu.
# echo "Sprawdzanie i ewentualne włączenie SELinux..."
# if command -v sestatus &> /dev/null; then
#   if [ "$(sestatus | grep 'Current mode' | awk '{print $3}')" != "enforcing" ]; then
#     sudo setenforce 1
#     # Poniższa linia jest specyficzna dla konfiguracji SELinux i może wymagać dostosowania lub usunięcia
#     # sudo sed -i 's/SELINUX=.*$/SELINUX=enforcing/g' /etc/selinux/config
#     echo "SELinux został przełączony w tryb enforcing. Może być wymagany restart."
#   fi
# else
#   echo "SELinux nie jest zainstalowany (sestatus nie znaleziono)."
# fi

echo "Skrypt zakończony. Sprawdź logi i ewentualnie zrestartuj system, jeśli były dokonywane zmiany na niskim poziomie."