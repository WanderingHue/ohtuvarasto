import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.osittainen = Varasto(10, 3)
        self.tilaton = Varasto(0)
        self.taysi = Varasto(10, 10)
        self.negatiivinen = Varasto(-1, -1)
        self.liiantaysi = Varasto (10, 11)


    # Varaston luomisen testit
    def test_luodaan_liiantaysi_varasto(self):
        # https://docs.python.org/3/library unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.liiantaysi.saldo, 10)
        self.assertAlmostEqual(self.liiantaysi.tilavuus, 10)
        self.assertAlmostEqual(self.liiantaysi.paljonko_mahtuu(), 1)


    def test_luodaan_taysi_varasto(self):
        # https://docs.python.org/3/library unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.taysi.saldo, 10)
        self.assertAlmostEqual(self.taysi.tilavuus, 10)
        self.assertAlmostEqual(self.taysi.paljonko_mahtuu(), 0)


    def test_luodaan_tilaton_varasto(self):
        # https://docs.python.org/3/library unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.tilaton.saldo, 0)
        self.assertAlmostEqual(self.tilaton.tilavuus, 0)
        self.assertAlmostEqual(self.tilaton.paljonko_mahtuu(), 0)


    def test_luodaan_negatiivinen_varasto(self):
        # https://docs.python.org/3/library unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.negatiivinen.saldo, 0)
        self.assertAlmostEqual(self.negatiivinen.tilavuus, 0)
        self.assertAlmostEqual(self.negatiivinen.paljonko_mahtuu(), 0)


    def test_luodaan_osittainen_varasto(self):
        self.assertAlmostEqual(self.osittainen.saldo, 3)
        self.assertAlmostEqual(self.osittainen.tilavuus, 10)
        self.assertAlmostEqual(self.osittainen.paljonko_mahtuu(), 7)


    def test_luodaan_normaali_varasto(self):
        # https://docs.python.org/3/library unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")


    # Lisäämisen testit
    def test_varastoo_lisataan(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)


    def test_varastoon_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)


    def test_varastoon_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-6)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    # Ottamisen testit
    def test_varastosta_otetaan(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(2), 2)
        self.assertAlmostEqual(self.varasto.saldo, 6)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_varastosta_otetaan_liikaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 8)
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)


    def test_varastosta_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
