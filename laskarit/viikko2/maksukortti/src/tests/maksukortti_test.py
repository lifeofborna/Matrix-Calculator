import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")


    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")


    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")


    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        for i in range(3):
            self.kortti.syo_edullisesti()
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.5 euroa")
    

    def test_negatiivisen_summan_lataaminen_ei_muuta_saldoa(self):
        self.kortti.lataa_rahaa(-10)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10 euroa")


    def test_kortilla_voi_ostaa_edullisen_lounaan_kun_rahaa_sen_verran(self):
        
        for i in range(3):
            self.kortti.syo_edullisesti()
        ##Rahaa 2.5 jäljellä
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.0 euroa")
    

    def test_kortilla_voi_ostaa_maukkaan_lounaan_kun_kortilla_maukkaan_verran_rahaa(self):
        for i in range(2):
            self.kortti.syo_maukkaasti()
        ##2e
        self.kortti.lataa_rahaa(2)
        #4e
        self.kortti.syo_maukkaasti()
        #0e

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0 euroa")