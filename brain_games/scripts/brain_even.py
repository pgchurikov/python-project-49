#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.games.even import even_condition


def main():
    print('brain-even\n')
    play_game(even_condition, GAME_INSTRUCTIONS["even"])


if __name__ == '__main__':
    main()
