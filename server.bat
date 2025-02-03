@echo off
cd .\alz2env\Scripts\
call .\activate
cd..
cd..
cd .\src\
start  python manage.py runserver
timeout /t 3
start http://127.0.0.1:8000
