#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games.prime import brain_prime


def main():
    print('brain-prime\n')
    play_game(brain_prime)


if __name__ == '__main__':
    main()
