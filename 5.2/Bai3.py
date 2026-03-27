
import matplotlib.pyplot as plt
x = list(range(11))  # Tạo dãy số từ 0 đến 10
y = [i**2 for i in x]  # Tính bình phương của x
plt.plot(x, y)  # Vẽ đồ thị
plt.title("Đồ thị y = x^2")  # Thêm tiêu đề
plt.xlabel("x")  # Thêm nhãn trục x
plt.ylabel("y")  # Thêm nhãn trục y
plt.grid()  # Thêm lưới
plt.show()  # Hiển thị đồ thị

