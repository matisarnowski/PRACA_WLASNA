#!/bin/bash
set -e

# Sprawdzenie, czy skrypt jest uruchamiany na systemie z APT (charakterystyczne dla Debiana/Ubuntu)
if ! command -v apt &> /dev/null; then
  echo "Ten skrypt jest przeznaczony dla systemu używającego APT (np. Ubuntu)."
  exit 1
fi

# Instalacja Tilix
echo "Instalowanie Tilix..."
if ! command -v tilix &> /dev/null; then
    sudo apt update # Upewnij się, że lista pakietów jest aktualna
    sudo apt install -y tilix || { echo "Błąd podczas instalacji Tilix."; exit 1; }
else
    echo "Tilix jest już zainstalowany."
fi

# Instalacja zsh
echo "Instalowanie Zsh..."
if ! command -v zsh &> /dev/null; then
    sudo apt install -y zsh || { echo "Błąd podczas instalacji Zsh."; exit 1; }
else
    echo "Zsh jest już zainstalowany."
fi

# Zmiana domyślnej powłoki na zsh (jeśli nie jest już ustawiona)
if [ "$SHELL" != "$(which zsh)" ]; then
  echo "Zmiana domyślnej powłoki na Zsh dla użytkownika $(whoami)..."
  # chsh wymaga podania hasła interaktywnie, jeśli nie jest uruchamiany jako root dla innego użytkownika.
  # Jeśli skrypt jest uruchamiany z sudo, to zmieni powłokę dla roota.
  # Aby zmienić dla bieżącego użytkownika, który uruchamia sudo:
  sudo chsh -s $(which zsh) $(whoami) || { echo "Błąd podczas zmiany powłoki na Zsh. Spróbuj ręcznie: chsh -s $(which zsh)"; }
  echo "Może być konieczne ponowne zalogowanie, aby zmiana powłoki odniosła skutek."
else
  echo "Zsh jest już domyślną powłoką."
fi

# Pobranie i zastosowanie motywu Dracula w Tilix
# Upewnij się, że katalog istnieje
mkdir -p "$HOME/.config/tilix/schemes/"
echo "Pobieranie motywu Dracula dla Tilix..."
wget -qO "$HOME/.config/tilix/schemes/Dracula.json" https://raw.githubusercontent.com/dracula/tilix/master/Dracula.json || { echo "Błąd podczas pobierania motywu Dracula."; exit 1; }

# Instalacja Oh My Zsh (jeśli nie jest już zainstalowany)
echo "Sprawdzanie/Instalowanie Oh My Zsh..."
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  # Oh My Zsh install script will typically ask to change the shell, we can say no if already changed or handle it.
  # Użycie --unattended może pominąć interakcję, ale upewnij się, że to pożądane.
  # Jeśli chsh było uruchomione z sudo dla innego użytkownika, to 'sh -c ...' jako zwykły użytkownik jest OK.
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended || { echo "Błąd podczas instalacji Oh My Zsh."; exit 1; }
else
  echo "Oh My Zsh jest już zainstalowany."
fi

# Konfiguracja pliku .zshrc (jeśli nie istnieje lub chcemy dodać podstawy)
# Ta sekcja jest nieco ryzykowna jeśli .zshrc już istnieje i ma własne konfiguracje.
# Oh My Zsh tworzy domyślny .zshrc. Można by sprawdzić i dodać/zmienić ZSH_THEME i plugins.
echo "Konfigurowanie .zshrc..."
if [ -f "$HOME/.zshrc" ]; then
  echo ".zshrc już istnieje. Sprawdzanie i ewentualne dodawanie ustawień..."
  # Zmiana motywu na agnoster, jeśli nie jest ustawiony
  sed -i 's/ZSH_THEME=".*"/ZSH_THEME="agnoster"/' ~/.zshrc
  if ! grep -q 'ZSH_THEME="agnoster"' ~/.zshrc; then
    echo 'ZSH_THEME="agnoster"' >> ~/.zshrc
  fi
  # Dodawanie wtyczek, jeśli ich brakuje w linii plugins=(...)
  # To jest uproszczone, bardziej zaawansowane parsowanie mogłoby być potrzebne.
  if ! grep -q "plugins=(.*git.*)" ~/.zshrc; then
    sed -i '/plugins=(/s/)/ git)/' ~/.zshrc # Dodaje git jeśli brakuje
  fi
  if ! grep -q "plugins=(.*zsh-syntax-highlighting.*)" ~/.zshrc; then
    sed -i '/plugins=(/s/)/ zsh-syntax-highlighting)/' ~/.zshrc
  fi
  if ! grep -q "plugins=(.*zsh-autosuggestions.*)" ~/.zshrc; then
    sed -i '/plugins=(/s/)/ zsh-autosuggestions)/' ~/.zshrc
  fi
