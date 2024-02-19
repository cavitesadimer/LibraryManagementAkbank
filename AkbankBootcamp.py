class Library():

  def __init__(self):
    self.dosya = open("books.txt", "a+") 
  
  def kitap_ekle(self,kitap_adi,yazar_adi,yayin_yili,sayfa_sayisi):
    self.dosya.write(kitap_adi + ", " + yazar_adi + ", " + yayin_yili + ", " + sayfa_sayisi + "")
    print("Kitap ekleme basarili")
  
  def kitap_sil(self,kitap_adi):
    self.dosya.seek(0)  
    satirlar = self.dosya.readlines()
    self.dosya.seek(0)
    self.dosya.truncate()
    for satir in satirlar:
        if kitap_adi not in satir:
            self.dosya.write(satir)
    print("Kitap silme basarili")
    
  def kitap_listele(self):
    print("Kitap Listesi:")
    self.dosya.seek(0)  
    satirlar = self.dosya.read().splitlines()
    if(len(satirlar)==0):
      print("Kitap mevcut degil")
    for satir in satirlar:
      kitap_yazar = satir.split(", ")[:2]
      print(f"Kitap: {kitap_yazar[0]} Yazar: {kitap_yazar[1]}")

  def __del__(self):
    self.dosya.close()

while 1:
  print ("\n*** MENU ***")
  print("1-Kitap listele")
  print("2-Kitap ekle")
  print("3-Kitap sil")
  print("q-Cikis\n")
  secim = input("Lütfen secim yapiniz: ")
  if secim == "1":
    lib = Library()
    lib.kitap_listele()

  elif secim == "2":
    
    kitap_adi = input("Kitap Adi: ")
    yazar_adi= input("Kitabin Yazari: ")
    yayin_yili = input("Yayin Tarihi: ")
    sayfa_sayisi = input("Sayfa Sayisi: ")
    lib = Library()
    lib.kitap_ekle(kitap_adi,yazar_adi,yayin_yili,sayfa_sayisi)

  elif secim == "3":
    silinecek_kitap_adi = input("Silinecek kitap adini giriniz: ")
    lib = Library()
    lib.kitap_sil(silinecek_kitap_adi)

  elif secim == "q":
    print("Program sonlandiriliyor")
    break
    
  else:
     print("Hatali secim")
  