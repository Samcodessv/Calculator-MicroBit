"""

Başlangıç değişkenleri

"""
"""

0: İşlem seçimi, 1: Birinci sayı, 2: İkinci sayı, 3: Sonuç

"""
"""

0: +, 1: -, 2: *, 3: /

"""
# Sistemi sıfırlayıp başa döndüren fonksiyon
def hesap_sifirla():
    global durum, islem_index, sayi1, sayi2
    durum = 0
    islem_index = 0
    sayi1 = 0
    sayi2 = 0
    ekran_guncelle()
# A Tuşuna basıldığında (Seçenekler arasında gezinme)

def on_button_pressed_a():
    global islem_index, sayi1, sayi2
    if durum == 0:
        # İşlemleri değiştir (0'dan 3'e kadar, 4 olunca 0'a döner)
        islem_index = (islem_index + 1) % 4
    elif durum == 1:
        # 1. sayıyı artır (0-9 arası)
        sayi1 = (sayi1 + 1) % 10
    elif durum == 2:
        # 2. sayıyı artır (0-9 arası)
        sayi2 = (sayi2 + 1) % 10
    elif durum == 3:
        # Sonuç ekranındayken A'ya basılırsa başa dön
        hesap_sifirla()
        return
    ekran_guncelle()
input.on_button_pressed(Button.A, on_button_pressed_a)

# Ekranda o anki durumu gösterecek fonksiyon
def ekran_guncelle():
    if durum == 0:
        basic.show_string("" + (islemler[islem_index]))
    elif durum == 1:
        basic.show_number(sayi1)
    elif durum == 2:
        basic.show_number(sayi2)
# B Tuşuna basıldığında (Onaylama / İleri gitme)

def on_button_pressed_b():
    global durum
    if durum == 0:
        durum = 1
        # 1. sayı seçimine geç
        ekran_guncelle()
    elif durum == 1:
        durum = 2
        # 2. sayı seçimine geç
        ekran_guncelle()
    elif durum == 2:
        durum = 3
        # Sonucu hesapla ve göster
        hesapla_ve_goster()
    elif durum == 3:
        # Sonuç ekranındayken B'ye basılırsa başa dön
        hesap_sifirla()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Matematiksel işlemi yapıp LED'de gösteren fonksiyon
def hesapla_ve_goster():
    global sonuc
    basic.clear_screen()
    basic.pause(200)
    # Hesaplıyor hissi vermek için kısa bir bekleme
    if islem_index == 0:
        sonuc = sayi1 + sayi2
    elif islem_index == 1:
        sonuc = sayi1 - sayi2
    elif islem_index == 2:
        sonuc = sayi1 * sayi2
    elif islem_index == 3:
        # Sıfıra bölünme hatasını engelle
        if sayi2 == 0:
            basic.show_string("HATA")
            return
        else:
            sonuc = sayi1 / sayi2
    basic.show_number(sonuc)
sonuc = 0
sayi2 = 0
sayi1 = 0
islem_index = 0
durum = 0
islemler: List[str] = []
islemler = ["+", "-", "*", "/"]
# Cihaz açıldığında ilk ekranı göster
ekran_guncelle()