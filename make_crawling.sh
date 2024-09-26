#!/bin/bash

# 현재 날짜+시간
timestamp=$(date +"%Y%m%d%H%M%S")

# 로그 파일 경로
LOG_FILE="./logs/crawling_log_$1_$timestamp.log"

# batch pid 파일 경로
PID_FILE="./logs/crawling_batch_pid_$1_$timestamp.txt"

# 파이썬 스크립트 경로
PYTHON_SCRIPT="crawling_NaverMap_to_DB.py"


# 날짜 형식 체크 함수
check_date() {
    if ! date -j -f "%Y-%m-%d" "$1" "+%Y-%m-%d" &> /dev/null; then
        return 1  # 유효하지 않으면 1 반환
    fi

    # 월과 일이 두 자리인지 체크
    if [[ ! "$1" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        return 1  # 형식이 맞지 않으면 1 반환
    fi

    return 0  # 유효하면 0 반환
}

# 인자 개수 확인
if [ $# -eq 0 ]; then
    echo "오류: argument가 필요합니다. (crawling date)"
    echo "사용법: $0 <날짜 (YYYY-MM-DD 형식)>"
    exit 1  # 에러 코드 1로 종료
fi

# 날짜 형식 확인
if ! check_date "$1"; then
    echo "오류: '$1'은 유효한 날짜 형식이 아닙니다."
    echo "사용법: $0 <날짜 (YYYY-MM-DD 형식)>"
    exit 1
fi

nohup python3 $PYTHON_SCRIPT -crawldate $1 > "$LOG_FILE" 2>&1 & # 모든 출력과 오류를 로그 파일에 추가

# PID를 저장하여 나중에 확인할 수 있게 함
echo $! > $PID_FILE

echo ""
echo "-------------------------------------------------------------------------"
echo ""
echo " Crawling Batch 시작했습니다."
echo ""
echo "     * Process ID :  $!"
echo ""
echo "        - batch 중단하려면,  'kill -9 $!' 실행해주세요."
echo ""
echo "            -> pid 저장 파일 :  $PID_FILE"
echo ""
echo "        - batch 완료는 별도 알림이 없습니다."
echo ""
echo "-------------------------------------------------------------------------"
echo ""
echo " Crawling 로그 파일 :  $LOG_FILE"
echo ""
echo "     * 실시간 로그 현황은 아래 명령어로 확인하세요."
echo ""
echo "        tail -100f $LOG_FILE"
echo ""
echo "-------------------------------------------------------------------------"
echo ""

exit 0
