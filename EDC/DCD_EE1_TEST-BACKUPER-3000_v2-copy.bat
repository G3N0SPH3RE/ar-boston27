@echo off

setlocal EnableDelayedExpansion
@REM ssh sprocket:sprocket@11.200.1.10

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
for /R "D:\GOES DATA CENTER" %%i in ("*T1700???.jpg") do copy "%%~i" "D:\destination folder\"
rem Copy the file from the Test Controller to local machine
for %%I in (%partial_filename%*) do (
    if %directory% == EE1 (
        scp var/TestResults/EE1/%%~nI* . "C:/ARTE/Test_Reports/EE1"
    ) else if %directory% == EE2 (
        scp var/TestResults/EE2/%%~nI* . "C:/ARTE/Test_Reports/EE2"
    ) else (
        echo Invalid directory. Please enter EE1 or EE2.
        goto end
    )
)


echo File copy complete.

:end