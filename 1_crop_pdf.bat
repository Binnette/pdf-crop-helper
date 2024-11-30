@echo off
setlocal

REM Create the virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Install the necessary libraries
pip install pymupdf pillow

REM Run the Python file picker script and get the selected file's full path
for /f "delims=" %%i in ('python file_picker.py') do set "PDF_PATH=%%i"

if "%PDF_PATH%"=="No file selected" (
    echo No file selected.
    pause
    exit /b 1
)

if "%PDF_PATH%"=="" (
    echo No file selected.
    pause
    exit /b 1
)

REM Run pdf_cropper.py with the selected PDF file
python pdf_cropper.py "%PDF_PATH%"

echo Process completed.
pause

endlocal
