#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games.gcd import brain_gcd


def main():
    print('brain-gcd\n')
    play_game(brain_gcd)


if __name__ == '__main__':
    main()
