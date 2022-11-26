import random
from dataclasses import dataclass


@dataclass
class DealResult:
    """
    勝敗を示す列挙型

    dataclassは未履修ですが...エクセルVBAの構造体のようなものです (^^;
    """
    win: int = 0
    draw: int = 1
    lose: int = 2


@dataclass
class Score:
    dealer_min: int = 17
    dealer_max: int = 21


def get_default_dealer_cards(card_list):
    """
    ディーラーが最初に引く2枚のカードを取得する

    :param card_list: ディーラーがこれから引くことが可能なカードのリスト。要素が2つ以上あることが前提
    :return: ディーラーが最初に引いた2枚のカードのリスト

    なお、リストはミュータブルなので、この関数内での変更が、呼び出し元にあるリストにも反映される。
    なので、戻り値として card_list を返す必要はない
    """
    dealer_card_list = []
    for _ in range(2):
        card = random.choice(card_list)
        dealer_card_list.append(card)
        card_list.remove(card)
    return dealer_card_list


def set_dealer_final_card_list(dealer_card_list, card_list):
    """
    ディーラーがカードを引いていき、最終的なスコアを確定させる
    unit testはありません。(用意できないことはないですが、説明がさらにかなり必要になるので)

    :param dealer_card_list: ディーラーがすでに引いている2枚目までのカード
    :param card_list: ディーラーがこれから引くことが可能なカードのリスト
    :return: 最終的なディーラーのカードのリストとスコアのタプル
    """

    # while 文内での処理用の初期値
    ace_count = 0  # list.filter で while 文内で算出するほうが良いですが、まずはこんな感じで。
    total_score = dealer_card_list[0].score + dealer_card_list[1].score  # A を常に11点とみなしたときの総得点
    dealer_score = total_score  # ディーラーのスコアとみなすべき値。最終的に戻り値になる。

    while dealer_score < Score.dealer_min:
        card = random.choice(card_list)
        dealer_card_list.append(card)
        card_list.remove(card)

        if card.is_ace:
            ace_count += 1

        total_score += card.score
        dealer_score = get_dealer_current_score(total_score, ace_count)

    return dealer_card_list, dealer_score


def get_dealer_current_score(score, ace_count):
    """
    16を超えた値を受け取り、ディーラーのスコアを計算する
    """
    while score > Score.dealer_max and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score


def get_deal_result(player_score, dealer_score):
    """
    プレイヤーとディーラーのスコアを受け取り、勝敗を判定する
    プレイヤーのスコアは 21 を超えていないという前提
    """
    if dealer_score > Score.dealer_max:
        return DealResult.win
    elif player_score > dealer_score:
        return DealResult.win
    elif player_score == dealer_score:
        return DealResult.draw
    else:
        return DealResult.lose