else
  echo "Tworzenie nowego pliku .zshrc z domyślnymi ustawieniami..."
  cat <<EOL > ~/.zshrc
export ZSH="\$HOME/.oh-my-zsh"
ZSH_THEME="agnoster"
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)
export TERM="xterm-256color"
source \$ZSH/oh-my-zsh.sh
EOL
fi

# Instalacja wtyczek dla Oh My Zsh (zsh-syntax-highlighting, zsh-autosuggestions)
# Oh My Zsh może je już zawierać lub instalować w inny sposób, ale to jest popularna metoda
echo "Instalowanie wtyczek Zsh (jeśli potrzebne)..."
ZSH_CUSTOM_PLUGINS_DIR="${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins"
mkdir -p "$ZSH_CUSTOM_PLUGINS_DIR"

if [ ! -d "${ZSH_CUSTOM_PLUGINS_DIR}/zsh-syntax-highlighting" ]; then
   echo "Instalowanie zsh-syntax-highlighting..."
   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM_PLUGINS_DIR}/zsh-syntax-highlighting" || { echo "Błąd podczas instalacji wtyczki zsh-syntax-highlighting."; exit 1; }
fi
if [ ! -d "${ZSH_CUSTOM_PLUGINS_DIR}/zsh-autosuggestions" ]; then
   echo "Instalowanie zsh-autosuggestions..."
   git clone https://github.com/zsh-users/zsh-autosuggestions.git "${ZSH_CUSTOM_PLUGINS_DIR}/zsh-autosuggestions" || { echo "Błąd podczas instalacji wtyczki zsh-autosuggestions."; exit 1; }
fi

# Wymuszenie zmiany powłoki na zsh w domyślnym profilu Tilix
# Upewnij się, że Tilix nie nadpisuje tego przy starcie, jeśli ma własne ustawienia profilu
# Czasami Tilix odczytuje domyślną powłokę systemu.
# Poniższe dconf może być konieczne, jeśli Tilix nie respektuje systemowej powłoki.
echo "Konfigurowanie Tilix do używania Zsh..."
# Pobranie UUID domyślnego profilu Tilix
# Ścieżka może się różnić w zależności od wersji Tilix
# Spróbujmy znaleźć domyślny profil w bardziej ogólny sposób, jeśli /default nie działa
DEFAULT_PROFILE_UUID=$(gsettings get com.gexperts.Tilix.ProfilesList default)
DEFAULT_PROFILE_UUID=$(echo "$DEFAULT_PROFILE_UUID" | tr -d "'") # Usuń apostrofy

if [ -n "$DEFAULT_PROFILE_UUID" ]; then
    TILIX_PROFILE_PATH="/com/gexperts/Tilix/profiles/${DEFAULT_PROFILE_UUID}/"
    # Sprawdź, czy ścieżka istnieje w dconf, zanim zaczniesz pisać
    if dconf list "$TILIX_PROFILE_PATH" &> /dev/null; then
        dconf write "${TILIX_PROFILE_PATH}use-custom-command" "true"
        dconf write "${TILIX_PROFILE_PATH}custom-command" "'/bin/zsh'" # Użyj /bin/zsh lub $(which zsh)
        echo "Domyślny profil Tilix ($DEFAULT_PROFILE_UUID) skonfigurowany do używania Zsh."
    else
        echo "Nie można znaleźć ścieżki dconf dla domyślnego profilu Tilix: $TILIX_PROFILE_PATH"
        echo "Może być konieczna ręczna konfiguracja Tilix lub ścieżka dconf jest inna."
    fi
else
    echo "Nie można odczytać domyślnego profilu Tilix z dconf. Pomijanie konfiguracji Tilix dla Zsh."
fi


# Pobranie i ustawienie domyślnego pliku dir_colors
echo "Konfigurowanie dir_colors..."
if [ -f "$HOME/.dir_colors" ];then
    mv ~/.dir_colors ~/.dir_colors_backup_$(date +%Y%m%d%H%M%S)
    echo "Istniejący .dir_colors przeniesiony do kopii zapasowej."
fi
wget -qO ~/.dir_colors https://raw.githubusercontent.com/seebi/dircolors-solarized/master/dircolors.256dark || echo "Ostrzeżenie: Nie udało się pobrać dircolors-solarized."
# Nie ma potrzeby eval tutaj, .zshrc/bashrc to zrobi przy source

echo "Konfiguracja zakończona. Uruchom ponownie Tilix lub otwórz nową sesję Zsh."
echo "Aby zmiany w .zshrc zadziałały natychmiast w bieżącej sesji (jeśli to Zsh), wykonaj: source ~/.zshrc"
echo "Opcjonalnie: Zainstaluj Powerline fonts (np. pakiet fonts-powerline w Ubuntu) dla poprawnego wyświetlania motywu Agnoster."