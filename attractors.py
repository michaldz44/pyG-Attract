class Attractors(object):
    def __init__(self,js):
        assert js["type"]=="FeatureCollection"
        assert "features" in js

        self.attractors_positions=[]


        for feature in js["features"]:
            assert "geometry" in feature
            assert "properties" in feature
            assert "MASS" in feature["properties"]
            assert feture["geometry"]["type"]=="Point"

            self.attractors_positions.append({
                "mass":feature["properties"]["MASS"],
                "color":feature["properties"]["COLOR"],
                "position":complex(*feature["geometry"]["coordinates"])
            })

    #def distances_list(self,position):
    #    return

    def get_force(self,position):
        return sum([attractor["mass"]/abs(position-attractor["position"])**(2) for attractor in  self.attractors])

    def min_distance(self,position):
        return min([abs(position-attractor["position"]) for attractor in self.attractors])

    def
