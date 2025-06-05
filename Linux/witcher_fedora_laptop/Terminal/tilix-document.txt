#!/bin/bash

# Instalacja Tilix
sudo dnf install tilix -y

# Instalacja zsh
sudo dnf install zsh -y

# Zmiana domyślnej powłoki na zsh
chsh -s $(which zsh)

# Pobranie i zastosowanie motywu Dracula w Tilix
mkdir -p ~/.config/tilix/schemes
wget -O ~/.config/tilix/schemes/Dracula.json https://raw.githubusercontent.com/dracula/tilix/master/Dracula.json

# Konfiguracja pliku .zshrc
cat <<EOL >> ~/.zshrc
ZSH_THEME="agnoster"
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
export TERM="xterm-256color"
source ~/.oh-my-zsh/oh-my-zsh.sh
EOL

# Instalacja Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Instalacja zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# Instalacja zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Wymuszenie zmiany powłoki na zsh w Tilix
tilix_profile=$(dconf read /com/gexperts/Tilix/profiles/default | tr -d "'")
dconf write /com/gexperts/Tilix/profiles/${tilix_profile}/use-custom-command true
dconf write /com/gexperts/Tilix/profiles/${tilix_profile}/custom-command "'/bin/zsh'"

# Pobranie i ustawienie domyślnego pliku dir_colors
mv ~/.dir_colors ~/.dir_colors_backup
wget -O ~/.dir_colors https://raw.githubusercontent.com/seebi/dircolors-solarized/master/dircolors.256dark
eval $(dircolors ~/.dir_colors)

# Zastosowanie zmian
source ~/.zshrc
