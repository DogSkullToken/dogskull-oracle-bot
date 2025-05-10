@echo off
echo 🔮 Starting DogSkull Oracle Bot...

REM Ativa o ambiente virtual
call venv\Scripts\activate.bat

REM Instala as dependências com força total
pip install --force-reinstall -r requirements.txt

REM Executa o bot
python main.py

pause
