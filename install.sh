#!/bin/bash
clear
pacman -Sy --noconfirm --overwrite '*' python git
rm -rf /tmp/archinstall
git clone https://github.com/Wjanek13/archinstall /tmp/archinstall
cd /tmp/archinstall
python3 main.py
