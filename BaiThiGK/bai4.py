import random
import time

def miniHangman():

    danhSachTu = ["python", "apple", "river"]

    tuBiMat = random.choice(danhSachTu)

    hienThi = ["_"] * len(tuBiMat)

    soLanSai = 5

    chuDaDoan = []

    startTime = time.time()

    print("Từ cần đoán:")
    print(" ".join(hienThi))

    while soLanSai > 0 and "_" in hienThi:

        print("Đã đoán:", ", ".join(chuDaDoan))

        chu = input("Nhập chữ cái: ").lower()

        if len(chu) != 1 or not chu.isalpha():
            print("Vui lòng nhập đúng 1 chữ cái")
            continue

        if chu in chuDaDoan:
            print("Bạn đã đoán chữ này rồi")
            continue

        chuDaDoan.append(chu)

        if chu in tuBiMat:

            for i in range(len(tuBiMat)):
                if tuBiMat[i] == chu:
                    hienThi[i] = chu

        else:
            soLanSai -= 1
            print("Sai! Còn", soLanSai, "lượt")

        print(" ".join(hienThi))

    endTime = time.time()

    thoiGian = round(endTime - startTime, 2)

    with open("hangman_result.txt", "w", encoding="utf-8") as f:

        if "_" not in hienThi:
            print("Bạn thắng!")

            f.write(
                f"Thắng | Từ: {tuBiMat} | Thời gian: {thoiGian} giây"
            )

        else:
            print("Bạn thua! Từ là:", tuBiMat)

            f.write(
                f"Thua | Từ: {tuBiMat} | Lượt còn: {soLanSai}"
            )

miniHangman()
