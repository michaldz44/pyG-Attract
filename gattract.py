import argparse
import json
import sys
from golem import Golem
from attractors import Attractors
import pickle


def main():
    parser = argparse.ArgumentParser(description='Gravitational attractors')
    parser.add_argument('--dt', type=float, default=0.0005, help='timestep')
    parser.add_argument('--h', type=float, default=0.1, help='magic depth parameter - DO NOT CHANGE!!!!')
    parser.add_argument('--pot_d', type=float, default=0.005, help='potential diameter')
    parser.add_argument('--term_v', type=float, default=0.005, help='terminatig velocity')
    parser.add_argument('--mu', type=float, default=0.7, help='friction coefficient')
    parser.add_argument('--size', type=int, default=10, help='Problem size (N as it will compute NxN matrix) ')
    parser.add_argument('--max_steps', type=int, default=False, help='Max steps that will occure (default run each terminated)')
    parser.add_argument('positions', type=str, help='Geojson file containing positions with masses')



    args = parser.parse_args()

    with open(args.positions) as file:
        js=json.loads(file.read())
    attractors=Attractors(js,args)

    N=args.size
    # We choose points from [0,1]x[0,1] area
    # WE split it into NxN regoins (future pixels)
    # Each golem gets position according to pixel center which is
    golems=[Golem((i%N+0.5)/N,(i//N+0.5)/N,args,attractors) for i in range(N*N)]

    for a in attractors.attractors:
        print(a["esc_energy"])
    print(attractors.get_potencial(complex(10000,10000)))

    golems_functions=[golem.do_move for golem in golems]
    golem_runnig=golems_functions

    steps=0
    positions_x=[]
    positions_y=[]
    number_to_view=10
    while any(golem_runnig):
        golem_runnig=[golem_function() for golem_function in golems_functions]
        no_of_golems_running=sum([1 for rg in golem_runnig if rg])
        print(
            repr(golems[number_to_view].position).ljust(43),
            repr(golems[number_to_view].get_energy()).ljust(20),
            repr(golems[number_to_view].energy).ljust(20),
            repr(no_of_golems_running).rjust(5)
        )
        positions_x.append(golems[10].position.real)
        positions_y.append(golems[10].position.imag)
        steps+=1
        if args.max_steps and args.max_steps < steps:
            break
    #

    try:
        #try:
        #    with open('data.pkl', 'rb') as input:
        #        golems = pickle.load(input)
        #except:
        #    pass

        from PIL import Image
        img = Image.new( 'RGB', (N,N), "black") # create a new black image
        pixels = img.load() # create the pixel map

        for i in range(N*N):    # for every pixel:
            color = golems[i].get_color()
            if color:
                pixels[i%N,i//N] = tuple(color) # set the colour accordingly
        img.show()
    except:
        with open('data.pkl', 'wb') as output:
            pickle.dump(golems, output, pickle.HIGHEST_PROTOCOL)

    try:
        #try:
        #    with open('data1.pkl', 'rb') as input:
        #        (positions_x,positions_y) = pickle.load(input)
        #except:
        #    pass

        import matplotlib.pyplot as plt
        plt.plot(positions_x,positions_y)
        for at in attractors.attractors:
            plt.plot([at["position"].real],[at["position"].imag],'r*')
        plt.show()
    except:
        with open('data1.pkl', 'wb') as output:
            pickle.dump((positions_x,positions_y), output, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    main()
