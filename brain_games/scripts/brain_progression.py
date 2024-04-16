#!/usr/bin/env python3


from brain_games.core import play_game
from brain_games.constant import GAME_INSTRUCTIONS
from brain_games.games.progression import progression_condition


def main():
    print('brain-progression\n')
    play_game(progression_condition, GAME_INSTRUCTIONS["progression"])


if __name__ == '__main__':
    main()
