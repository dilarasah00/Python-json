import json

def urunler(urunAdi, fiyat, satistami, kategori):
    urun  = {
            "name": urunAdi,
            "fiyat": fiyat,
            "satis_durumu": satistami,
            "urun_kategori": kategori
        }
    with open("urunler.json", "w") as file:
        json.dump(urun, file, ensure_ascii= False)

#urunler("samsung",1000, True, ["telefon", "elektronik"])
     


def urun_bilgi():

    with open("urunler.json") as file:
        urun = json.load(file)
    print(urun)

urun_bilgi()





         