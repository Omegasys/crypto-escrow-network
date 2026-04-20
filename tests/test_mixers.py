import unittest
from mixers.mixer_1 import Mixer1
from mixers.mixer_2 import Mixer2
from mixers.mixer_3 import Mixer3
from mixers.mixer_4 import Mixer4
from mixers.mixer_5 import Mixer5
from mixers.mixer_6 import Mixer6
from wallet_2A_6F import MixerWallet

class TestMixers(unittest.TestCase):

    def test_mixer_1(self):
        mixer = Mixer1()
        sender_wallet = MixerWallet(balance=100.0, address="Sender1")
        target_wallet = mixer.mix(50.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 50.0)
        self.assertEqual(target_wallet.get_balance(), 50.0)

    def test_mixer_2(self):
        mixer = Mixer2()
        sender_wallet = MixerWallet(balance=100.0, address="Sender2")
        target_wallet = mixer.mix(30.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 70.0)
        self.assertEqual(target_wallet.get_balance(), 30.0)

    def test_mixer_3(self):
        mixer = Mixer3()
        sender_wallet = MixerWallet(balance=100.0, address="Sender3")
        target_wallet = mixer.mix(40.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 60.0)
        self.assertEqual(target_wallet.get_balance(), 40.0)

    def test_mixer_4(self):
        mixer = Mixer4()
        sender_wallet = MixerWallet(balance=100.0, address="Sender4")
        target_wallet = mixer.mix(50.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 50.0)
        self.assertEqual(target_wallet.get_balance(), 50.0)

    def test_mixer_5(self):
        mixer = Mixer5()
        sender_wallet = MixerWallet(balance=100.0, address="Sender5")
        target_wallet = mixer.mix(60.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 40.0)
        self.assertEqual(target_wallet.get_balance(), 60.0)

    def test_mixer_6(self):
        mixer = Mixer6()
        sender_wallet = MixerWallet(balance=100.0, address="Sender6")
        target_wallet = mixer.mix(70.0, sender_wallet)
        self.assertEqual(sender_wallet.get_balance(), 30.0)
        self.assertEqual(target_wallet.get_balance(), 70.0)

if __name__ == '__main__':
    unittest.main()
