#!/bin/bash

# Instalacja narzędzi sieciowych na Fedora 40

# 1. iftop - Monitorowanie przepływu danych w sieci w czasie rzeczywistym
sudo dnf install -y iftop

# 2. nload - Wizualizacja ruchu sieciowego w formie wykresu
sudo dnf install -y nload

# 3. bmon - Monitorowanie przepustowości sieci i statystyk
sudo dnf install -y bmon

# 4. speedtest-cli - Pomiar prędkości łącza internetowego
sudo dnf install -y speedtest-cli

# 5. macchanger - Zmiana (randomizacja) adresu MAC interfejsu sieciowego
sudo dnf install -y macchanger

# 6. mtr - Śledzenie trasy pakietów oraz ich opóźnień
sudo dnf install -y mtr

# 7. tcpdump - Przechwytywanie i analizowanie ruchu sieciowego
sudo dnf install -y tcpdump

# 8. htop - Interaktywne monitorowanie procesów systemowych (dodatkowe narzędzie)
sudo dnf install -y htop

echo "Instalacja narzędzi sieciowych zakończona."
