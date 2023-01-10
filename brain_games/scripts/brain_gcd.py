#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import brain_gcd


def main():
    engine.play(brain_gcd)


if __name__ == '__main__':
    main()
