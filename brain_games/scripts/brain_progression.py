#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.games import progression


def main():
    print('brain-progression\n')
    play_game(progression)


if __name__ == '__main__':
    main()
