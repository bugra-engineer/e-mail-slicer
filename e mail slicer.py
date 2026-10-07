import re

def email_ayir(email):
    kalip = r"^[\w\.\-+]+@[\w\-]+(\.[\w\-]+)+$"
    if not re.match(kalip, email):
        return None
    kullanici, alan_adi = email.split("@")
    return kullanici, alan_adi

def main():
    print("✂️ E-POSTA DİLİMLEYİCİ")
    email = input("E-posta adresi: ").strip()
    sonuc = email_ayir(email)

    if sonuc is None:
        print("❌ Geçersiz e-posta adresi.")
        return

    kullanici, alan_adi = sonuc
    print(f"Kullanıcı adı : {kullanici}")
    print(f"Alan adı      : {alan_adi}")

if __name__ == "__main__":
    main()