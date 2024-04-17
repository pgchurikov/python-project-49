#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games.calc import brain_calc


def main():
    print('brain-calc\n')
    play_game(brain_calc)


if __name__ == '__main__':
    main()
