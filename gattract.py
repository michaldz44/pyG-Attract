import argparse
import json
import sys
from golem import Golem

def main():
    parser = argparse.ArgumentParser(description='Gravitational attractors')
    parser.add_argument('--dt', type=float, default=0.05, help='timestep')
    parser.add_argument('--h', type=float, default=0.2, help='magic depth parameter - DO NOT CHANGE!!!!')
    parser.add_argument('--pot_d', type=float, default=0.005, help='potential diameter')
    parser.add_argument('--term_v', type=float, default=0.005, help='terminatig velocity')
    parser.add_argument('--mu', type=float, default=0.7, help='friction coefficient')
    parser.add_argument('--size', type=int, default=100, help='Problem size (N as it will compute NxN matrix) ')
    args = parser.parse_args()

    bitmap=[[Golem(x,y,args) for x in range(N)] for y in range(N)]


if __name__ == "__main__":
    main()
