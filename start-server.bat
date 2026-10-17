@echo off
title Metal Tetris Server
cd /d "%~dp0"
echo ========================================================
echo   [Metal Tetris] 俄罗斯方块本地服务启动中...
echo ========================================================
echo.
echo 本机访问:   http://localhost:8080
echo 手机局域网: http://192.168.1.6:8080
echo.
echo 提示 1: 手机连上同一 Wi-Fi，在浏览器直接输入上面的网址即可
echo 提示 2: 手机若开了 VPN / 代理软件，请先断开或开启局域网直连
echo ========================================================
python server.py 8080
pause
