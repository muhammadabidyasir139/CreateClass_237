class PersegiPanjang:
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    def keliling (self):
        return 2 * (self.panjang + self.lebar)
    def luas (self):
        return self.panjang * self.lebar
    def __str__ (self):
        return f"panjang persegi dengan panjang ({self.panjang}) dan lebar ({self.lebar}) memiliki keliling ({self.keliling()}) dan luas ({self.luas()})"
    def main():
        try:
            panjang = int(input("masukkan panjang: "))
            lebar = int(input("masukkan lebar: "))
            pp = PersegiPanjang(panjang, lebar)
            pilihan = input("apakah anda ingin menghitung 'keliling' atau 'luas'").strip().lower()
            if pilihan == "keliling":
                print(f"keliling dengan panjang ({pp.panjang}) dan lebar ({pp.lebar} adalah ({pp.keliling()})")
            elif pilihan == "luas":
                print(f"luas dengan panjang ({pp.panjang}) dan lebar ({pp.lebar}) adalah ({pp.luas()})")
            else:
                print("masukkan pilihan yang benar")
        except ValueError:
            print("masukkan angka")

if __name__ == "__main__":
    PersegiPanjang.main()