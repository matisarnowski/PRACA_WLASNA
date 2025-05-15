#!/bin/bash
set -e

# --- Konfiguracja ---
# UWAGA: Ścieżka OUTPUT_DIR jest specyficzna dla użytkownika.
# Upewnij się, że katalog istnieje lub skrypt ma uprawnienia do jego utworzenia.
OUTPUT_DIR="/home/witcher-mati/Dokumenty"
OUTPUT_FILE="$OUTPUT_DIR/konfiguracja_sieci_$(date +%Y-%m-%d_%H-%M-%S).txt"
#CONNECTION_NAME="Witcher"  # ZAKOMENTOWANE - będziemy używać nazwy istniejącego połączenia
TARGET_HOST="8.8.8.8"
NETWORK_CIDR="192.168.1.0/24" # Adres sieci do skanowania

# --- Funkcje pomocnicze ---
log() {
  # Zapisz do pliku
  echo "$(date +%Y-%m-%d_%H-%M-%S) - $1" >> "$OUTPUT_FILE"
  # Wyświetl na konsoli
  echo "$1"
}

# --- Sprawdzenie uprawnień ---
if [ "$(id -u)" -ne 0 ]; then
   # Nie używamy funkcji log() tutaj, bo plik log jeszcze może nie istnieć
   # lub skrypt nie ma uprawnień do zapisu w OUTPUT_DIR bez sudo.
   echo "Błąd: Skrypt musi być uruchomiony jako root (użyj sudo)."
   exit 1
fi

# --- Tworzenie katalogu wyjściowego, jeśli nie istnieje ---
# (robione z uprawnieniami sudo, więc powinno zadziałać)
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
  # Popraw uprawnienia, jeśli katalog tworzony jest jako root, a ma być dostępny dla użytkownika
  # Załóżmy, że skrypt jest uruchamiany przez `sudo ./skrypt.sh`, więc $SUDO_USER będzie ustawione.
  if [ -n "$SUDO_USER" ]; then
    chown "$SUDO_USER":"$SUDO_USER" "$OUTPUT_DIR"
  fi
  echo "Utworzono katalog: $OUTPUT_DIR (log() jeszcze niedostępne)" # Logujemy po utworzeniu pliku
fi

# --- Zapis nagłówka do pliku ---
# Teraz możemy bezpiecznie używać log(), bo plik powinien być zapisywalny.
echo "Raport konfiguracji sieci i diagnostyki" > "$OUTPUT_FILE"
echo "Data i godzina: $(date +%Y-%m-%d_%H-%M-%S)" >> "$OUTPUT_FILE"
echo "----------------------------------------" >> "$OUTPUT_FILE"
# Popraw uprawnienia pliku, jeśli $SUDO_USER jest ustawione
if [ -n "$SUDO_USER" ]; then
  chown "$SUDO_USER":"$SUDO_USER" "$OUTPUT_FILE"
fi


log "Skrypt uruchomiony przez użytkownika: $(whoami), efektywny użytkownik: $(id -u -n)"
if [ -n "$SUDO_USER" ]; then
    log "Uruchomiono z sudo przez: $SUDO_USER"
fi


# --- 1. Konfiguracja DNS (modyfikacja ISTNIEJĄCEGO aktywnego połączenia Wi-Fi) ---

log "Pobieranie nazwy aktywnego połączenia Wi-Fi..."
# Poprawione polecenie, aby było bardziej odporne, jeśli nazwa połączenia zawiera spacje
# lub aby wybrać pierwsze aktywne połączenie, jeśli jest ich więcej.
CONNECTION_NAME=$(nmcli --terse --fields NAME,DEVICE,TYPE connection show --active | grep ':wifi$' | head -n 1 | cut -d':' -f1)


if [ -z "$CONNECTION_NAME" ]; then
  log "Błąd: Nie znaleziono aktywnego połączenia Wi-Fi."
  exit 1
fi

log "1. Konfiguracja DNS dla połączenia '$CONNECTION_NAME'..."

# Ustawienie serwerów DNS (IPv4 i IPv6) i ignorowanie automatycznie pobieranych DNS
nmcli connection modify "$CONNECTION_NAME" ipv4.ignore-auto-dns yes ipv4.dns "8.8.8.8 1.1.1.1"
nmcli connection modify "$CONNECTION_NAME" ipv6.ignore-auto-dns yes ipv6.dns "2001:4860:4860::8888 2606:4700:4700::1111"

log "Restartowanie połączenia '$CONNECTION_NAME' w celu zastosowania zmian DNS..."
# Czasami restart może chwilę potrwać lub zgłosić błąd, jeśli sieć jest niestabilna
nmcli connection down "$CONNECTION_NAME" || log "Ostrzeżenie: Nie udało się wyłączyć połączenia '$CONNECTION_NAME'. Może już było nieaktywne."
sleep 5 # Dajmy chwilę
nmcli connection up "$CONNECTION_NAME" || { log "Błąd krytyczny: Nie udało się ponownie aktywować połączenia '$CONNECTION_NAME'."; exit 1; }
log "Konfiguracja DNS zakończona i połączenie zrestartowane."

# Zapis konfiguracji połączenia do pliku...
log "Zapis aktualnej konfiguracji połączenia '$CONNECTION_NAME' do pliku..."
nmcli connection show "$CONNECTION_NAME" >> "$OUTPUT_FILE"

# --- 2. Instalacja narzędzi diagnostycznych ---
log "2. Instalacja narzędzi diagnostycznych (jeśli potrzebne)..."
# Zmieniono dnf na apt, bind-utils na dnsutils
sudo apt update # Upewnij się, że lista pakietów jest aktualna
sudo apt install -y traceroute net-tools dnsutils nmap

# --- 3. Diagnostyka sieci ---
log "3. Rozpoczynanie diagnostyki sieci..."

log " a) Traceroute (ICMP) do $TARGET_HOST:"
# Na Ubuntu traceroute domyślnie używa UDP, -I wymusza ICMP, co jest często lepsze do diagnostyki.
traceroute -I "$TARGET_HOST" >> "$OUTPUT_FILE" 2>&1 || log "Ostrzeżenie: Traceroute mogło nie powieść się."

log " b) Skanowanie sieci $NETWORK_CIDR (nmap -sn):"
# Zmieniono -sP (przestarzałe) na -sn (Ping Scan)
nmap -sn "$NETWORK_CIDR" >> "$OUTPUT_FILE" 2>&1 || log "Ostrzeżenie: Skanowanie nmap mogło nie powieść się."

log " c) Informacje o adresach IP (ip addr):"
ip addr >> "$OUTPUT_FILE" 2>&1

log " d) Tablica routingu (ip route):"
ip route >> "$OUTPUT_FILE" 2>&1

log " e) Aktywne połączenia sieciowe (ss -tulnp):"
ss -tulnp >> "$OUTPUT_FILE" 2>&1

log "Raport diagnostyki sieci zapisany do pliku: $OUTPUT_FILE"
log "Skrypt zakończył działanie."
exit 0