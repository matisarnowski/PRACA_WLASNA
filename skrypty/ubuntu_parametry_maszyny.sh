#!/bin/bash

echo "--- Informacje o procesorze (CPU) ---"
lscpu | grep "Model name"

echo "\n--- Informacje o pamięci RAM ---"
free -h | grep "Mem"

echo "\n--- Informacje o karcie graficznej (GPU) ---"
lspci | grep -E "VGA|3D"

echo "\n--- Informacje o dyskach ---"
df -h /

echo "\n--- Informacje o rozdzielczości ekranu ---"
xrandr | grep "*current"
