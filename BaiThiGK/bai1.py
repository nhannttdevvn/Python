def todoList():

    danhSach = []

    print("Nhập các công việc (nhập 'x' để dừng):")

    while True:

        congViec = input("Nhập công việc: ")

        congViec = congViec.strip()

        if congViec.lower() == 'x':
            break

        if congViec == "":
            print("Công việc không được rỗng")
            continue

        if congViec in danhSach:
            print("Công việc đã tồn tại")
            continue

        danhSach.append(congViec)

        print(f"Đã thêm công việc số {len(danhSach)}")

    if not danhSach:
        print("Danh sách rỗng, không có công việc để lưu")
        return

    print("\nDanh sách công việc:")

    print(f"Tổng số công việc: {len(danhSach)}")

    with open("todo_list.txt", "w", encoding="utf-8") as f:

        f.write("DANH SÁCH CÔNG VIỆC\n\n")

        for i, cv in enumerate(danhSach, start=1):

            dong = f"{i}. {cv}"

            print(dong)

            f.write(dong + "\n")

        f.write("\n--- Hết danh sách ---")

todoList()
