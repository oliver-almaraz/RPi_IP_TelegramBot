import socket
import telegram_send

## Dependencies:
# pip install telegram_send
# telegram-send --configure

# If pip is not installed:
# sudo apt install python-pip (or for Arch based distros: sudo pacman -Syyuu python pip)
# echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.profile
# . ~/.profile

host_name = socket.gethostname()
IP_addres = socket.gethostbyname(host_name)
telegram_send.send(messages=[f"IP adress for '{host_name}' is:\n{IP_addres}"])
