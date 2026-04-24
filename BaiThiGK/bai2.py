import string

def tachTu(vanBan):

    dauTiengViet = "…“”‘’"

    for dau in string.punctuation + dauTiengViet:
        vanBan = vanBan.replace(dau, "")

    danhSachTu = vanBan.lower().split()

    return danhSachTu


def phanTichVanBan():

    vanBan = input("Nhập đoạn văn (2-3 câu): ")

    danhSachTu = tachTu(vanBan)

    if not danhSachTu:
        print("Lỗi: Đoạn văn không được rỗng")
        return

    tongSoTu = len(danhSachTu)

    demTu = {}

    for tu in danhSachTu:
        demTu[tu] = demTu.get(tu, 0) + 1

    maxLan = max(demTu.values())

    tuNhieuNhat = []

    for tu, soLan in demTu.items():
        if soLan == maxLan:
            tuNhieuNhat.append(tu)

    print("Tổng số từ:", tongSoTu)

    if maxLan == 1:
        print("Tất cả các từ đều xuất hiện 1 lần")

    elif len(tuNhieuNhat) == 1:
        print(
            f"Từ xuất hiện nhiều nhất: {tuNhieuNhat[0]} ({maxLan} lần)"
        )

    else:
        print(f"Các từ xuất hiện nhiều nhất ({maxLan} lần):")

        for tu in tuNhieuNhat:
            print(f"- {tu}: {maxLan} lần")


phanTichVanBan()
