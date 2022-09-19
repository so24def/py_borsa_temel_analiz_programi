def LikiditeRasyo():

      DonenVarliklar = float(input("\n Dönen varlıklar değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      KisaDonemYabanciKaynaklar = float(input("\n Kısa dönem yabancı kaynaklar değerini(veya yükümlülükler diye geçer) giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      Stoklar = float(input("\n Stokların değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      print("")
      CariOran = DonenVarliklar/KisaDonemYabanciKaynaklar
      AsitTestiOrani = (DonenVarliklar - Stoklar) / KisaDonemYabanciKaynaklar
      print("Girilen değerlere göre Cari Oran: ", CariOran)
      print("")
      print("Girilen değerlere göre Asit Testi Oran: ", AsitTestiOrani)


def MaliYapiRasyo():

      ToplamBorc = float(input("\n Toplam borç değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      ToplamVarlik = float(input("\n Toplam varlık değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      DuranVarliklar = float( input("\n Duran varlıklar değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      OzSermaye = float(input("\n Öz sermaye değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      print("")
      KaldıracOrani = ToplamBorc/ToplamVarlik
      DuranVarlikSermayeOran = DuranVarliklar / OzSermaye
      print("Girilen değerlere göre Kaldıraç Oranı: ", KaldıracOrani)
      print("")
      print("Girilen değerlere göre Duran Varlıkların Öz Sermayeye Oranı: ", DuranVarlikSermayeOran)

def FaaliyetRasyo():

      NetSatislar = float(input("\n Net satışların(hasılat) değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      KisaVadeliTicAlacaklar = float(input("\n Kısa vadeli ticari alacakların değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      SatislarinMaaliyeti = float(input("\n Satışların maaliyeti değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      DonemBasiStok = float( input("\n Dönem başı stok değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      DonemSonuStok = float(input("\n Dönem sonu stok değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      print("")
      AlacakDevirHizi = NetSatislar/KisaVadeliTicAlacaklar
      AlacakTahsilSuresi = 365/AlacakDevirHizi
      StokDevirHizi = SatislarinMaaliyeti/((DonemBasiStok+DonemSonuStok)/2)
      StokDonusumSuresi = 365/StokDevirHizi
      print("Girilen değerlere göre Alacak Devir Hızı: ", AlacakDevirHizi, " ve Alacak Tahsil Süresi: ",AlacakTahsilSuresi)
      print("")
      print("Girilen değerlere göre Stok Devir Hızı: ", StokDevirHizi, " ve Stok Dönüşüm Süresi: ", StokDonusumSuresi)

def KarlilikRasyo():

      NetKar = float( input("\n Net kar(ana ortaklık payları) değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      NetSatislar = float(input("\n Net satışların(hasılat) değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      OzSermaye = float(input("\n Öz sermaye değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      print("")
      NetKarMarji = NetKar/NetSatislar
      OzSermayeKarliligi = NetKar/OzSermaye
      print("")
      print("Girilen değerlere göre Net Kar Marjı: ", NetKarMarji)
      print("")
      print("Girilen değerlere göre Öz Sermaye Karlılığı: ", OzSermayeKarliligi)

def Tahminleme():

      HasilatGuncelDonem = float(input("\n Açıklanan ve güncel en son dönemin hasılat değerini giriniz(örneğin ilk 6 aylık açıklanmışsa 6 aylık tablosundaki hasılatı giriniz), sayıyı yazarken nokta veya virgül kullanmayınız: "))
      HasilatGecenDonem = float(input("\n Açıklanandan bir önceki hasılat değerini giriniz(örneğin ilk 6 aylık açıklanmışsa, 3 aylık tablosundaki hasılatı giriniz), sayıyı yazarken nokta veya virgül kullanmayınız: "))
      GuncelDonemHasilat = float(input("\n Bu senenin hasılatını giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      GuncelDonemNetKar = float( input("\n Bu senenin NET DÖNEM KARI değerini(özkaynaklar kısmında) giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      HisseSenediSayisi = float( input("\n Hisse senedi sayısını(ödenmiş sermaye) giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      yuzde = float(input("\n Güvenli bir tahmin yapabilmek için, çıkan sonucu yüzde kaç aşağı yuvarlamak istiyorsunuz? Örneğin %15 için sadece 15 yazıp enter'a basınız. En az %10 önerilir."))
      print("")
      HasilatDegisimKatsayisi = HasilatGuncelDonem/HasilatGecenDonem
      YilsonuHasilatTahmini = (HasilatDegisimKatsayisi * HasilatGuncelDonem) - ((HasilatDegisimKatsayisi * HasilatGuncelDonem) * (yuzde/100))
      NetKarMarji = GuncelDonemNetKar/HasilatGuncelDonem
      YilsonuNetKarTahmin = YilsonuHasilatTahmini * NetKarMarji
      HisseBasinaNetKar = YilsonuNetKarTahmin/HisseSenediSayisi
      print("Girilen değerlere göre Hasılat Değişim Katsayısı: ", HasilatDegisimKatsayisi)
      print("")
      print("Girilen değerlere göre ve %",yuzde,"güven ile Yılsonu Hasılat Tahmini: ", YilsonuHasilatTahmini)
      print("")
      print("Girilen değerlere göre Net Kar Marjı: ", NetKarMarji)
      print("")
      print("Girilen değerlere göre Yılsonu Net Kar Tahmini: ", YilsonuNetKarTahmin)
      print("")
      print("Girilen değerlere göre Hisse Başına Net Kar: ", HisseBasinaNetKar)

def Degerleme():
      HisseBorsaFiyat = float(input("\n !!!ÖNEMLİ!!! Hisse senedinin borsa fiyatını giriniz, sayıyı yazarken VİRGÜL KULLANMAYINIZ, NOKTA KULLANARAK YAZINIZ ! \n Örneğin 15,25 DEĞİL 15.25 yazınız !!! : "))
      HisseBasinaNetKar = float(input("\n Tahmin kısmında hesapladığınız HİSSE BAŞINA KAR değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      OzKaynaklar = float(input("\n Öz Kaynaklar değerini(ana ortaklığa ait) giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      YilsonuNetKarTahmin = float(input("\n Tahmin kısmında hesapladığınız YILSONU NET KAR TAHMİNİ değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      NetKar = float(input("\n NET DÖNEM KARI değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      HisseSenediSayisi = float(input("\n Hisse senedi sayısını(ödenmiş sermaye) değerini giriniz, sayıyı yazarken nokta veya virgül kullanmayınız: "))
      print("")
      FirmaFK = HisseBorsaFiyat/HisseBasinaNetKar
      ogfFK = (10/FirmaFK) * HisseBorsaFiyat
      YilsonuTahminiOzkaynak = OzKaynaklar + (YilsonuNetKarTahmin - NetKar)
      HisseBasinaDefterDegeri = YilsonuTahminiOzkaynak/HisseSenediSayisi
      FirmaPDDD = HisseBorsaFiyat/HisseBasinaDefterDegeri
      ogfPDDD = (2/FirmaPDDD) * HisseBorsaFiyat
      GercekDeger = (ogfFK + ogfPDDD)/2
      print("Girilen değerlere göre Firma F/K: ", FirmaFK, "ve Firma F/K 'ya göre olması gereken fiyat: ", ogfFK)
      print("")
      print("Girilen değerlere göre Yılsonu Tahmini Öz Kaynak: ", YilsonuTahminiOzkaynak,"\n Hisse Başına Defter Değeri : ",HisseBasinaDefterDegeri )
      print("")
      print("Girilen değerlere göre Firma PD/DD: ", FirmaPDDD, "ve Firma PD/DD 'ye göre olması gereken fiyat: ", ogfPDDD)
      print("")
      print("F/K ve PD/DD hesaplamalarına göre HİSSENİN GERÇEK(NİHAİ DEĞERİ): ", GercekDeger)



while 1:
      print(
            "\n\n*** RASYOLAR (ORANLAR) *** \n\n" +
            "1 - Likidite Rasyoları\n" + "\t - Cari Oran \n" + " \t - Asit Test Oranı \n\n" +
            "2 - Mali Yapı Rasyoları \n " + "\t - Kaldıraç Oranı \n" + "\t - Duran Varlık/Öz Sermaye Oranı \n\n" +
            "3 - Faaliyet(Aktivite) Rasyoları \n " + "\t - Alacak Devir Hızı \n" + "\t - Stok Devir Hızı \n\n" +
            "4 - Karlılık(Verimlilik) Rasyoları \n " + "\t - Net Kar Marjı \n" + "\t - Öz Sermaye Karlılığı \n\n" +
            "*** HİSSE DEĞERLEMESİ *** \n\n" +
            "5 - Yılsonu Tahminleri\n" + "\t - Hasılat Değişim Katsayısı \n " + "\t - Yılsonu Hasılat Tahmini \n" +
            "\t - İlgili Dönem Kar Marjı \n" + "\t - Yılsonu Net Kar Tahmini \n" + "\t - Hisse Başına Net Kar \n\n" +
            "6 - Yapılan Tahmin Sonuçları ile Hisse Değerleme \n" + "\t - Firma F/K ile Olması Gereken Değer \n " +
            "\t - Firma PD/DD ile olması gereken değer\n" + "\t - F/K ve PD/DD ile HİSSENİN GERÇEK (NİHAİ) DEĞER \n "
            )
      ilkSecenek = int(input("\n\n HESAPLAMAK İSTEDİĞİNİZ VERİ GRUBUNU, BAŞINDAKİ NUMARAYI YAZIP VE ARDINDAN ENTER'A BASARAK SEÇİNİZ(Çıkış için 0) :  \n\n\n\n"))
      if ilkSecenek == 1:
            LikiditeRasyo();
            sonrakiSecenek = int(input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 2:
            MaliYapiRasyo();
            sonrakiSecenek = int(
                  input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 3:
            FaaliyetRasyo();
            sonrakiSecenek = int(
                  input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 4:
            KarlilikRasyo();
            sonrakiSecenek = int(
                  input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 5:
            Tahminleme();
            sonrakiSecenek = int(
                  input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 6:
            Degerleme();
            sonrakiSecenek = int(
                  input("\n\n Hesaplamaya devam etmek için 1 , çıkmak için 0 yazıp enter 'a basınız : \n\n"))
            if sonrakiSecenek == 0:
                  break;
            else:
                  continue;

      elif ilkSecenek == 0:
            break;

      else:
            print("Geçersiz bir sayı girdiniz, hesaplamak istediğiz veri grubu için gerekli sayıyı giriniz")


