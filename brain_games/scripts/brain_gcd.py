#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.games.gcd import gcd_condition


def main():
    print('brain-gcd\n')
    play_game(gcd_condition, GAME_INSTRUCTIONS["gcd"])


if __name__ == '__main__':
    main()
