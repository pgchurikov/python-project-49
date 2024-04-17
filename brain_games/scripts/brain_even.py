#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games.even import brain_even


def main():
    print('brain-even\n')
    play_game(brain_even)


if __name__ == '__main__':
    main()
