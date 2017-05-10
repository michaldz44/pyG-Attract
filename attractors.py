class Attractors(object):
    def __init__(self,js, args):
        assert js["type"]=="FeatureCollection"
        assert "features" in js

        self.attractors=[]
        self.args = args


        for feature in js["features"]:
            assert "geometry" in feature
            assert "properties" in feature
            assert "MASS" in feature["properties"]
            assert feature["geometry"]["type"]=="Point"

            self.attractors.append({
                "mass":feature["properties"]["MASS"],
                "color":feature["properties"]["COLOR"],
                "position":complex(*feature["geometry"]["coordinates"])
            })

    #def distances_list(self,position):
    #    return

    def get_force(self,position,velocity):
        list_of_potentialsMG=[]
        for attractor in self.attractors:
            absz = abs(attractor["position"]-position)
            versor = (attractor["position"]-position) / (absz)

            component = attractor["mass"]/(absz**2+self.args.h**2)*versor/(absz**2+self.args.h**2)**(0.5)
            list_of_potentialsMG.append(component)
        sum_of_potentials = sum(list_of_potentialsMG)

        return -self.args.mu*velocity + sum_of_potentials


        #powiniein zwracac sile o wlasciwym kierunku i zwrocie
     #   return -sum([attractor["mass"]/(position-attractor["position"])*abs(position-attractor["position"]) for attractor in  self.attractors])
       # return




    def min_distance(self,position):
        return min([abs(position-attractor["position"]) for attractor in self.attractors])

    def min_attractor(self,position):
        return min([{
                "distance":abs(position-attractor["position"]),
                "attractor":attractor
                } for attractor in self.attractors],key=lambda x:x["distance"])["attractor"]
