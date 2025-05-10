#!/bin/bash

echo "🔧 Iniciando configuração do ambiente DogSkull Oracle Bot..."

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Bibliotecas instaladas:"
pip list

echo -e "\n🚀 Tudo pronto! Para iniciar seu bot, use:\n"
echo "source venv/bin/activate && python main.py"
