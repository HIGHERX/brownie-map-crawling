
import psycopg2
from psycopg2 import sql, pool

from properties import (
    # brwnie
	dev_brwnie_db_host, dev_brwnie_db_name, dev_brwnie_db_user, dev_brwnie_db_password
	, prod_brwnie_db_host, prod_brwnie_db_name, prod_brwnie_db_user, prod_brwnie_db_password
    # wkdk
	, dev_wkdk_db_host, dev_wkdk_db_name, dev_wkdk_db_user, dev_wkdk_db_password
	, prod_wkdk_db_host, prod_wkdk_db_name, prod_wkdk_db_user, prod_wkdk_db_password
)

# 커넥션 풀 생성
db_pool = None

def init_db_pool(db, system):
    global db_pool

    if db == "dev" and system == "brwnie" :
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,  # 최소, 최대 연결 수
            dbname = dev_brwnie_db_name,
            user = dev_brwnie_db_user,
            password = dev_brwnie_db_password,
            host = dev_brwnie_db_host,
            port = '5432'
        )
    elif db == "prod" and system == "brwnie":
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,  # 최소, 최대 연결 수
            dbname = prod_brwnie_db_name,
            user = prod_brwnie_db_user,
            password = prod_brwnie_db_password,
            host = prod_brwnie_db_host,
            port = '5432'
        )
    elif db == "dev" and system == "wkdk" :
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,  # 최소, 최대 연결 수
            dbname = dev_wkdk_db_name,
            user = dev_wkdk_db_user,
            password = dev_wkdk_db_password,
            host = dev_wkdk_db_host,
            port = '5432'
        )
    elif db == "prod" and system == "wkdk":
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,  # 최소, 최대 연결 수
            dbname = prod_wkdk_db_name,
            user = prod_wkdk_db_user,
            password = prod_wkdk_db_password,
            host = prod_wkdk_db_host,
            port = '5432'
        )

    if db_pool is None:
        print("\n(DB connection 오류)  DB 연결할 수 없어 종료합니다.  (db=", db, ", system=", system, ")\n", flush=True)
        exit()
    else:
        print("\n# DB connected!  (db=", db, ", system=", system, ")\n", flush=True)

def fetch_data(query, data):
    """데이터를 선택하는 함수"""
    try:
        # 커넥션 풀에서 연결 가져오기
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            if data is not None:
                cursor.execute(sql.SQL(query), data)
            else:
                cursor.execute(sql.SQL(query))
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
            if data is not None:
                cursor.execute(sql.SQL(query), data)
            else:
                cursor.execute(sql.SQL(query))
            conn.commit()
    except Exception as e:
        print(f"INSERT 오류: {e}", flush=True)
        if conn:
            conn.rollback()
    finally:
        if conn:
            db_pool.putconn(conn)

def update_data(query, data):
    """데이터를 삭제하는 함수"""
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            if data is not None:
                cursor.execute(sql.SQL(query), data)
            else:
                cursor.execute(sql.SQL(query))
            conn.commit()
    except Exception as e:
        print(f"UPDATE 오류: {e}", flush=True)
        if conn:
            conn.rollback()
    finally:
        if conn:
            db_pool.putconn(conn)

def delete_data(query, data):
    """데이터를 삭제하는 함수"""
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            if data is not None:
                cursor.execute(sql.SQL(query), data)
            else:
                cursor.execute(sql.SQL(query))
            conn.commit()
    except Exception as e:
        print(f"DELETE 오류: {e}", flush=True)
        if conn:
            conn.rollback()
    finally:
        if conn:
            db_pool.putconn(conn)

def create_table(query):
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(f"테이블 생성 오류: {e}", flush=True)
    finally:
        if conn:
            db_pool.putconn(conn)

def drop_table(query):
    try:
        conn = db_pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        print(f"테이블 삭제 오류: {e}", flush=True)
    finally:
        if conn:
            db_pool.putconn(conn)

def close_db_pool(db, system):
    """커넥션 풀 닫기"""
    if db_pool:
        db_pool.closeall()
        print("\n\n# DB closed!  (db=", db, ", system=", system, ")\n", flush=True)
    else:
        print("\n\n(DB close 오류)  커넥션 풀이 없습니다.  (db=", db, ", system=", system, ")\n", flush=True)

