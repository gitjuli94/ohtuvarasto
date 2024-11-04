import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_lisaa_tavaraa(self):
        self.varasto.lisaa_varastoon(80)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

        self.varasto.lisaa_varastoon(-80)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_liikaa_liikaa_pois(self):
        self.varasto.ota_varastosta(80)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

        self.varasto.ota_varastosta(-80)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_virheellinen_alustus(self):
        self.varasto_neg = Varasto(-10, -100)

        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)
        self.assertAlmostEqual(self.varasto_neg.saldo, 0)

        self.varasto_liikaa = Varasto(10, 100)

        self.assertAlmostEqual(self.varasto_liikaa.saldo, 10)

    def test_str(self):
        self.varasto_uusi = Varasto(100)
        self.assertEqual(str(self.varasto_uusi), "saldo = 0, vielä tilaa 10")
