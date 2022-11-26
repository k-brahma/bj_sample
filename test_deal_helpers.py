from unittest import TestCase

from deal_helpers import get_dealer_current_score, get_deal_result, DealResult


class TestGetDealResult(TestCase):
    """ get_deal_result のテスト """

    def test_dealer_over_21(self):
        """ ディーラーが21を超えている場合 """
        player_score = 20
        dealer_score = 22
        result = get_deal_result(player_score, dealer_score)
        self.assertEqual(result, DealResult.win)

    def test_player_over_dealer(self):
        """ プレイヤーのスコアがディーラーのスコアを超えている場合 """
        player_score = 20
        dealer_score = 19
        result = get_deal_result(player_score, dealer_score)
        self.assertEqual(result, DealResult.win)

    def test_player_dealer_equal(self):
        """ プレイヤーとディーラーのスコアが同じ場合 """
        player_score = 20
        dealer_score = 20
        result = get_deal_result(player_score, dealer_score)
        self.assertEqual(result, DealResult.draw)

    def test_player_under_dealer(self):
        """ プレイヤーのスコアがディーラーのスコアより小さい場合 """
        player_score = 20
        dealer_score = 21
        result = get_deal_result(player_score, dealer_score)
        self.assertEqual(result, DealResult.lose)


class TestGetFixedScore(TestCase):
    """ get_dealer_current_score のテスト """

    def test_lt_21(self):
        """ 21以下の場合はそのまま返す """
        self.assertEqual(get_dealer_current_score(20, 0), 20)

    def test_just_21(self):
        """ 21の場合 """
        self.assertEqual(get_dealer_current_score(21, 0), 21)

    def test_gt_21(self):
        """ 21を超えていて、 ace が含まれていない場合 """
        self.assertEqual(get_dealer_current_score(22, 0), 22)

    def test_lte_21_has_aces(self):
        """ ace が含まれていても、21以下ならば受け取った値をそのまま返す """
        self.assertEqual(get_dealer_current_score(20, 1), 20)

    def test_gt_21_has_aces(self):
        """ 21を超えていて、 ace が含まれている場合
            ace の枚数にかかわらず、21 以下ならばそこで確定 """
        self.assertEqual(get_dealer_current_score(22, 1), 12)
        self.assertEqual(get_dealer_current_score(22, 2), 12)

    def test_gt_31_has_one_ace(self):
        """ 21以下にするには、aceを2枚使う必要がある場合 """
        self.assertEqual(get_dealer_current_score(32, 1), 22)
        self.assertEqual(get_dealer_current_score(32, 2), 12)
        self.assertEqual(get_dealer_current_score(32, 3), 12)
