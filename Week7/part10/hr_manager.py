import mysql.connector
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning)

try:
    conn = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='', 
        database='company_db'
    )
    cursor = conn.cursor()
    print("Kết nối MySQL thành công!\n")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            department VARCHAR(50)
        )
    """)
    conn.commit()

    print("--- NHẬP LIỆU NHÂN VIÊN ---")
    while True:
        name = input("Nhập tên nhân viên (gõ 'q' để thoát): ")
        if name.lower() == 'q':
            break
        
        try:
            age = int(input("Nhập tuổi: "))
            department = input("Nhập phòng ban: ")
            
            sql = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, age, department))
            conn.commit()
            print(f"-> Đã thêm '{name}' vào database!\n")
        except ValueError:
            print("Lỗi: Tuổi phải là một số nguyên. Vui lòng nhập lại.\n")

    print("\n--- DANH SÁCH TOÀN BỘ NHÂN VIÊN ---")
    df = pd.read_sql("SELECT * FROM employees", conn)
    print(df)

    print("\n--- THỐNG KÊ THEO PHÒNG BAN ---")
    if not df.empty:
        stats = df.groupby('department').agg(
            count=('id', 'count'),
            avg_age=('age', 'mean'),
            max_age=('age', 'max')
        ).round(1) 
        print(stats)
    else:
        print("Chưa có dữ liệu để thống kê.")

except mysql.connector.Error as err:
    print(f"Lỗi cơ sở dữ liệu: {err}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\nĐã đóng kết nối database.")

# Pagination
def search_employee(conn, keyword):
    sql = "SELECT * FROM employees WHERE name LIKE %s"
    df = pd.read_sql(sql, conn, params=(f'%{keyword}%',))
    return df

def get_page(conn, page, size=5):   
    offset = (page - 1) * size
    sql = "SELECT * FROM employees LIMIT %s OFFSET %s"
    df = pd.read_sql(sql, conn, params=(size, offset))
    return df