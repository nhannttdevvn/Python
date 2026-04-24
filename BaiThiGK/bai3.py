def tinhBMI():

    # Nhập cân nặng
    while True:
        try:
            canNang = float(input("Nhập cân nặng (kg): "))

            if not (2 <= canNang <= 300):
                print("Lỗi: Cân nặng phải từ 2 đến 300 kg")
                continue

            break

        except ValueError:
            print("Lỗi: Bạn phải nhập số!")

    # Nhập chiều cao
    while True:
        try:
            chieuCao = float(input("Nhập chiều cao (m): "))

            if not (0.5 <= chieuCao <= 2.5):
                print("Lỗi: Chiều cao phải từ 0.5 đến 2.5 m")
                continue

            break

        except ValueError:
            print("Lỗi: Bạn phải nhập số!")

    bmi = canNang / (chieuCao ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Phân loại: Gầy")

    elif bmi < 25:
        print("Phân loại: Bình thường")

    else:
        print("Phân loại: Thừa cân")


tinhBMI()
