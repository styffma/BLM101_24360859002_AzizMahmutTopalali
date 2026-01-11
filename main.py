def mantik_hesaplamasi():
    print("\n--- Mantık Hesaplaması Modu ---")
    print("Format: Deger1 ISLEM Deger2 (Örn: 1 AND 0)")
    
    girdi = input("İşlemi giriniz: ")
    
    try:
        # Girdiyi parçalara ayırıyoruz ("1", "AND", "0")
        parcalar = girdi.split()
        
        # Parca uzunlugu kontrolu
        if len(parcalar) != 3:
            print("Hata: Lütfen aralarda boşluk bırakarak 3 parça girin.")
            return

        val1 = int(parcalar[0])
        operator = parcalar[1].upper() # Küçük harf girilirse büyütür
        val2 = int(parcalar[2])
        
        sonuc = None

        if operator == "AND":
            sonuc = val1 & val2
        elif operator == "OR":
            sonuc = val1 | val2
        elif operator == "XOR":
            sonuc = val1 ^ val2
        else:
            print("Hata: Geçersiz operatör! (Sadece AND, OR, XOR)")
            return
            
        print(f"Sonuç: {sonuc}")

    except ValueError:
        print("Hata: Lütfen değer kısımlarına sadece sayı (0 veya 1) girin.")        

def mantik_tablosu():
    print("\n--- Mantık Tablosu Modu (3 Değişkenli) ---")
    print("Lütfen A, B ve C değişkenlerini kullanarak ifadenizi yazın.")
    print("Desteklenenler: AND, OR, XOR")
    print("Örnek: A AND (B OR C)")
    
    ifade_girilen = input("\nDenklemi giriniz: ").upper()
    
    python_ifadesi = ifade_girilen.replace("AND", "and").replace("OR", "or").replace("XOR", "^").replace("NOT", "not")
    
    print("\n" + "-" * 25)
    print("A  B  C  |  SONUÇ")
    print("-" * 25)
    
    # 0'dan 7'ye kadar (binary 000 -> 111) tüm olasılıkları deniyoruz
    for i in range(8):
        
        c = i % 2         
        b = (i // 2) % 2   
        a = (i // 4) % 2   
    
        hesaplanacak = python_ifadesi.replace("A", str(a)).replace("B", str(b)).replace("C", str(c))
        
        try:
            # eval() stringi kod gibi çalıştırır
            ham_sonuc = eval(hesaplanacak)

            sonuc = 1 if ham_sonuc else 0
            
            print(f"{a}  {b}  {c}  |    {sonuc}")
            
        except Exception as hata:
            print(f"Hata oluştu! İfadeyi kontrol edin. Hata detayı: {hata}")
            return

    print("-" * 25)


if __name__ == "__main__":
    isim = input("Merhaba! Lütfen isminizi girer misiniz: ") # İsim alma kısmı bilerek döngü dışına bırakıldı
    print(f"\nHoşgeldin {isim}!")

    while True:
        # Bir seçim yaptıktan sonra tekrar tekra seçin yapabilmek için sonsuz döngü
        try:
            secim = int(input(f"\nİşlemler:\n1) Mantık Hesaplamaları\n2) Mantık Tablosu Çıkarma\n\nLütfen seçiminizi giriniz (çıkmak için '-1'): "))
        except ValueError:
            print("Lütfen sayı giriniz!")
            continue

        if (secim == -1):
            print("Programdan çıkılıyor!")
            break
        elif (secim == 1):
            mantik_hesaplamasi()
        elif (secim == 2):
            print("Mantık Tablosu seçildi")
            mantik_tablosu()
        else:
            print("Yanlış bir seçim yaptınız. Lütfen tekrar deneyin.")
    
