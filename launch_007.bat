@echo off 
TITLE Project 007 - Browser UI 
cd /d "C:\Users\ASHFAQ AHMAD\project007" 
start python main.py 
timeout /t 3 
start chrome http://localhost:5000 
