@echo off
chcp 65001 > nul
echo ========================================================
echo   CeylonGo - Auto Push ^& Deploy to GitHub
echo ========================================================
echo.
git status
echo.
git add .
set /p msg="Commit message eka gahanna (Neththan ENTER obanna): "
if "%msg%"=="" set msg=Update CeylonGo website
git commit -m "%msg%"
echo.
echo Pushing changes to GitHub...
git push origin main
echo.
echo ========================================================
echo   ✅ Done! Changes sent to GitHub successfully!
echo ========================================================
pause

