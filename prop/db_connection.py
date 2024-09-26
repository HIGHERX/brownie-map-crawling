
import psycopg2
from psycopg2 import sql, pool

from properties import (
	db_host, db_name, db_user, db_password
)

# 커넥션 풀 생성
db_pool = None

def init_db_pool():
    global db_pool
    db_pool = psycopg2.pool.SimpleConnectionPool(
        1, 10,  # 최소, 최대 연결 수
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port='5432'
    )

def fetch_data(query, data):
    """데이터를 선택하는 함수"""
    try:
        # 커넥션 풀에서 연결 가져오기
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL(query), data)
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print(f"SELECT 오류: {e}", flush=True)
    finally:
        # 커넥션 반납
        if conn:
            db_pool.putconn(conn)

def insert_data(query, data):
    """데이터를 삽입하는 함수"""
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute(sql.SQL(query), data)
            conn.commit()
    except Exception as e:
        print(f"INSERT 오류: {e}", flush=True)
        if conn:
            conn.rollback()
    finally:
        if conn:
            db_pool.putconn(conn)

def close_db_pool():
    """커넥션 풀 닫기"""
    if db_pool:
        db_pool.closeall()

