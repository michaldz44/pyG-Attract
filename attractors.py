import math,pdb
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

        c=250
        for attractor1 in self.attractors:
            energy=[]
            for attractor2 in self.attractors:
                if attractor1==attractor2:
                    continue
                v=(attractor2["position"]-attractor1["position"]) /c
                m=max([self.get_potencial(attractor1["position"]+v*linspace) for linspace in range(1,c)])
                energy.append(m)
            attractor1["esc_energy"]=min(energy)-(1/c)*min(energy)

    def get_force(self,position,velocity):
        list_of_potentialsMG=[]
        h=self.args.h
        for attractor in self.attractors:
            absz = abs(attractor["position"]-position)
            versor = (attractor["position"]-position) / (absz)
            component = (versor*attractor["mass"])/math.pow(absz*absz+h*h,1.5)

            list_of_potentialsMG.append(component)
        sum_of_potentials = sum(list_of_potentialsMG)

        return (-self.args.mu*velocity) + sum_of_potentials

    def get_potencial(self,position):
        list_of_potentialsMG=[]
        h=self.args.h
        for attractor in self.attractors:
            absz = abs(attractor["position"]-position)
            #if absz>0.00001:
            try:
                component = 1/h+(-attractor["mass"])/math.sqrt(absz*absz+h*h)
            except:
                pdb.set_trace()
            #else:
            #    component = 1/h
            list_of_potentialsMG.append(component)
        sum_of_potentials = sum(list_of_potentialsMG)

        return  sum_of_potentials

    def min_distance(self,position):
        return min([abs(position-attractor["position"]) for attractor in self.attractors])

    def min_attractor(self,position):
        return min([{
                "distance":abs(position-attractor["position"]),
                "attractor":attractor
                } for attractor in self.attractors],key=lambda x:x["distance"])["attractor"]
