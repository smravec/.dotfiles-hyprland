#Global vars
#Welcome message when starting fish
set -U -x fish_greeting ""

#Fixes for bspwm

if status is-interactive
    	
	#Global Path
	set -Ua fish_user_paths /home/$USER/.config/fish/scripts
	set -Ua fish_user_paths /home/$USER/.local/bin
	set -Ua fish_user_paths /home/$USER/.config/hypr/Scripts
end

if status --is-login

	#Automatically execute startx on login and hide its output
	if test -z "$DISPLAY"
  		/home/simon/.config/fish/scripts/startw
  end	
end
