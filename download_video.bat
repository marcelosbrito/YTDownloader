@echo off
setlocal

rem Check if a URL is provided
if "%~1"=="" (
    echo Usage: download_video.bat ^<YouTube Video URL^>
    exit /b 1
)

rem Call the Python script with the provided URL
python ytDownloader.py %~1

rem Open the directory where the video is saved
explorer "D:\Marcelo\Downloads"

endlocal