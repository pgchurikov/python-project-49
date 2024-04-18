#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games import gcd


def main():
    print('brain-gcd\n')
    play_game(gcd)


if __name__ == '__main__':
    main()
