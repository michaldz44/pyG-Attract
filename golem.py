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

    def move(self):
        dt=self.args.dt
        dp=self.velocity*dt+(4.0*self.acceleration0-self.acceleration1)*dt**2
        self.position+=dp
        self.vpredict = self.velocity+ (3.0*self.acceleration0 - self.acceleration1)*dt/2.0
        self.acceleration2 += self.attractors.get_force(self.position,self.vpredict)

        self.acceleration2 += self.position - self.args.mu*self.vpredict
        self.velocity += (2.0*self.acceleration2+5.0*acceleration0 - acceleration1)*dt/6.0
        self.acceleration1 = self.acceleration0
        self.acceleration0 = acceleration2



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

        if self.attractors.min_distance(self.position) < self.args.pot_d and abs(self.velocity) < self.args.term_v: # close to the city and low velocity
            self.final_attractor=self.attractors.min_attractor(self.position)
            return True
        return False
