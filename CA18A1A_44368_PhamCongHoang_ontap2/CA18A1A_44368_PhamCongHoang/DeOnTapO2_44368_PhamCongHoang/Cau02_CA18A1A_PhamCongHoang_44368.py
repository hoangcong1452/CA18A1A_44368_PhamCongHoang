"""
De On Tap 02
Date: 30/10/2021
Pham Cong Hoang
"""
def Cau02():
    data = []
    n = 0

    class MatHang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia
    def cau23():
        f = open("CA18A1A_PhamCongHoang_44368_inp.txt", mode="r", encoding="utf-8")
        n = int(f.readline())

        for i in  range(n):
            row_data = f.readline().split("|")
            Thiet_Bi = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(Thiet_Bi) #dua du lieu vao data cac object

            # dong file
        f.close()
        print("=="*10)
        print("Hoan thanh viec nhap du lieu tu file: CA18A1A_PhamCongHoang_44368_inp.txt")

    def cau24():
        print("=="*20)
        if len(data) == 0:
            print("Ban can chon nhap thong tin ve mat hang tu file")
        else:
            print("\nIn thong tin cac mat hang:\n")
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                        .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)

    def cau25():
        if len(data) == 0:
           print("Ban can chon nhap thong tin ve mat hang")
        else:
            # ghi du lieu
            f = open("CA18A1A_PhamCongHoang_44368_out.txt", mode="w", encoding="utf-8")

            f.write(str(len(data)) + "\n")

            for i in data:
                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                    + "|" + str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                f.write(s)

            f.close()
        print("Hoan thanh ghi ra file: CA18A1A_PhamCongHoang_44368_out.txt")
        print("++"*20)

    def cau26():
        """Hien thi mat hang co don gia cao nhat"""
        print("==== Mat Hang Dat Nhat ====")
        matHangDatNhat = data[0]
        for i in data:
            if i.don_gia > matHangDatNhat.don_gia:
                matHangDatNhat = i
        matHangDatNhat_str = matHangDatNhat.ma_mat_hang + "|" + matHangDatNhat.ten_mat_hang + "|" + str(matHangDatNhat.so_luong) \
                    + "|" + str(matHangDatNhat.don_gia) + "|" + str(matHangDatNhat.thanh_tien)
        print(matHangDatNhat_str)
        print("=="*15)
    while True:
        print("---MENU---")
        print("1. Nhap du lieu tu file.")
        print("2. In du lieu ra mang hinh.")
        print("3. In mat hang don gia cao nhat.")
        print("4. Ghi thong tin vao file.")
        cv = input("Ban chon cong viec, bam Q de thoat: ")
        if cv == "1":
            cau23()
        elif cv == "2":
            cau24()
        elif cv == "3":
            cau26()
        elif cv == "4":
            cau25()
        elif cv.upper() == "Q":
            break


if __name__ == '__main__':
    Cau02()








