#!/usr/bin/env bash
# Remember to give this script execution permission by all users:
# chmod a+x startBot.sh

while true
do
# Loop to wait until internet connnection is ready
  if nc -zw1 google.com 443; then
    # When there is response from google.com @ https
    python ./RPi_IP_TelegramBot.py &
    # End loop and quit
    break
  fi
done
