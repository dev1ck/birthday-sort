@echo off

rem 코드 페이지를 UTF-8로 변경
chcp 65001

set PYINSTALLER_PATH=C:\Users\firej\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts
set OUTPUT_FOLDER=%~dp0output
set SCRIPT_NAME=birthday.py
set PROGRAM_NAME=birthday_sorter
set ICON_PATH=resources\icon.ico
set FINAL_NAME=생일자정렬기.exe
set SHORTCUT_NAME=생일자정렬기.lnk
set ZIP_NAME=생일자정렬기.zip

if not exist %OUTPUT_FOLDER% mkdir %OUTPUT_FOLDER%

%PYINSTALLER_PATH%\pyinstaller.exe --icon=%~dp0%ICON_PATH% --windowed --noconfirm --name %PROGRAM_NAME% --distpath %OUTPUT_FOLDER% %SCRIPT_NAME%

rem 빌드된 실행 파일 디렉토리 설정
set DIST_FOLDER=%OUTPUT_FOLDER%\%PROGRAM_NAME%

rem 빌드 후 리소스 폴더 복사
xcopy %~dp0resources %DIST_FOLDER%\resources /E /I /Y

rem 빌드된 실행 파일 이름 변경 및 이동
ren "%DIST_FOLDER%\%PROGRAM_NAME%.exe" "%FINAL_NAME%"

rem 폴더 압축
tar -cvf %~dp0%ZIP_NAME% -C %OUTPUT_FOLDER% .

pause
