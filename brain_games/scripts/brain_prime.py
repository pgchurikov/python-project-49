#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games import prime


def main():
    print('brain-prime\n')
    play_game(prime)


if __name__ == '__main__':
    main()
