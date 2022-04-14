#!/bin/bash

echo "Iniciando instalação de pacotes"

sudo apt-get update && apt-get upgrade
sudo apt-get install python3 python3-pip
sudo apt-get install mpv flac cmatrix

pip install -r requeriments.txt
pipwin install pyaudio