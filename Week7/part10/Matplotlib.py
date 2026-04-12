from turtle import pd

import matplotlib.pyplot as plt

def plot_department_ages(conn):
    df = pd.read_sql("SELECT * FROM employees", conn)
    
    if df.empty:
        print("Không có dữ liệu để vẽ biểu đồ.")
        return
    avg_age_df = df.groupby('department')['age'].mean()
    
    avg_age_df.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Tuổi trung bình của nhân viên theo phòng ban')
    plt.xlabel('Phòng ban')
    plt.ylabel('Tuổi trung bình')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_department_ages(conn)
