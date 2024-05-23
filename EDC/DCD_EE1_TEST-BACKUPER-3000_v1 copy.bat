@echo off

setlocal EnableDelayedExpansion

rem Set the directory to monitor and the destination directory
set "source_dir=E:\var\TestResults\EE1"
set "dest_dir=C:\EE1"
set "archive_dir=E:\Desktop\New_Assets"

:loop
rem Copy new files from E:\var\TestResults\EE1\ to C:\EE1\
robocopy "E:\var\TestResults\EE1\" "C:\EE1\" /e /ndl /nfl @rem /np

rem Move all files from E:\var\TestResults\EE1\ to E:\Desktop\New_Assets
if exist "E:\var\TestResults\EE1\*.*" (
    move "E:\var\TestResults\EE1\*.*" "E:\Desktop\New_Assets"
)

rem Grab the day of the week and the specified time (0=Sunday, 1=Monday, ..., 6=Saturday)
for /f "tokens=1,2 delims==" %%i in ('wmic path win32_localtime get DayOfWeek^,Hour^,Minute /format:table') do (
    if "%%i"=="DayOfWeek" set "day_of_week=%%j"
    if "%%i"=="Hour" set "hour=%%j"
    if "%%i"=="Minute" set "minute=%%j"
)

@REM rem Delete files in archive_dir every Sunday at 23:00
@REM if %day_of_week% equ 0 if %hour% equ 23 if %minute% equ 0 (
@REM     del /q "%archive_dir%\*.*"
@REM )

rem Wait for 60 seconds before checking again
timeout /t 300 > nul
goto loop


@rem Here's how it works:

@rem The script starts by setting the source directory (source_dir), destination directory (dest_dir), and archive directory (archive_dir).

@rem The script then enters a loop that runs continuously.

@rem Inside the loop, the script uses the robocopy command to copy any new files from the source_dir to the dest_dir. The /e
@rem copies subdirectories, /ndl suppresses directory names, /nfl suppresses file names, and /np suppresses progress percentage.

@rem The script then checks if there are any files in the source_dir . If there are any they are moved to archive_dir

@rem The script then gets the current week, hour, and minute using the wmic command and stores them as day_of_week, hour, and minute

@rem Then checks if the current day = Sunday (0), hour 2300 (11:00 PM), and the minute 0. If all these conditions are met, files in archive_dir
@rem  with deleted.

@rem The script then waits 60 seconds using timeout /t 300 nul (5 minutes) before repeating loop.

@rem ~~~~~~~~~~~~ EXTRAS ~~~~~~~~~~~~
@rem Basic copy script below:


@rem rem Copy the file to C:/EE1/
@rem copy E:\var\TestResults\EE1\x.txt C:\EE1\

@rem rem Move the file to ..\TestREsults\EE1\ to E:\Deskto\New_Assets
@rem move E:\var\TestResults\EE1\x.txt E:\Desktop\New_Assets

@rem echo File copy and move operation completed.