# BLM101_24360859002_AzizMahmutTopalali

# Mantık Hesaplamaları ve Mantık Tablosu Uygulaması

## Öğrenci Bilgileri

* **Ad:** Aziz Mahmut 
* **Soyad:** Topalali
* **Numara:** 24360859002

## Proje Konusu

Python ile Mantık Hesaplamaları ve 3 Değişkenli Mantık Tablosu Oluşturma

## YouTube Linki

Sunum videosu bağlantısı:

[https://youtu.be/sXdi6bdTm5U](https://youtu.be/sXdi6bdTm5U)
---

## Proje Açıklaması

Bu proje, Python programlama dili kullanılarak geliştirilmiş bir mantık işlemleri uygulamasıdır. Program, kullanıcıdan alınan girişlere göre temel mantık operatörleri ile işlem yapabilmekte ve ayrıca üç değişkenli mantık ifadeleri için doğruluk tablosu oluşturabilmektedir. Uygulama, kullanıcıyla etkileşimli çalışan bir konsol programı şeklinde tasarlanmıştır.

Program iki ana bölümden oluşmaktadır:

* Mantık hesaplamaları
* Mantık tablosu oluşturma

---

## Kurulum ve Çalıştırma

Programın çalışması için herhangi bir ek kütüphane kurulmasına gerek yoktur. Python 3 sürümünün yüklü olması yeterlidir.

Program aşağıdaki komut ile çalıştırılabilir:

```bash
python mantik_programi.py
```

---

## Programın Çalışma Mantığı

### Mantık Hesaplaması Modu

Bu modda kullanıcıdan aşağıdaki formatta bir giriş alınır:

```
Deger1 ISLEM Deger2
Örnek: 1 AND 0
```

Kullanıcı tarafından girilen ifade boşluklara göre üç parçaya ayrılır. İlk ve son kısımlar mantık değerleri olarak kabul edilir ve tam sayıya dönüştürülür. Ortadaki kısım ise operatör olarak değerlendirilir. Küçük harfle girilen operatörler otomatik olarak büyük harfe çevrilir.

İşlemler Python’daki bit düzeyinde mantık operatörleri kullanılarak gerçekleştirilir. Hatalı giriş yapılması durumunda kullanıcıya uygun hata mesajı gösterilir.

---

### Mantık Tablosu Modu

Bu modda kullanıcıdan A, B ve C değişkenlerini içeren bir mantık ifadesi girmesi istenir.

Örnek ifade:

```
A AND (B OR C)
```

Kullanıcının girdiği ifade Python sözdizimine uygun hâle getirilir. Ardından 0’dan 7’ye kadar olan tüm sayılar ikilik sisteme çevrilerek A, B ve C değişkenlerinin alabileceği tüm olası durumlar hesaplanır.

Her bir durum için ifade `eval()` fonksiyonu ile çalıştırılır ve elde edilen sonuç 0 veya 1 olacak şekilde tablo hâlinde ekrana yazdırılır.

---

## Ana Menü Yapısı

Program başlangıcında kullanıcıdan isim bilgisi alınır. Daha sonra aşağıdaki menü sürekli olarak ekranda gösterilir:

* 1: Mantık Hesaplamaları
* 2: Mantık Tablosu Oluşturma
* -1: Programdan çıkış

Geçersiz girişlerde kullanıcı uyarılır ve tekrar seçim yapması istenir.

---

## Sonuç

Bu proje, mantık operatörlerinin çalışma prensiplerini öğretmeyi ve Python dilinde kullanıcı etkileşimli bir uygulama geliştirmeyi amaçlamaktadır. Program, temel seviyedeki kullanıcılar için anlaşılır olup eğitim amaçlı kullanıma uygundur.

yeniden düzenleyebilirim.
