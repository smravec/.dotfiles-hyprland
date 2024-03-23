# Arch Linux install guide

### Before install
1. download arch iso and flash it onto usb stick with BalenaEtcher
2. plug usb stick into the machine
3. enter bios by pressing f2 (also might be f6 f10 or del) when booting and put the usb stick to the top of the boot order
4. save changes, exit and reboot

## Connect to internet (wifi)
start iwctl
```
iwctl 
```
scan for networks
```
station wlan0 scan
```
show all available networks
```
station wlan0 get-networks
```
connect to network
```
station wlan0 connect NAME_OF_NETWORK
```

## Set up system clock and timezones
list all timezones (exit with q)
```
timedatectl list-timezones
```
set timezone
```
ln -sf /usr/share/zoneinfo/Europe/Bratislava /etc/localtime
```
sync clock
```
timedatectl set-ntp true
```
```
hwclock --systohc
```
## Partition your disk
list all available disks
```
fdisk -l
```
start partitioning your disk (could be named /dev/sda, /dev/nvme0n1 or /dev/mmcblk0, I will use /dev/nvme0n1)
```
fdisk /dev/nvme0n1
```
view all the commands for fdisk
```
m
```
create a new gpt table
```
g
```
create 4 partitions (EFI, SWAP, ROOT and HOME)
### EFI (create partition, assign the number 1 to it, select how big it should be, change the type to EFI partition)
```
n
1
(just press enter)
+350M
t
1
1
```
### SWAP (create partition, assing the number 2 to it, select how big it should be, change the type to Linux swap)
```
n
2
(just press enter)
```
depends on size of ram but 10G should be good
```
+10G
```
change the type to Linux swap
```
t
2
```
to get this number type L which prints all available partition types
```
19
```
### Linux root filesystem (create new partition, assign the number 3 to it, select how big it should be, dont have to change the type)
```
n
3
(just press enter)
+140G
```

### Linux home filesystem (create new partition, assign the number 4 to it, select how big it should be, dont have to change the type)
```
n
4
(just press enter)
(just press enter)
```
to save all changes press w
```
w
```
## Format partitions
format the EFI, SWAP, ROOT and HOME partitions (and enable swap)
```
mkfs.fat -F32 /dev/nvme0n1p1
mkswap /dev/nvme0n1p2
swapon /dev/nvme0n1p2
mkfs.ext4 /dev/nvme0n1p3
mkfs.ext4 /dev/nvme0n1p4
```
## Install base
mount all partitions except swap on /mnt
```
mount /dev/nvme0n1p3 /mnt
mkdir /mnt/boot
mount /dev/nvme0n1p1 /mnt/boot
mkdir /mnt/home
mount /dev/nvme0n1p4 /mnt/home
```
install linux
```
pacstrap /mnt base linux-lts linux-firmware
```
generate fstab (save partition mount points)
```
genfstab -U /mnt >> /mnt/etc/fstab
```
## Chroot
change root into the new arch install
```
arch-chroot /mnt
```
setup clock and timezone again
```
ln -sf /usr/share/zoneinfo/Europe/Bratislava /etc/localtime
hwclock --systohc 
```
download vim (basic vim commands: I to enter insert mode, Esc to exit insert mode, to exit and save :wq (also you have to be out of insert mode), to just exit without saving :q! (also you have to be out of insert mode))
```
pacman -S vim
```
### Localisation
setup keyboard layout
```
vim /etc/locale.gen
```
find this line
```
#en_US.UTF-8 UTF-8 
```
uncomment it e.g.
```
en_US.UTF-8 UTF-8
```
generate locale
```
locale-gen
```
setup en_US.UTF-8 as default fallback
```
echo "LANG=en_US.UTF-8" >> /etc/locale.conf
```
### Networking
setup hostname (replace framework for your hostname)
```
echo "framework" >> /etc/hostname
```
setup hosts (ip lookup table)
```
vim /etc/hosts
```
copy this into /etc/hosts (replace framework for your hostname)
```
127.0.0.1   localhost
::1         localhost
127.0.1.1   framework.localdomain  framework
```
### Permissions
setup root password
```
passwd 
```
add user, set password and give permissions (replace simon with your username)
```
useradd -m simon
passwd simon
usermod -aG wheel simon
```
download sudo with pacman
```
pacman -S sudo
```
setup sudo
```
visudo
```
find this line
```
#%wheel ALL=(ALL:ALL) ALL
```
uncomment it e.g.
```
%wheel ALL=(ALL:ALL) ALL
```
save and exit by pressing Ecs and :wq

## Bootloader (EFISTUB)
install efibootmgr
```
pacman -S efibootmgr
```
get partuuid of your root partition
```
vim /etc/fstab
```
copy the string next to UUID= (my root partition is /dev/nvme0n1p3)
```
# /dev/nvme0n1p3
UUID=17ccf50c-592a-41c2-ac96-ec3f8157385c	/         	ext4      	rw,relatime	0 1
```
add efi entry (replace after --disk your disk, after --part number of boot partition, after UUID= your UUID of root partition) 
```
efibootmgr --disk /dev/nvme0n1 --part 1 --create --label "Arch Linux" --loader /vmlinuz-linux-lts --unicode 'root=UUID=17ccf50c-592a-41c2-ac96-ec3f8157385c rw quiet loglevel=3 rd.systemd.show_status=false rd.udev.log_level=3 vt.global_cursor_default=0 initrd=/intel-ucode.img initrd=/initramfs-linux-lts.img'
```
check if everything is correct
```
efibootmgr -u
```
on next reboot check in bios if entry "Arch Linux" is on top of the boot order

## Other packages install and setup
install base packages 
```
pacman -S base-devel dhcpcd wpa_supplicant intel-ucode linux-lts-headers git man-pages man-db
```
## Reboot
exit chroot
```
exit
```
unmount file system
```
umount -R /mnt
```
reboot pc and remove usb stick
```
reboot
```
# POST INSTALLATION
# Wifi
login as root
```
su
```
edit wpa supplicant config file  (make one if none is present)
```
# vim /etc/wpa_supplicant/wpa_supplicant.conf
```
make it look like this
```
ctrl_interface=DIR=/var/run/wpa_supplicant
update_config=1
```
save and exit
```
:wq
```
add your wifi ssid and password
```
# wpa_passphrase MyNetwork MyPassword >> /etc/wpa_supplicant/wpa_supplicant.conf
```
get your wifi card name(could be something like wlan or wlp..  mine is wlp170s0)
```
ip link
```
rename your wpa supplicant config to include you wifi card name (replace wlp170s0 with yours)
```
# mv /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant-wlp170s0.conf
```

start wpa_supplicant and dhcpcd service
```
# systemctl enable wpa_supplicant@wlp170s0.service
# systemctl enable dhcpcd.service
```
and finally reboot reboot
```
# reboot
```
## Pacman and aur
download the archlinux-keyring package
```
sudo pacman -S archlinux-keyring
```
sync databases and update all packages
```
sudo pacman -Syu
```
download yay (aur package manager)
```
git clone https://aur.archlinux.org/paru.git
```
install yay
```
cd ./paru
makepkg -si
```
## Silent boot
Follow arch wiki here: https://wiki.archlinux.org/title/silent_boot 
