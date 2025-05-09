#!/bin/bash

# Instalacja dconf-cli (jeśli jeszcze nie jest zainstalowane)
sudo dnf install dconf

# Pobranie i instalacja motywu Dracula dla Gnome Terminal
git clone https://github.com/dracula/gnome-terminal
cd gnome-terminal
./install.sh
cd ..
rm -rf gnome-terminal

# Konfiguracja pliku .bashrc
cat <<EOL >> ~/.bashrc
# Włącz podświetlanie składni w bashu
if [ -f /etc/bashrc ]; then
    source /etc/bashrc
fi

# Ustawienia kolorów dla bash (PS1 prompt)
export PS1="\[\e[35m\]\u@\h \[\e[36m\]\w\[\e[0m\] $ "
export TERM="xterm-256color"
EOL

# Zastosowanie zmian
source ~/.bashrc
