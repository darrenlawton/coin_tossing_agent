import numpy as np
from statistics import mean

COIN_PROBABILITY = 0.5
SELECTION_PROBABILITY = 0.5
N_LOTTERY = 100000
TERMINAL_GAME = 16


def toss_coin(pb_head):
    if np.random.uniform(0, 1) < pb_head:
        return 1
    else: return 0


def get_selection(pb_select):
    if np.random.uniform(0, 1) < pb_select:
        return 1
    else: return 0


def play_game(bet):
    pick = get_selection(SELECTION_PROBABILITY)
    toss = toss_coin(COIN_PROBABILITY)
    if pick == toss:
        return bet * 2
    else:
        return bet * -1


def start_lottery(initial_bet):
    capital = initial_bet
    games = 1

    while games <= TERMINAL_GAME:
        bet = capital
        game_return = play_game(bet)
        capital = game_return
        # print("{} return after {} games".format(capital, games))
        if capital < 0: return initial_bet * -1, games, bet
        games = games + 1

    return capital, games, bet


if __name__ == '__main__':
    cum_pnl = []
    cum_games = []
    cum_max_bet = []

    for i in range(0, N_LOTTERY):
        game_return, n_games, max_bet = start_lottery(1)
        cum_pnl.append(game_return)
        cum_games.append(n_games)
        cum_max_bet.append(max_bet)

    print("total return: {}".format(sum(cum_pnl)))
    print("average games: {}".format(sum(cum_games)/len(cum_games)))
    print("max bet: {}".format(max(cum_max_bet)))