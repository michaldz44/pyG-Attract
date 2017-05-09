import argparse
import json
import sys
from golem import Golem
from attractors import Attractors
import Image, ImageDraw, sys



def main():
    parser = argparse.ArgumentParser(description='Gravitational attractors')
    parser.add_argument('--dt', type=float, default=0.05, help='timestep')
    parser.add_argument('--h', type=float, default=0.2, help='magic depth parameter - DO NOT CHANGE!!!!')
    parser.add_argument('--pot_d', type=float, default=0.005, help='potential diameter')
    parser.add_argument('--term_v', type=float, default=0.005, help='terminatig velocity')
    parser.add_argument('--mu', type=float, default=0.7, help='friction coefficient')
    parser.add_argument('--size', type=int, default=100, help='Problem size (N as it will compute NxN matrix) ')
    parser.add_argument('positions', type=str, help='Geojson file containing positions with masses')

    with open(args.positions) as file:
        js=json.reads(file.read())
    attractors=Attractors(js)
    args = parser.parse_args()
    N=args.positions
    bitmap=[[Golem(x,y,args,attractors) for x in range(N)] for y in range(N)]
    # coś tutaj
    if allOD(bitmap[y][x].if_stop() for x in range(N)):
        colormap=[[bitmap[y][x].get_color() for ]
    

if __name__ == "__main__":
    main()
