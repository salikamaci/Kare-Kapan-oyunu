EKSI_BIR = -1
SIFIR = 0
BIR = 1
IKI = 2
UC = 3
DORT = 4
A_ASCII_KODU = 65   #65 A karakterinin ASCII kodudur.
BEYAZ = "B"
SIYAH = "S"
EVET = "E"
EVET_HAYIR = "EH"


# Belirlenen aralıkta sayı almaya yarar. Belirlediğimiz aralık: [3, 7]
# Geriye hamle sayısını, konumları, satırı, sütunu, beyaz ve siyah taş sayısını döndürür.
def satir_sayisi_al(aralik):
    hata = True
    while hata:
        try:
            satir_sayi = int(input("Satır sayısını giriniz: "))
            while satir_sayi not in aralik:
                print("Girdiğiniz değer aralıkta bulunmamaktadır. Tekrar giriniz")
        except ValueError:
            print("Sadece tam sayı girmeniz gerekmektedir.")
        else:
            sutun_sayi = satir_sayi + BIR
            beyaz_tas = int(satir_sayi * sutun_sayi / IKI)
            siyah_tas = int(satir_sayi * sutun_sayi / IKI)
            hamle_sayisi = beyaz_tas + siyah_tas
            konumlar = []
            for i in range(satir_sayi):
                sutun_liste = []
                for j in range(sutun_sayi):
                    sutun_liste.append(" ")
                konumlar.append(sutun_liste)
            oyun_tahtasi(konumlar, satir_sayi, sutun_sayi)
            hata = False
    return hamle_sayisi, konumlar, satir_sayi, sutun_sayi, beyaz_tas, siyah_tas


# Oyun tahtasının en başındaki harfleri yazdırır. Sütun sayısı kadar harf yazdırır, bunun için ASCII'den yararlanır.
# chr fonksiyonu bir tamsayıdan karakter döndürür.
def harfleri_yazdir(sutun):
    print(" ", end=" ")
    for sayi in range(sutun):
        print(chr(A_ASCII_KODU + sayi), end="   ")
    print()


# Oyun tahtasını yazdırmaya yarar. Konumları, satır ve sütun sayısını parametre olarak alır.
def oyun_tahtasi(konumlar, satir, sutun):
    harfleri_yazdir(sutun)
    satir = satir - BIR
    sutun = sutun - BIR
    for satir_index in range(satir):
        print(satir_index + BIR, end=" ")
        for sutun_index in range(sutun):
            print(konumlar[satir_index][sutun_index], end="---")
        print(konumlar[satir_index][sutun], end=" ")
        print(satir_index + BIR)

        print("  ", end="")
        for _ in range(sutun + BIR):
            print("|", end="   ")
        print()
    print(satir + BIR, end=" ")
    for sutun_index in range(sutun):
        print(konumlar[satir][sutun_index], end="---")
    print(konumlar[satir][sutun], end=" ")
    print(satir + BIR)
    harfleri_yazdir(sutun + BIR)


# Yerleştirmek istenilen taşın değerini alarak onu oyun tahtasına koymaya yarar.
def tas_yerlestir(renk, konumlar):
    yanlis_deger = True
    while yanlis_deger:
        try:
            tas_konumu = input("Koymak istediğiniz taşın değerini giriniz: ").upper()
            satir_index = int(tas_konumu[0]) - BIR
            sutun_index = ord(tas_konumu[1]) - A_ASCII_KODU
            dolu_degil = dolu_mu(konumlar, satir_index, sutun_index)
            if not dolu_degil:
                print("Verdiğiniz konumda zaten bir taş bulunmaktadır. Lütfen tekrar değer giriniz.")
            else:
                konumlar[satir_index][sutun_index] = renk
                yanlis_deger = False
        except ValueError:
            print("Yanlış değer girdiniz, ilk değeriniz sayı olmak zorunda.")
        except IndexError:
            print("Girdiğiniz değer oyun tahtasında bulunmamaktadır. Lütfen tekrar giriniz.")


# Hamlenin bir sonraki oyuncuya geçmesini sağlar.
def rengi_degistir(renk):
    if renk == BEYAZ:
        renk = SIYAH
    else:
        renk = BEYAZ
    return renk


# Hamle sayısı kadar dönerek tas_yerlestir fonksiyonunu çağırır.
def hamleler(hamle_sayisi, renk, konumlar, satir, sutun):
    for hamle in range(hamle_sayisi):
        tas_yerlestir(renk, konumlar)
        renk = rengi_degistir(renk)
        oyun_tahtasi(konumlar, satir, sutun)


# Beyaz kare ve siyah kare sayısı kadar taş almaya yarar.
def tas_al(beyaz_kare_sayi, siyah_kare_sayi, konumlar, kare_indexleri, satir, sutun, siyah_tas, beyaz_tas):
    renk = BEYAZ
    kare_sayilari = [beyaz_kare_sayi, siyah_kare_sayi]
    for kare_rengi in kare_sayilari:
        for _ in range(kare_rengi):
            tas_al_kontrol(renk, kare_indexleri, konumlar, satir, sutun)
            oyun_tahtasi(konumlar, satir, sutun)
            if renk == BEYAZ:
                siyah_tas -= BIR
            else:
                beyaz_tas -= BIR
        renk = rengi_degistir(renk)

    return beyaz_tas, siyah_tas


