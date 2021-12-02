from converter import (
    Converter,
    InvalidOriginalBase,
    InvalidTargetBase,
    CharacterOutOfRange,
)

print("======================================")
print("\t\tBASE NUMBER CONVERTER")
print("======================================")

print(f"Urutan karakter (ltr): {Converter.list_karakter}")
print("Input: [angka_untuk_dikonversi] [basis_original] [basis_tujuan]")
print("Contoh: 2748 10 16 -> ABC")


while True:
    user_input = input("\n> ").split()

    try:
        angka_original, basis_original, basis_tujuan = user_input
    except ValueError:
        print("Masukkan input dengan benar")
        continue

    try:
        convert = Converter(
            angka_original=angka_original,
            basis_original=basis_original,
            basis_tujuan=basis_tujuan,
        )
        hasil = convert.eksekusi()
    except ValueError:
        print("Masukkan input dengan benar")
        continue

    except InvalidOriginalBase:
        print(f"Basis original ({convert.basis_original}) diluar jangkauan (2-36)")
        continue

    except InvalidTargetBase:
        print(f"Basis tujuan ({convert.basis_tujuan}) diluar jangkauan (2-36)")
        continue

    except CharacterOutOfRange:
        print(
            f"Angka original ({''.join(convert.angka_original)}) tidak mengikuti aturan basis original ({convert.basis_original})"
        )
        continue

    convert.log()

    print(hasil)
