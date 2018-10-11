@ECHO OFF

REM on appelle le fichier python chargé de la vérification du code 
REM on appelle pour cela le shell python (python.exe)
REM le cmd le trouve car son chemin se met dans les variables d'evnt 
REM à l'installation
python .git/hooks/verification_qualite.py


REM si le prog python trouve une erreur, il renvoie 1
REM Cette valeur est stocké dans la varaible d'evnt ERRORLEVEL
REM Donc si elle est différente de 0 on sort du programme avec exit
if %ERRORLEVEL% neq 0 (
    echo Commit refusé
    exit 1      
    )