# Oyuncudan almak istediği taşın koordinatını alır ve o koordinattan taşı almayı sağlar.
def tas_al_kontrol(renk, kare_indexleri, konumlar, satir, sutun):
    yanlis_deger = True
    renk = rengi_degistir(renk)
    while yanlis_deger:
        try:
            tas_degeri = input("Almak istediğiniz taşın değerini giriniz: ").upper()
            if tas_degeri not in kare_indexleri:
                satir_index = int(tas_degeri[0]) - BIR
                sutun_index = ord(tas_degeri[1]) - A_ASCII_KODU
                if satir_index <= satir and sutun_index <= sutun and konumlar[satir_index][sutun_index] == renk:
                    konumlar[satir_index][sutun_index] = " "
                    yanlis_deger = False
                else:
                    print("Geçersiz değer girdiniz, lütfen tekrar giriniz.")
            else:
                print("Geçersiz değer girdiniz, lütfen tekrar giriniz.")
        except IndexError:
            print("Girdiğiniz değer tahtada bulunmuyor. Lütfen tekrar giriniz.")
        except ValueError:
            print("Değerinizin ilk basamağı sayı olmak zorunda. Lütfen tekrar giriniz.")


# Oyundaki herhangi bir renkten 3 tane taş kalıncaya kadar döngüye girer.
# İlk önce siyah kare ve beyaz kare sayısı kadar taş alır daha sonra kare oluşuncaya kadar taşları hareket ettirir.
def oyun_sonu(beyaz_kare_sayi, siyah_kare_sayi, konumlar, kare_indexleri, satir, sutun, siyah_tas, beyaz_tas, renk):
    oyun_bitmedi = True
    while oyun_bitmedi:
        beyaz_tas, siyah_tas = tas_al(beyaz_kare_sayi, siyah_kare_sayi, konumlar,
                                      kare_indexleri, satir, sutun, siyah_tas, beyaz_tas)

        kare_olusmadi = True
        if beyaz_tas == 3 or siyah_tas == 3:
            oyun_bitmedi = False
            kare_olusmadi = False
        while kare_olusmadi:
            beyaz_kare_sayi, siyah_kare_sayi, kare_indexleri = tas_hareket_ettir(konumlar, renk, satir, sutun)

            renk = rengi_degistir(renk)
            if kare_indexleri:
                kare_olusmadi = False

    if beyaz_tas > 3:
        kazanan = "Beyaz"
    else:
        kazanan = "Siyah"
    return kazanan


# Hareket edilecek taşın konumunu ve nereye hareket edileceğini alır ve taşı o konuma hareket ettirir.
def tas_hareket_ettir(konumlar, renk, satir, sutun):
    kare_index = []
    beyaz_kare_sayi = 0
    siyah_kare_sayi = 0
    try:
        tas_konumu = input("Hareket ettirmek istediğinz taşın koordinatlarını ve hareket ettireceğiniz yeri giriniz:")\
                    .upper()
        if len(tas_konumu) == 5 and tas_konumu[SIFIR].isdigit() and tas_konumu[UC].isdigit():
            ilk_satir_index = int(tas_konumu[SIFIR]) - BIR
            ilk_sutun_index = ord(tas_konumu[BIR]) - A_ASCII_KODU
            son_satir_index = int(tas_konumu[UC]) - BIR
            son_sutun_index = ord(tas_konumu[DORT]) - A_ASCII_KODU
            if konumlar[ilk_satir_index][ilk_sutun_index] == renk and konumlar[son_satir_index][son_sutun_index] == " ":
                hareket = hareket_edebilir_mi(konumlar, ilk_satir_index, ilk_sutun_index, son_satir_index,
                                              son_sutun_index)
                if hareket:
                    konumlar[ilk_satir_index][ilk_sutun_index] = " "
                    konumlar[son_satir_index][son_sutun_index] = renk
                    _, _, kare_indexleri = kare_sayisi(konumlar, satir, sutun, oyun_basi=False)

                    for indexler in kare_indexleri:
                        if tas_konumu[UC:] in indexler:
                            kare_index = indexler
                            if renk == SIYAH:
                                siyah_kare_sayi = BIR
                            else:
                                beyaz_kare_sayi = BIR
                else:
                    print("O konuma hareket ettiremezsiniz. Lütfen tekrar giriniz.")
            else:
                print("Hareket ettirmek istediğiniz taş sizin renginiz değil ya da hareket konumu boş değil.")
        else:
            print("1. ve 3. degeriniz tam sayı olmak zorundadır. Lütfen tekrar giriniz")
    except ValueError:
        print("İlk değeriniz tam sayı olmak zorundadır. Lütfen tekrar giriniz.")
    except IndexError:
        print("Girdiginiz değer oyun tahtasında bulunmamaktadır. Lütfen Tekrar giriniz.")
    return beyaz_kare_sayi, siyah_kare_sayi, kare_index


