
import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400) 

    def test_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_myytyjen_lounaiden_määrä_on_oikea(self):
        self.assertEqual(str(self.kassapaate.edulliset + self.kassapaate.maukkaat), "0")



    ##Edulliset kaikki testit:

##EDULLISET KÄTEISELLÄ

    def test_jos_maksu_riittävää_rahamäärä_kasvaa_lounaan_hinnalla_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")

    def test_vaihtoraha_oikein_kateisella_edulliset(self):
        s = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(s), "10")

    def test_kaikki_rahat_palautetaan_jos_maksu_ei_riittävä_kateisella(self):
        s = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(s), "200")

    def test_myytyjen_edullisten_maara_kasvaa_jos_maksu_riittava_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
    
    def test_myytyjen_edullisten_maara_ei_kasva_jos_maksu_ei_riittava_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.edulliset), "0")


### EDULLISET KORTILLA
    
    def test_jos_maksu_kortilla_riittava_veloitetetaan_kortista_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), "160")

    def test_jos_maksu_kortilla_ei_riittava_ei_veloiteteta_kortista_edulliset(self):
        self.maksukortti.ota_rahaa(200)

        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), "200")


    def test_jos_maksu_kortilla_riittava_palautetaan_True_edulliset(self):
        s = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(s), "True")

    def test_jos_maksu_kortilla_ei_riittava_palautetaan_False_edulliset(self):
        self.maksukortti.ota_rahaa(400)

        s = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(s), "False")

    def test_jos_kortilla_tarpeeksi_rahaa_edulliset_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")
    
    def test_jos_ei_kortilla_tarpeeksi_rahaa_edulliset_ei_kasva(self):
        self.maksukortti.ota_rahaa(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "0")
    
    def test_kassassa_oleva_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_kortille_ladataessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 20)
        self.assertEqual(str(self.maksukortti.saldo), "420")

    def test_kortille_ladataessa_kortin_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 20)
        self.assertEqual(str(self.maksukortti.saldo), "420")
    
    def test_kortille_ladataessa_kortin_saldo_ei_muutu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(str(self.maksukortti.saldo), "400")    


    def test_kortille_ladataessa_kassassa_oleva_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 20)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100020")

    def test_kortille_ladataessa_kassassa_oleva_rahamaara_ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 0)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")










##maukkaiden testit

##maukkaat kortilla
    
    def test_jos_maksu_kortilla_riittava_veloitetetaan_kortista_edulliset(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), "0")


    def test_jos_maksu_kortilla_ei_riittava_ei_veloiteteta_kortista_maukkaat(self):
        self.maksukortti.ota_rahaa(200)

        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), "200")



    def test_jos_maksu_kortilla_riittava_palautetaan_True_maukkaat(self):
        s = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(s), "True")

    def test_jos_maksu_kortilla_ei_riittava_palautetaan_False_maukkaasti(self):
        self.maksukortti.ota_rahaa(400)

        s = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(s), "False")

  
    def test_jos_kortilla_tarpeeksi_rahaa_maukkaat_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
    

    def test_jos_ei_kortilla_tarpeeksi_rahaa_maukkaat_ei_kasva(self):
        self.maksukortti.ota_rahaa(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    


    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_palauta_jos_ei_salittu_luku_kun_ladataan_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)

    

    








#MAUKKAAT kateisella

    def test_jos_maksu_riittävää_rahamäärä_kasvaa_lounaan_hinnalla_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")

    def test_vaihtoraha_oikein_kateisella_maukkaat(self):
        s = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(str(s), "50")

    def test_kaikki_rahat_palautetaan_jos_maksu_ei_riittävä_kateisella_maukkaat(self):
        s = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(s), "390")

    def test_myytyjen_maukkaiden_maara_kasvaa_jos_maksu_riittava_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")
    
    def test_myytyjen_maukkaiden_maara_ei_kasva_jos_maksu_ei_riittava_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")


## maukkaat kortilla
