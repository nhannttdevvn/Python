import matplotlib.pyplot as plt

def quanLyKho():

    kho = {
        'Balo': 150,
        'Túi xách': 80,
        'Vali': 120
    }

    print("Danh sách ban đầu:")

    for ten, soLuong in kho.items():
        print(f"{ten}: {soLuong}")

    while True:
        try:
            soLuongViDa = int(input("Nhập số lượng Ví da: "))

            if soLuongViDa < 0:
                print("Lỗi: Số lượng phải >= 0")
                continue

            break

        except ValueError:
            print("Lỗi: Phải nhập số")

    kho['Ví da'] = soLuongViDa

    if kho['Balo'] >= 30:
        kho['Balo'] -= 30
    else:
        print("Không đủ Balo để xuất kho")

    print("\nDanh sách sau cập nhật:")

    for ten, soLuong in kho.items():

        if ten == 'Balo':
            print(f"{ten}: {soLuong} (xuất kho 30)")

        elif ten == 'Ví da':
            print(f"{ten}: {soLuong} (nhập mới)")

        else:
            print(f"{ten}: {soLuong}")

    tongKho = sum(kho.values())


    labels = list(kho.keys())
    sizes = list(kho.values())

    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%'
    )

    plt.title("Tỷ trọng hàng trong kho")

    plt.show()

quanLyKho()
