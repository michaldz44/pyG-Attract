import math

class Golem(object):
    def __init__(self, x, y, args, attractors):
        self.attractors=attractors
        self.args=args
        self.position=complex(x,y)
        self.velocity=complex(0,0)
        self.acceleration0=complex(0,0)
        self.acceleration1=complex(0,0)
        self.acceleration2=complex(0,0)
        self.vpredict=complex(0.0)
        self.final_attractor=None
        self.energy=self.get_energy()

    def move(self):
        # step
        dt=self.args.dt

        #dp=self.velocity*dt+(4.0*self.acceleration0-self.acceleration1)*dt**2

        if abs(self.velocity)==0:
            self.velocity=self.attractors.get_force(self.position,self.velocity)*dt
        else:
            v=abs(self.velocity)
            self.velocity+=self.attractors.get_force(self.position,self.velocity)*dt
            self.velocity=v*self.velocity/abs(self.velocity)

        self.position+=self.velocity*dt
        if (self.energy-self.attractors.get_potencial(self.position))>0:
            v=math.sqrt(2*(self.energy-self.attractors.get_potencial(self.position)))
        else:
            v=0
        self.velocity=v*self.velocity/abs(self.velocity)

        self.energy-=dt*self.args.mu*abs(self.velocity)**2

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
