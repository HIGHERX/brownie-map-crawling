#!/bin/bash

# 파이썬 스크립트 경로
PYTHON_SCRIPT="apply_wkdk_to_brwnie.py"


# 인자 개수 확인
if [ $# -ne 1 ]; then
    echo "오류: 1개의 argument가 필요합니다. (db)"
    echo "사용법: $0 <dev 또는 prod>"
    exit 1  # 에러 코드 1로 종료
fi

# DB system 확인
if [[ "$1" != "dev" && "$1" != "prod" ]]; then
    echo "오류: 1번째 argument '$1'는 dev 또는 prod 만 가능합니다."
    echo "사용법: $0 <dev 또는 prod>"
    exit 1
fi

python3 $PYTHON_SCRIPT -db $1

exit 0
