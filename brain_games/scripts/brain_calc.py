#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.games.calc import calculation


def main():
    print('brain-calc\n')
    play_game(calculation, GAME_INSTRUCTIONS["calc"])


if __name__ == '__main__':
    main()
