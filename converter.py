from string import digits, ascii_uppercase


class Converter:
    """
    Konversi sebuah angka dari satu basis ke basis lainnya
    """

    list_karakter = digits + ascii_uppercase

    def __init__(
        self, angka_original: str, basis_original: str, basis_tujuan: str
    ) -> None:
        self.angka_original = tuple(angka_original.upper())
        self.basis_original = int(basis_original)
        self.basis_tujuan = int(basis_tujuan)
        self.sudah_dieksekusi = False

        self.output = list()

    def alokasi_karakter(self) -> None:
        """
        Alokasi karakter yang dapat digunakan untuk basis original dan tujuan
        """

        self.karakter_basis_original = self.list_karakter[: self.basis_original]
        self.karakter_basis_tujuan = self.list_karakter[: self.basis_tujuan]

    def validasi(self) -> None:
        """
        Cek jika self.basis_original atau self.basis_tujuan diluar jangkauan
        """

        if not (2 < self.basis_original < len(self.list_karakter)):
            raise Exception(
                f"[basis_original] exceed the allowed base (2 - {len(self.list_karakter)})"
            )

        if not (2 < self.basis_tujuan < len(self.list_karakter)):
            raise Exception(
                f"[basis_tujuan] exceed the allowed base (2 - {len(self.list_karakter)})"
            )

    def konversi_ke_desimal(self) -> str:
        """
        Konversi self.angka_original ke desimal
        """

        nilai_desimal = 0
        for i in range(len(self.angka_original)):
            # Diakses dari belakang
            angka = self.angka_original[0 - (i + 1)]

            if angka not in self.karakter_basis_original:
                raise ValueError(
                    "[angka_untuk_dikonversi] does not follow the [basis_original] format"
                )

            nilai_original_dalam_desimal = (
				self.karakter_basis_original.index(angka) 
				* (self.basis_original ** i)
            )

            # DEBUGGING / TESTING
            # print(i, self.karakter_basis_original.index(angka), (self.basis_original ** i), nilai_original_dalam_desimal)

            nilai_desimal += nilai_original_dalam_desimal

        return nilai_desimal

    def kalkulasi_output(self, nilai_desimal: int) -> None:
        """
        Kalkulasi output yang diinginkan
        """

        untuk_dikalkulasi = nilai_desimal

        while untuk_dikalkulasi != 0:
            # DEBUGGING / TESTING
            # print(divmod(untuk_dikalkulasi, self.basis_tujuan))

            untuk_dikalkulasi, sisa_bagi = divmod(untuk_dikalkulasi, self.basis_tujuan)

            self.output.append(self.karakter_basis_tujuan[sisa_bagi])

    def eksekusi(self) -> str:
        """
        Pintu masuk.
        """

        if not self.sudah_dieksekusi:
            self.validasi()
            self.alokasi_karakter()
            self.kalkulasi_output(self.konversi_ke_desimal())
            self.output.reverse()
            self.sudah_dieksekusi = True

        return "".join(self.output)


print(
    """
======================================
        BASE NUMBER CONVERTER
======================================
"""
)
print(f"Urutan karakter (ltr): {Converter.list_karakter}")
print("Input: [angka_untuk_dikonversi] [basis_original] [basis_tujuan]")
print("Contoh: 2748 10 16 -> ABC")

while True:
    user_input = input("\n> ").split()

    angka_original, basis_original, basis_tujuan = user_input

    convert = Converter(
        angka_original=angka_original,
        basis_original=basis_original,
        basis_tujuan=basis_tujuan,
    )

    hasil = convert.eksekusi()

    print(hasil)
