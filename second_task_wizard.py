"""
В N корзинах находятся золотые монеты. Корзины пронумерованы числами от 1 до N. Во всех корзинах, кроме одной,
монеты весят по w граммов. В одной корзине монеты фальшивые и весят w–d граммов. Волшебник берет 1 монету из первой
корзины, 2 монеты из второй корзины, и так далее, и, наконец, N-1 монету из (N-1)-й корзины. Из N-й корзины он не
берет ничего. Он взвешивает взятые монеты и сразу указывает на корзину с фальшивыми монетами. Напишите программу,
которая сможет выполнять такое волшебство. Дано: четыре целых числа: N, w, d и P – суммарный вес отобранных монет.
Найти номер корзины с фальшивыми монетами.
"""


def find_counterfeit_basket(num_of_bask, coin_weight, weight_diff, total_weigh_coins):
    """
    total_weight: вычисляет общий вес монет, но не используется напрямую при расчете количества фальшивых корзин.
    Полезная промежуточная переменная которая может быть использована для контроля расчетов.
    """
    if weight_diff == coin_weight:
        return num_of_bask
    total_weight = (num_of_bask * (num_of_bask + 1) // 2) * coin_weight
    taken_weight = (1 + num_of_bask - 1) * (num_of_bask - 1) // 2 * coin_weight
    diff = total_weigh_coins - taken_weight
    counterfeit_basket = diff // weight_diff + 1
    return counterfeit_basket if 0 < counterfeit_basket else num_of_bask


N = 5      # Общее количество корзин
w = 10     # Вес каждой обычной монеты в граммах
d = 2      # Разница в весе между обычными монетами и поддельными монетами в граммах
P = 105    # Общий вес выбранных монет в граммах

fake_basket = find_counterfeit_basket(N, w, d, P)
print(f"The counterfeit basket index is: {fake_basket}")