# Belirlenen konumun dolu olup olmadığını kontrol eder.
def dolu_mu(konumlar, satir, sutun):
    if konumlar[satir][sutun] != " ":
        return False
    else:
        return True


# Belirlenen taşın istenilen konuma hareket edip edilemeyeceğini kontrol eder.
def hareket_edebilir_mi(konumlar, ilk_satir_index, ilk_sutun_index, son_satir_index, son_sutun_index):
    dolu = True
    if ilk_satir_index == son_satir_index:
        if ilk_sutun_index > son_sutun_index:
            for ikinci_index in range(ilk_sutun_index - BIR, son_sutun_index, EKSI_BIR):
                dolu = dolu_mu(konumlar, ilk_satir_index, ikinci_index)
        else:
            for ikinci_index in range(ilk_sutun_index + BIR, son_sutun_index):
                dolu = dolu_mu(konumlar, ilk_satir_index, ikinci_index)
    elif ilk_sutun_index == son_sutun_index:
        if ilk_satir_index > son_satir_index:
            for ilk_index in range(ilk_satir_index - BIR, son_satir_index, EKSI_BIR):
                dolu = dolu_mu(konumlar, ilk_index, ilk_sutun_index)
        else:
            for ilk_index in range(ilk_satir_index + BIR, son_satir_index):
                dolu = dolu_mu(konumlar, ilk_index, ilk_sutun_index)
    else:
        dolu = False

    return dolu


# Oyun tahtasındaki kareleri saymaya yarar.
def kare_sayisi(konumlar, satir, sutun, oyun_basi):
    kare_indexleri = []
    siyah_kare_sayi = 0
    beyaz_kare_sayi = 0

    for satir_index in range(satir - BIR):
        for sutun_index in range(sutun - BIR):
            anlik_konum = konumlar[satir_index][sutun_index]
            sag_konum = konumlar[satir_index][sutun_index + BIR]
            alt_konum = konumlar[satir_index + BIR][sutun_index]
            capraz_konum = konumlar[satir_index + BIR][sutun_index + BIR]
            if anlik_konum == sag_konum \
                    and anlik_konum == alt_konum \
                    and anlik_konum == capraz_konum:
                anlik = str(satir_index + BIR) + chr(sutun_index + A_ASCII_KODU)
                sag = str(satir_index + BIR) + chr(sutun_index + BIR + A_ASCII_KODU)
                alt = str(satir_index + IKI) + chr(sutun_index + A_ASCII_KODU)
                capraz = str(satir_index + IKI) + chr(sutun_index + BIR + A_ASCII_KODU)
                kare_indexleri.append([anlik, sag, alt, capraz])
                if konumlar[satir_index][sutun_index] == BEYAZ:
                    beyaz_kare_sayi += BIR
                else:
                    siyah_kare_sayi += BIR
    if oyun_basi:
        if siyah_kare_sayi == SIFIR and beyaz_kare_sayi == SIFIR:
            beyaz_kare_sayi = 1
    return siyah_kare_sayi, beyaz_kare_sayi, kare_indexleri


# Oyunla ilgili temel fonksiyonları çağırmaya yarar yani bir nevi oyunu başlatır.
def oyunu_baslat(aralik, renk):
    hamle_sayisi, konumlar, satir_sayi, sutun_sayi, beyaz_tas, siyah_tas = satir_sayisi_al(aralik)
    hamleler(hamle_sayisi, renk, konumlar, satir_sayi, sutun_sayi)
    siyah_kare_sayi, beyaz_kare_sayi, kare_indexleri = kare_sayisi(konumlar, satir_sayi, sutun_sayi, oyun_basi=True)
    kazanan = oyun_sonu(beyaz_kare_sayi, siyah_kare_sayi, konumlar, kare_indexleri, satir_sayi, sutun_sayi, siyah_tas,
                        beyaz_tas, renk)
    return kazanan


# Yeni oyun başlatmamıza yarar.
def yeni_oyun_baslat(aralik, renk):
    yeni_oyun = input("Yeniden oynamak ister misiniz?(E/H):").upper()
    while yeni_oyun not in EVET_HAYIR:
        print("Sadece e/E ya da h/H değerlerini girebilirsiniz. Lütfen tekrar giriniz.")
        yeni_oyun = input("Yeniden oynamak ister misiniz?(E/H):").upper()
    if yeni_oyun == EVET:
        kazanan = oyunu_baslat(aralik, renk)
        print(f"Kazanan renk: {kazanan}")
        yeni_oyun_baslat(aralik, renk)


def main():
    aralik = [3, 4, 5, 6, 7]
    renk = BEYAZ
    kazanan = oyunu_baslat(aralik, renk)
    print(f"Kazanan renk: {kazanan}")
    yeni_oyun_baslat(aralik, renk)


main()