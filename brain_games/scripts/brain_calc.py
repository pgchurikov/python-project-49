#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games import calc


def main():
    print('brain-calc\n')
    play_game(calc)


if __name__ == '__main__':
    main()
