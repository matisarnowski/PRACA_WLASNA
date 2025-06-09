#!/bin/bash
set -e

# Sprawdzenie, czy skrypt jest uruchamiany na Fedorze
if ! command -v dnf &> /dev/null; then
  echo "Ten skrypt jest przeznaczony dla systemu Fedora."
  exit 1
fi

# Instalacja Tilix
if ! command -v tilix &> /dev/null; then
    sudo dnf install tilix -y || { echo "Błąd podczas instalacji Tilix."; exit 1; }
else
    echo "Tilix jest już zainstalowany."
fi

# Instalacja zsh
if ! command -v zsh &> /dev/null; then
    sudo dnf install zsh -y || { echo "Błąd podczas instalacji Zsh."; exit 1; }
else
    echo "Zsh jest już zainstalowany."
fi

# Zmiana domyślnej powłoki na zsh (jeśli nie jest już ustawiona)
if [ "$SHELL" != "$(which zsh)" ]; then
  chsh -s $(which zsh) || { echo "Błąd podczas zmiany powłoki na Zsh."; exit 1; }
else
  echo "Zsh jest już domyślną powłoką."
fi

# Pobranie i zastosowanie motywu Dracula w Tilix (skrócona wersja)
wget -qO- https://raw.githubusercontent.com/dracula/tilix/master/Dracula.json --directory-prefix=$HOME/.config/tilix/schemes/ || { echo "Błąd podczas pobierania motywu Dracula."; exit 1; }

# Instalacja Oh My Zsh (jeśli nie jest już zainstalowany)
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended || { echo "Błąd podczas instalacji Oh My Zsh."; exit 1; }
else
  echo "Oh My Zsh jest już zainstalowany."
fi

# Konfiguracja pliku .zshrc (jeśli nie istnieje)
if [ ! -f "$HOME/.zshrc" ]; then
  cat <<EOL >> ~/.zshrc
ZSH_THEME="agnoster"
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
export TERM="xterm-256color"
source ~/.oh-my-zsh/oh-my-zsh.sh
EOL
else
  echo ".zshrc już istnieje - sprawdź, czy zawiera wymagane ustawienia."
fi

# Wtyczki powinny być już obsłużone przez Oh My Zsh, ale dla pewności:
for plugin in zsh-syntax-highlighting zsh-autosuggestions; do
  if [ ! -d "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/$plugin" ]; then
     git clone https://github.com/zsh-users/$plugin.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/$plugin || { echo "Błąd podczas instalacji wtyczki $plugin."; exit 1; }
  fi
done

# Wymuszenie zmiany powłoki na zsh w Tilix
tilix_profile=$(dconf read /com/gexperts/Tilix/profiles/default | tr -d "'")
dconf write /com/gexperts/Tilix/profiles/$tilix_profile/use-custom-command true
dconf write /com/gexperts/Tilix/profiles/$tilix_profile/custom-command "'/bin/zsh'"

# Pobranie i ustawienie domyślnego pliku dir_colors
if [ -f "$HOME/.dir_colors" ];then
    mv ~/.dir_colors ~/.dir_colors_backup
fi
wget -O ~/.dir_colors https://raw.githubusercontent.com/seebi/dircolors-solarized/master/dircolors.256dark
eval $(dircolors ~/.dir_colors)

# Zastosowanie zmian
source ~/.zshrc

echo "Konfiguracja zakończona. Uruchom ponownie Tilix."
echo "Opcjonalnie: Zainstaluj Powerline fonts dla poprawnego wyświetlania motywu Agnoster."
