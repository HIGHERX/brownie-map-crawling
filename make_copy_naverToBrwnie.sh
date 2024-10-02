#!/bin/bash

# 파이썬 스크립트 경로
PYTHON_SCRIPT="copy_naver_to_brwnie.py"


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
if [ $# -ne 2 ]; then
    echo "오류: 2개의 argument가 필요합니다. (crawling date, db)"
    echo "사용법: $0 <날짜 (YYYY-MM-DD 형식)> <dev 또는 prod>"
    exit 1  # 에러 코드 1로 종료
fi

# 날짜 형식 확인
if ! check_date "$1"; then
    echo "오류: 1번째 argument '$1'은 유효한 날짜 형식이 아닙니다."
    echo "사용법: $0 <날짜 (YYYY-MM-DD 형식)> <dev 또는 prod>"
    exit 1
fi

# DB system 확인
if [[ "$2" != "dev" && "$2" != "prod" ]]; then
    echo "오류: 2번째 argument '$2'는 dev 또는 prod 만 가능합니다."
    echo "사용법: $0 <날짜 (YYYY-MM-DD 형식)> <dev 또는 prod>"
    exit 1
fi

python3 $PYTHON_SCRIPT -crawldate $1 -db $2

exit 0
