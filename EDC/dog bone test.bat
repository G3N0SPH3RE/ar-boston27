@REM dog.bone.test

@REM copy files and transfer to test pc for Documentation. Move files from station origin to desktop.
@REM Later, add weekly removal of weekly desktop file horde.

@echo off
:::: :::::::-.      ...       .,-:::::/      :::::::.      ...   :::.    :::..,::::::::::::::::::.,:::::: .::::::.::::::::::::
::::  ;;,   `';, .;;;;;;;.  ,;;-'````'        ;;;'';;'  .;;;;;;;.`;;;;,  `;;;;;;;'''';;;;;;;;'''';;;;'''';;;`    `;;;;;;;;''''
::::  `[[     [[,[[     \[[,[[[   [[[[[[/     [[[__[[\.,[[     \[[,[[[[[. '[[ [[cccc      [[      [[cccc '[==/[[[[,    [[     
::::   $$,    $$$$$,     $$$"$$c.    "$$ cccc $$""""Y$$$$$,     $$$$$$ "Y$c$$ $$"""" cccc $$      $$""""   '''    $    $$     
::::   888_,o8P'"888,_ _,88P `Y8bo,,,o88o    _88o,,od8P"888,_ _,88P888    Y88 888oo,__    88,     888oo,__88b    dP    88,    
::::   MMMMP"`    "YMMMMMP"    `'YMUP"YMM    ""YUMMMP"   "YMMMMMP" MMM     YM """"YUMMM   MMM     """"YUMMM"YMmMY"     MMM    

for /f "delims=: tokens=*" %%A in ('findstr /b :::: "%~f0"') do @echo(%%A)


@REM #################################################

@echo off
:start

set dir_ee1=/var/TestResults/EE1
set dir_ee2=/var/TestResults/EE2
set dest_dir=C:\ARTE\TEST_REPORT_ARCHIVE

@REM ssh sprocket:sprocket@11.200.1.10
@REM ssh -i %userprofile%\\.ssh\\bot_id_rsa
set username=sprocket
set password=sprocket
set remote_host=11.200.1.10

@REM ~~~~~~~~~~~~FOR TESTING~~~~~~~~~
@REM set dir_ee1=C:\Users\cliljohn\Documents\DCD\EE1
@REM set dir_ee2=C:\Users\cliljohn\Documents\DCD\EE2
@REM set dest_dir=C:\Users\cliljohn\Documents\DCD\EE1\TestMove

pause

rem Log in to the remote server via SSH
plink.exe -ssh %username%@%remote_host% -pw %password% ^
    "echo Successfull Login..."
    @REM "cd /var/TestResults/EE1; ^
pause /t 2 > nul

@rem -ssh option specifies that we want to use the SSH protocol. The -pw option specifies the password.


echo To copy and backup test files from test station...
rem Prompt the user for the partial file name
set /p partial_filename=Enter the partial file name: 

:source
rem Prompt the user to choose the source directory
echo Choose the source directory:
echo 1. EE1
echo 2. EE2
set /p source_dir_choice=Enter 1 or 2: 
echo.

rem Set the source directory based on the user's choice
if %source_dir_choice% == 1 (
    set source_dir=%dir_ee1%
) else if %source_dir_choice% == 2 (
    set source_dir=%dir_ee2%
) else (
    echo Invalid choice. Exiting.
    goto source
)

rem Set the destination directory


rem Create the destination directory if it doesn't exist
if not exist "%dest_dir%" mkdir "%dest_dir%"

rem Copy the files that match the partial file name
for %%f in ("%source_dir%\*%partial_filename%*") do (
    copy "%%f" "%dest_dir%"
    echo Copied file: %%~nxf
)

echo.
echo File copy complete.
echo.
echo.

set /p new_cp=Try another; Y / N : 
if /i %new_cp% == y (
    echo ~~~~~~~ New Entry ~~~~~~~
    echo.
    goto start
)   else if /i %new_cp% == n (
    echo You are finished.
    goto end
)


:end