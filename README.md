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



# Gallery
<img src=Preview2.png/>
<img src=Preview3.png/>
