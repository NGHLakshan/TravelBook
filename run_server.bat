@echo off
title CeylonGo Web Platform
echo ========================================================
echo        CEYLONGO TRAVEL & AFFILIATE PLATFORM
echo ========================================================
echo.
echo Starting Django Development Server...
echo.
echo Website URL:        http://127.0.0.1:8000/
echo Quick Code Lookup:  http://127.0.0.1:8000/lookup/
echo Admin Dashboard:    http://127.0.0.1:8000/admin/
echo.
echo Default Admin Login:
echo Username: admin
echo Password: admin123
echo ========================================================
echo.
.\venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
pause

