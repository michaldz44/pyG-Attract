import argparse
import json
import sys
from golem import Golem
from attractors import Attractors
import Image



def main():
    parser = argparse.ArgumentParser(description='Gravitational attractors')
    parser.add_argument('--dt', type=float, default=0.05, help='timestep')
    parser.add_argument('--h', type=float, default=0.2, help='magic depth parameter - DO NOT CHANGE!!!!')
    parser.add_argument('--pot_d', type=float, default=0.005, help='potential diameter')
    parser.add_argument('--term_v', type=float, default=0.005, help='terminatig velocity')
    parser.add_argument('--mu', type=float, default=0.7, help='friction coefficient')
    parser.add_argument('--size', type=int, default=100, help='Problem size (N as it will compute NxN matrix) ')
    parser.add_argument('positions', type=str, help='Geojson file containing positions with masses')
    


    args = parser.parse_args()

    with open(args.positions) as file:
        js=json.reads(file.read())
    attractors=Attractors(js)

    N=args.positions
    # We choose points from [0,1]x[0,1] area
    # WE split it into NxN regoins (future pixels)
    # Each golem gets position according to pixel center which is
    golems=[Golem((i%N+0.5)/N,(i//N+0.5)/N,args,attractors) for i in range(N*N)]

    golems_functions=[golem.do_move for golem in golems]

    steps=0
    while any(golems_functions):
        golem_runnig=[golem_function() for golem_function in golems_functions]
        #no_of_golems_running=sum([1 for rg in golem_runnig if fg])
        steps+=1
        #if steps > step limit
        # break
    #

    img = Image.new( 'RGB', (N,N), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for i in range(N*N):    # for every pixel:
        pixels[i%N,i//N] = (i%N, i//N, golems[i].get_color()) # set the colour accordingly
    img.show()


if __name__ == "__main__":
    main()
