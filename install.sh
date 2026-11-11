#!/bin/bash
count=4
clear
echo "0/$count   INSTALLING GIT"
pacman -Sy --noconfirm --overwrite '*' git > /dev/null 2>&1
echo "1/$count   INSTALLING PYTHON"
pacman -Sy --noconfirm --overwrite '*' python > /dev/null 2>&1
echo "2/$count   CLONING THE REPO"
ls /tmp
git clone -q https://github.com/Wjanek13/archinstall /tmp/archinstall 1>/dev/null 2>/dev/null
ls /tmp
echo "3/$count   WIPING OLDER INSTALLATION SCRIPTS"
rm -rf /tmp/archinstall
echo "4/$count   RUNNING THE SCRIPT"
cd /tmp/archinstall
python3 main.py
