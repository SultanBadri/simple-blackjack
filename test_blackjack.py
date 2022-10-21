import unittest
import blackjack

class TestBlackJack(unittest.TestCase):
  def test_get_card_value(self):
    result = blackjack.get_card_value("A")
    self.assertEqual(result, 1)

  def test_get_hand_value(self):
    result = blackjack.get_hand_value(["Q", "2", "A", "8"])
    self.assertEqual(result, 21)

  def test_blackjack_game(self):
    result = blackjack.blackjack_game()
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()

