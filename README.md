# Overview
<img src=Preview1.png/>

- **Window Manager:** [hyprland](https://github.com/hyprwm/Hyprland)
- **Shell** [fish](https://github.com/fish-shell/fish-shell)
- **Term** [Alacritty](https://github.com/alacritty/alacritty)
- **Browser** [Firefox](https://www.mozilla.org/en-US/firefox/) 
- **Bar** [eww](https://github.com/elkowar/eww)
- **Text Editor** [vim](https://github.com/vim/vim)
- **Music server** [mpd](https://github.com/MusicPlayerDaemon/MPD)
- **Sound Setup** [pipewire](https://gitlab.freedesktop.org/pipewire/pipewire/)
- **Font** [JetBrainsMono](https://github.com/JetBrains/JetBrainsMono)

# Installation
## OS
Install Arch with this guide: <a href=Arch-Install.md>Arch-Install.md<a/>

## Dotfiles
Clone this repo to home directory
```
git clone https://github.com/smravec/.dotfiles-hyprland ~/.dotfiles
```

## Dependencies
Install dependencies
```
paru -S hyprland eww-wayland hyprpaper-git \
        fish \
        ttf-jetbrains-mono ttf-material-design-icons breeze-snow-cursor-theme \
        wireplumber pipewire-jack pipewire-pulse \
        wofi cliphist \
        firefox alacritty superproductivity-bin \
        imv wl-clipboard wget tmux brightnessctl grim slurp mpd mpc kpcli \
        cmatrix neofetch \
        python python-pip nodejs \
        mesa
```
```
pip install yt-dlp
```

## Personalization (optional)
Copy your git token to hyprland config on line 136 to access it on shortcut Super + G
```
vim ~/.dotfiles/.config/hypr/hyprland.conf
```
also copy your git token to eww clipboard script on line 13 to not show it in the clipboard widget
```
vim ~/.dotfiles/.config/eww/Scripts/clipboard-mananger.py
```

## Final setup
copy all the files into their dirs
```
cp -r ~/.dotfiles/.config/* ~/.config/
cp -r ~/.dotfiles/home-dir/* ~/
```
refresh font cache
```
fc-cache -fv
```
# Keybinds
# Wm and Other Keybinds
|Keybind|Command|
|:-----:|:------:|
| super + t | Term|
|super + r | Launcher|
|super + f | Toggle floating tiled|
|super + q | Close window|
|super + up,down,left,right arrow| Change focus|
|super + 1-5| Change workspace|

****super = Windows Key****
## Alacritty keybinds
|Keybind|Command|
|:-----:|:------:|
|Ctrl + c| copy to clipboard|
|Ctrl + v |paste from clipboard|
|Ctrl + Shift + c| kill process|
|Ctrl + o| scroll up|
|Ctrl + p| scroll down|

## Vim keybinds
|Keybind|Command|
|:-----:|:------:|
|(Visual mode) Ctrl + y | copy to clipboard (system clipboard)|

## Tmux keybinds
|Keybind|Command|
|:-----:|:------:|
|Ctrl + x| Main prefix (replaces Ctrl + b)|
|Main prefix + .| Split term horizontally|
|Main prefix + /| Split term vertically|

## Custom Aliases
**mdownload** - download media from youtube <br/>
**dmount** - mount device as user (editable without sudo) <br/>

# Gallery
<img src=Preview2.png/>
<img src=Preview3.png/>
