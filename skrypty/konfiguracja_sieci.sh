#!/bin/bash
set -e

# --- Konfiguracja ---
OUTPUT_DIR="/home/witcher-mati/Dokumenty"  # Poprawiona ścieżka
OUTPUT_FILE="$OUTPUT_DIR/konfiguracja_sieci_$(date +%Y-%m-%d_%H-%M-%S).txt"
#CONNECTION_NAME="Witcher"  # ZAKOMENTOWANE - będziemy używać nazwy istniejącego połączenia
TARGET_HOST="8.8.8.8"
NETWORK_CIDR="192.168.1.0/24" # Poprawiony adres sieci

# --- Funkcje pomocnicze ---
log() {
  echo "$(date +%Y-%m-%d_%H-%M-%S) - $1" >> "$OUTPUT_FILE"
  echo "$1"
}

# --- Sprawdzenie uprawnień ---
if [ "$(id -u)" -ne 0 ]; then
   log "Skrypt musi być uruchomiony jako root (użyj sudo)."
   exit 1
fi

# --- Tworzenie katalogu Dokumenty, jeśli nie istnieje ---
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
  log "Utworzono katalog: $OUTPUT_DIR"
fi

# --- Zapis nagłówka do pliku ---
echo "Raport konfiguracji sieci i diagnostyki" > "$OUTPUT_FILE"
echo "Data i godzina: $(date +%Y-%m-%d_%H-%M-%S)" >> "$OUTPUT_FILE"
echo "----------------------------------------" >> "$OUTPUT_FILE"

# --- 1. Konfiguracja DNS (modyfikacja ISTNIEJĄCEGO połączenia Wi-Fi) ---

# Pobranie nazwy AKTUALNEGO połączenia Wi-Fi
CONNECTION_NAME=$(nmcli connection show --active | grep wifi | awk '{print $1}')

if [ -z "$CONNECTION_NAME" ]; then # Sprawdzamy, czy zmienna nie jest pusta
  log "Błąd: Nie znaleziono aktywnego połączenia Wi-Fi."
  exit 1
fi

log "1. Konfiguracja DNS dla połączenia '$CONNECTION_NAME'..."

# Ustawienie serwerów DNS (IPv4 i IPv6)
nmcli connection modify "$CONNECTION_NAME" ipv4.dns "8.8.8.8 1.1.1.1"
nmcli connection modify "$CONNECTION_NAME" ipv6.dns "2001:4860:4860::8888 2606:4700:4700::1111"

# Restart połączenia
nmcli connection down "$CONNECTION_NAME"
nmcli connection up "$CONNECTION_NAME"

# --- Reszta skryptu bez zmian ---
# Zapis konfiguracji połączenia do pliku...
log "Zapis konfiguracji połączenia do pliku..."
nmcli connection show "$CONNECTION_NAME" >> "$OUTPUT_FILE"

log "2. Instalacja narzędzi diagnostycznych..."
sudo dnf install traceroute net-tools bind-utils nmap -y

log "3. Diagnostyka sieci..."
log " a) Traceroute do $TARGET_HOST:"
traceroute -I "$TARGET_HOST" >> "$OUTPUT_FILE" 2>&1
log " b) Skanowanie sieci $NETWORK_CIDR (nmap -sP):"
nmap -sP "$NETWORK_CIDR" >> "$OUTPUT_FILE" 2>&1
log " c) Informacje o adresach IP (ip addr):"
ip addr >> "$OUTPUT_FILE" 2>&1
log " d) Tablica routingu (ip route):"
ip route >> "$OUTPUT_FILE" 2>&1
log " e) Aktywne połączenia sieciowe (ss):"
ss -tulnp >> "$OUTPUT_FILE" 2>&1

log "Raport zapisany do pliku: $OUTPUT_FILE"
exit 0
