@echo off
:start

set drive_a="C:\Users\cliljohn\Documents\DCD\EE1\"

rem Prompt the user for the search string
set /p search_string=Enter the search string: 

rem Prompt the user to choose the source directory
echo Choose the source directory:
echo 1. EE1
echo 2. EE2
set /p source_dir_choice=Enter 1 or 2: 


rem Set the source directory based on the user's choice
if %source_dir_choice% == 1 (
    set source_dir="C:\Users\cliljohn\Documents\DCD\EE1\"
    set dest_dir="C:\Users\cliljohn\Documents\DCD\EE1\TestMove1"
) else if %source_dir_choice% == 2 (
    set source_dir=%drive_a%
    set dest_dir="C:\Users\cliljohn\Documents\DCD\EE1\TestMove2"
) else (
    echo Invalid choice. Exiting.
    goto end
)



@REM rem destination directory
@REM if %source_dir_choice% == 1 (
@REM     set dest_dir=C:\Users\cliljohn\Documents\DCD\EE1\TestMove1
@REM ) else if %source_dir_choice% == 2 (
@REM     set dest_dir=C:\Users\cliljohn\Documents\DCD\EE1\TestMove2
@REM ) else (
@REM     echo Invalid choice. Exiting...
@REM     goto start
@REM )


rem Create the destination directory if it doesn't exist
if not exist "%dest_dir%" mkdir "%dest_dir%"

rem Copy the files that contain the search string
for %%f in ("%source_dir%\*") do (
    if "%%~nxf" gtr "" if "%%~nxf" lss "" (
        copy "%%f" "%dest_dir%"
        echo Copied file: %%~nxf
    )
)

echo.
echo File copy complete.
echo.

goto start

:end