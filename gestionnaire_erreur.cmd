@ECHO OFF

python .git/hooks/verification_qualite.py

if %ERRORLEVEL% neq 0 (
    echo Commit refusé
    exit 1      
    )