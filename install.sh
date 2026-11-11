#!/bin/bash
clear
pacman -Sy --noconfirm --overwrite '*' python git > /dev/null 2>&1
rm -rf /tmp/archinstall
git clone https://github.com/Wjanek13/archinstall /tmp/archinstall
cd /tmp/archinstall
python3 main.py
