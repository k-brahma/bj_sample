"""
ディーラーの挙動のデモ

スコアが16を超えるまではカードを引く。
16を超えたスコアが21を超えていない場合は終了。
21を超えている場合は、エースのスコアのうち1つを11点から1点に変更して再計算する。
ただし、この再計算は、エースの枚数分しかくりかえせない
"""

from cards import create_card_list, show_all_cards
from deal_helpers import get_deal_result, DealResult, set_dealer_final_card_list, get_default_dealer_cards

player_score = 18  # テスト用に適当に設定しました。実際には、カードを引いていって確定することになるかと

# 全カードのインスタンスのリストを生成
card_list = create_card_list()

# ディーラーが最初に有する2枚のカードを決定する
dealer_default_card_list = get_default_dealer_cards(card_list)

# 結果が確定するまでディーラーがカードに引かせ、引いたカードのリストと最終スコアを決める
dealer_card_list, dealer_score = set_dealer_final_card_list(dealer_default_card_list, card_list)

# ディーラーのカードのリストを出力する
for i, card in enumerate(dealer_card_list, 1):
    print(f'{i}枚目: {card}')

# カードのアスキーアートを横に並べて出力する
show_all_cards(dealer_card_list)

print(f"ディーラーのスコア: {dealer_score}点")
print(f"あなたのスコア    : {player_score}点")

# プレイヤーとディーラーのスコアを比較し、勝敗を決める
result = get_deal_result(player_score, dealer_score)

if result == DealResult.win:
    print("プレイヤーの勝ち")
elif result == DealResult.draw:
    print("引き分け")
else:
    print("プレイヤーの負け")
