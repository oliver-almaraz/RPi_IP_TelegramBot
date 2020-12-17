# RPi_IP_TelegramBot
Script that runs on startup to send device's IP to a Telegram bot. Usefull for headless devices without static IP, like a Raspberry Pi you will take here and there.

Download and extract both scripts in any location (both scripts must be in the same directory).
Install dependencies:
  - `sudo apt install netcat` (for arch based distros: `sudo pacman -Syyuu gnu-netcat`
  - Only if pip is not installed: (verify with `pip --version`)
    - `apt install python-pip`
    - `echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.profile`
    - `. ~/.profile`
  - `sudo pip install telegram_send`
  - `telegram-send --configure` (you will need to create a bot using Telegram's BotFather interface and inser bot's token)
  
  - Only for Arch based distributions (like Manjaro) you need to install cronie:
    - `sudo pacman -Syyuu cronie`
    - `sudo systemctl enable cronie.service`
  - `EDITOR=nano crontab -e`
  - Add: `@reboot <path to startBot.sh>`
  - `chmod a+x <path to startBot.sh>`
  - Reboot and try!
