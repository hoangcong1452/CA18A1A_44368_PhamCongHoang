"""
De thi 02
date:29/10/2021
Pham Cong Hoang

"""
def Cau2():
    data = []  # list chua cac doi tuong
    n = 0  # số lượng mặt hàng

    class Mathang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():
        # mở file
        f = open("CA18A1A_PhamCongHoang_44368_inp.txt", mode="r", encoding="utf-8")
        # đọc dữ liêu và đưa vào class
        n = int(f.readline())  # n la so luong mat hang

        for i in range(n):
            row_data = f.readline().split("|")
            mat_hang = Mathang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))

            data.append(mat_hang)  # dua du lieu vao data cac object

            # dong file
        f.close()
        print("==" * 20)
        print("Hoàn thành việc nhập dữ liệu từ file:CA18A1A_PhamCongHoang_44368_inp.txt ")

    def cv24():
        print("==" * 20)
        if len(data) == 0:
            print("Bạn cần nhập thông tin về mặt hàng")
        else:
            # đã có thông tin ,xử lí
            print("\nIn thông tin các mặt hàng:\n")
            for i in data:
                print("{:<5} {:<15} {:<5} {:>10} {:>10}" \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)

    def cv25():
        """"Hiển thị thông tin của mặt hàng có Đơn giá cao nhất"""
        print("=== Mặt hàng đơn giá cao nhất ===")
        # tìm mặt hàng có đơn giá cao nhất
        MatHangDatNhat = data[0]
        for i in data:
            if i.don_gia > MatHangDatNhat.don_gia:
                MatHangDatNhat = i
        # hiển thị ra
        MatHangDatNhat_str = MatHangDatNhat.ma_mat_hang + "|" + MatHangDatNhat.ten_mat_hang + "|" + str(MatHangDatNhat.so_luong) \
            + "|" + str(MatHangDatNhat.don_gia) + "|" + str(MatHangDatNhat.thanh_tien)
        print(MatHangDatNhat_str)
        print("==" * 16)


    def cv26():
        print("=="*20)
        if len(data) == 0:
            print("Bạn cần chọn nhập thông tin về mặt hàng:")
        else:
            # ghi dữ liệu
            f = open("CA18A1A_PhamCongHoang_44368_out.txt", mode="w", encoding="utf-8")
            f.write(str(len(data)) + "\n")

            for i in data:

                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                        + "|" + str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                f.write(s)
            f.close()
        print("Hoàn thành ghi ra file: CA18A1A_PhamCongHoang_44368_out.txt")
        print("==" * 20)

    while True:
        print("__MENU__")
        print("1 Nhập dữ liệu từ file.")
        print("2 In dữ liệu ra màn hình.")
        print("3 In mặt hàng đơn giá cao nhất.")
        print("4 Ghi thông tin vào file.")
        cv = input("Bạn chọn công việc, bấm O để thoát: ")
        if cv == "1":
            print("call cv23")
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "3":
            cv25()
        elif cv == "4":
            cv26()
        elif cv.upper() == "O":
            break


if __name__ == '__main__':
    Cau2()