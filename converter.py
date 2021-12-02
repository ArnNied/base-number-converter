import json
from string import ascii_uppercase, digits


class InvalidOriginalBase(Exception):
    pass


class InvalidTargetBase(Exception):
    pass


class CharacterOutOfRange(Exception):
    pass


class IsNotConverted(Exception):
    pass


class Converter:
    """
    Konversi sebuah angka dari satu basis ke basis lainnya
    """

    list_karakter = digits + ascii_uppercase

    def __init__(
        self, angka_original: str, basis_original: str, basis_tujuan: str
    ) -> "Converter":
        self.angka_original = tuple(angka_original.upper())
        self.basis_original = int(basis_original)
        self.basis_tujuan = int(basis_tujuan)
        self.tereksekusi = False

        self.output = list()

    def validasi(self) -> None:
        """
        Cek jika self.basis_original atau self.basis_tujuan diluar jangkauan
        """

        if not (2 <= self.basis_original <= len(self.list_karakter)):
            raise InvalidOriginalBase(
                f"Basis original ({self.basis_original}) diluar jangkauan (2-{len(self.list_karakter)})"
            )

        if not (2 <= self.basis_tujuan <= len(self.list_karakter)):
            raise InvalidTargetBase(
                f"Basis tujuan ({self.basis_original}) diluar jangkauan (2-{len(self.list_karakter)})"
            )

    def alokasi_karakter(self) -> None:
        """
        Alokasi karakter yang dapat digunakan untuk basis original dan tujuan
        """

        self.karakter_basis_original = self.list_karakter[: self.basis_original]
        self.karakter_basis_tujuan = self.list_karakter[: self.basis_tujuan]

    def konversi_ke_desimal(self) -> str:
        """
        Konversi self.angka_original ke desimal
        """

        nilai_desimal = 0
        for i in range(len(self.angka_original)):
            # Diakses dari belakang
            angka = self.angka_original[0 - (i + 1)]

            if angka not in self.karakter_basis_original:
                raise CharacterOutOfRange(
                    f"Angka original ({''.join(self.angka_original)}) tidak mengikuti aturan basis original ({self.basis_original})"
                )

            nilai_original_dalam_desimal = (
                self.karakter_basis_original.index(angka) * self.basis_original ** i
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

        if not self.tereksekusi:
            self.validasi()
            self.alokasi_karakter()
            self.kalkulasi_output(self.konversi_ke_desimal())
            self.output.reverse()
            self.tereksekusi = True

        return "".join(self.output)

    def log(self, file_path: str = "./log", force: bool = False):
        """
        Mencatat semua atribut ke dalam sebuah file json
        """

        if self.tereksekusi or force:
            with open(f"{file_path}.json", "r+") as file:
                data = json.load(file)

                try:
                    index = int(list(data.keys())[-1]) + 1
                except IndexError:
                    index = 1

                data.update(
                    {
                        index: {
                            "angka_original": "".join(self.angka_original),
                            "basis_original": self.basis_original,
                            "basis_tujuan": self.basis_tujuan,
                            "hasil": "".join(self.output),
                        }
                    }
                )
                file.seek(0)
                json.dump(data, file, indent=2)
        else:
            raise IsNotConverted(
                "Data belum dikonversi, tambahkan `force=True` jika ingin tetap melanjutkan"
            )
