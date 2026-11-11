#!/bin/bash
clear
pacman -Sy --noconfirm --overwrite '*' python git > /dev/null 2>&1
rm -rf /tmp/archinstall > /dev/null 2>&1
git clone -q https://github.com/Wjanek13/archinstall /tmp/archinstall > /dev/null 2>&1
cd /tmp/archinstall > /dev/null 2>&1
python3 main.py
