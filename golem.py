import math
import pdb

class Golem(object):
    def __init__(self, x, y, args, attractors,golem_number):
        self.attractors=attractors
        self.args=args
        self.position=complex(x,y)
        self.velocity=complex(0,0)
        #self.acceleration_previous=self.attractors.get_force(self.position,self.velocity)
        self.acceleration_previous=0
        self.final_attractor=None
        self.energy=self.get_energy()
        self.golem_number=golem_number
        self.state=[]

    def move(self):
        # step
        absv=abs(self.velocity)
        if absv>1:
            dt=self.args.dt*1/(absv)
        else:
            dt=self.args.dt
        acceleration_current=self.attractors.get_force(self.position,self.velocity)

        # let's ty to be accurate apply Beeman-Schofield algoritm
        #
        # position=\
        #     self.position+\
        #     self.velocity*dt+\
        #     dt*dt*(4*acceleration_current-self.acceleration_previous)/6.0
        #
        # v_predict=\
        #     self.velocity+\
        #     dt*(3*acceleration_current-self.acceleration_previous)/2.0
        #
        # acceleration_future=self.attractors.get_force(position,v_predict)
        #
        # self.velocity+=dt*(2*acceleration_future+5*acceleration_current-self.acceleration_previous)/6.0
        #
        # self.acceleration_previous=acceleration_current
        # self.position=position

        # Euler-Cromer fast simplified version
        self.velocity+=acceleration_current*dt
        self.position+=self.velocity*dt

        if (self.energy-self.attractors.get_potencial(self.position))>0:
            v=math.sqrt(2*(self.energy-self.attractors.get_potencial(self.position)))
        else:
            print("drag problem  - velocity anihilated",self.golem_number,abs(self.velocity))
            if abs(self.velocity)>0.1:
                pdb.set_trace()
            v=0.000001
            #v=-math.sqrt(-2*(self.energy-self.attractors.get_potencial(self.position)))

        absv=abs(self.velocity)
        self.velocity=v*self.velocity/absv
        #self.q=v/absv
        self.energy-=dt*self.args.mu*absv*absv
        #
        # self.state.append((
        #     abs(self.velocity),
        #     self.attractors.get_potencial(self.position),
        #     self.energy,
        #     dt
        # ))

        #self.vpredict = self.velocity+ (3.0*self.acceleration0 - self.acceleration1)*dt/2.0
        #self.acceleration2 += self.attractors.get_force(self.position,self.vpredict)

        #self.acceleration2 += self.position - self.args.mu*self.vpredict
        #self.velocity += (2.0*self.acceleration2+5.0*self.acceleration0 - self.acceleration1)*dt/6.0
        #self.acceleration1 = self.acceleration0
        #self.acceleration0 = self.acceleration2


    def get_energy(self):
        #print(self.attractors.get_potencial(self.position))
        return self.attractors.get_potencial(self.position)+abs(self.velocity)**2/2.0


    def do_move(self):
        if self.final_attractor:
            return False
        self.move()
        self.end_check()
        return True

    def get_color(self):
        if self.final_attractor:
            return self.final_attractor["color"]

    def end_check(self):
        # if final attrator is set we are fixed (attracted)

        if self.attractors.min_distance(self.position) < self.args.pot_d and abs(self.velocity) < self.args.term_v:  # close to the city and low velocity
            self.final_attractor=self.attractors.min_attractor(self.position)
            return True
        if self.energy<self.attractors.min_attractor(self.position)["esc_energy"]:
            self.final_attractor=self.attractors.min_attractor(self.position)
            return True
        return False
