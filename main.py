def hitung_bmi(berat, tinggi_cm):
    tinggi_m = tinggi_cm / 100
    bmi = berat / (tinggi_m ** 2)
    return bmi


def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main():
    print("=== Kalkulator BMI ===")
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

    bmi = hitung_bmi(berat, tinggi_cm)
    kategori = kategori_bmi(bmi)

    print(f"\nBMI kamu: {bmi:.2f}")
    print(f"Kategori: {kategori}")


if __name__ == "__main__":
    main()