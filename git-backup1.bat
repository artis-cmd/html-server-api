@echo off

:: 현재 폴더 기준에서 .git 있는지 확인
if not exist .git (
    echo [오류] .git 폴더가 없습니다. git init이 필요합니다.
    pause
    exit /b
)

:: 변경사항 스테이징
echo 변경사항 스테이징 중...
git add .

:: 커밋 메시지 받기
set /p msg=커밋 메시지를 입력하세요: 
if "%msg%"=="" set msg=default commit

:: 커밋
echo 커밋 중...
git commit -m "%msg%"

:: 푸시
echo GitHub로 푸시 중...
git push origin main

:: 완료 메시지
echo 백업 완료! GitHub를 확인하세요.
pause
