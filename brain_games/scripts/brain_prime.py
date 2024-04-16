#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.games.prime import prime_condition


def main():
    print('brain-prime\n')
    play_game(prime_condition, GAME_INSTRUCTIONS["prime"])


if __name__ == '__main__':
    main()
