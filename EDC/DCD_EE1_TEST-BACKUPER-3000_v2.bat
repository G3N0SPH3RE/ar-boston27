@echo off
:start

setlocal EnableDelayedExpansion
@REM ssh sprocket:sprocket@11.200.1.10

@REM set "source_dir=var/TestResults/"
@REM set "dest_dir=C:/ARTE/Test_Reports/"
@REM set "archive_dir=/var/BackupTests/"

@REM ~~~~~~TESTING~~~~~~
set "source_dir=C:\Users\cliljohn\Documents\DCD\EE1\"
set "dest_dir=C:\Users\cliljohn\Documents\DCD\EE1\TestMove"
set "archive_dir=/var/BackupTests/"

rem Prompt the user for SN
set /p partial_filename=Enter the SN to copy: 

rem Prompt the user for the directory (EE1 or EE2)
set /p directory=Enter the directory (EE1 or EE2): 

@REM rem Prompt the user for the SSH username and password
@REM set /p username=Enter the SSH username: 
@REM set /p password=Enter the SSH password: 

@REM rem Copy the file from the Test Controller to local machine
@REM if %directory% == EE1 (
@REM     scp %username%:%password%@11.200.1.10:/var/TestResults/EE1/%partial_filename%* .
@REM ) else if %directory% == EE2 (
@REM     scp %username%:%password%@11.200.1.10:/var/TestResults/EE2/%partial_filename%* .
@REM ) else (
@REM     echo Invalid directory. Please enter EE1 or EE2.
@REM     goto end
@REM )

rem Copy the file from the Test Controller to local machine

if not exist "C:\Users\cliljohn\Documents\DCD\EE1\TestMove\" mkdir C:\Users\cliljohn\Documents\DCD\EE1\TestMove

for %%I in (%partial_filename%*) do (
    if %directory% == EE1 (
        scp C:\Users\cliljohn\Documents\DCD\EE1\%%~nI* . "C:\Users\cliljohn\Documents\DCD\EE1\TestMove"
    ) else if %directory% == EE2 (
        scp var/TestResults/EE2/%%~nI* . "C:/ARTE/Test_Reports/EE2"
    ) else (
        echo Invalid directory. Please enter EE1 or EE2.
        goto start
    )
)


@REM rem Copy the file with the matching partial serial number
@REM for %%f in (%source_dir%*) do (
@REM     if "%%~nf" gtr "" if "%%~nf" lss "" if "%%~nf" contains "%partial_filename%" (
@REM         copy "%%f" "%dest_dir%"
@REM         echo File copied: %%~nxf
@REM     )
@REM )

echo.
echo File copy complete...
echo.
goto start
:end