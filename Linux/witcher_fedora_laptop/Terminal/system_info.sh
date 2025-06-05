#!/bin/bash

# Zbieranie informacji o systemie
echo "=== Informacje o systemie ==="
hostnamectl

echo ""
echo "=== Informacje o procesorze ==="
lscpu

echo ""
echo "=== Informacje o pamięci RAM ==="
free -h

echo ""
echo "=== Informacje o dyskach ==="
lsblk

echo ""
echo "=== Informacje o systemie plików ==="
df -hT

echo ""
echo "=== Informacje o karcie graficznej ==="
lspci -vnn | grep -i VGA

echo ""
echo "=== Informacje o sieci ==="
ip a
