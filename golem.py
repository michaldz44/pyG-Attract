class Golem(object):
    def __init__(self x, y, args, attractors):
        self.attractors=attractors
        self.args=args
        self.position=complex(x,y)
        self.velocity=complex(0,0)
        self.acceleration0=complex(0,0)
        self.acceleration1=complex(0,0)
        self.acceleration2=complex(0,0)
        self.vpredict=complex(0.0)

    def move(self):
        dt=self.args.dt
        dt=self.velocity*dt+(4.0*self.acceleration0-self.acceleration1)*dt**2
        self.position+=dt
        self.vpredict = self.velocity+ (3.0*self.acceleration0 - self.acceleration1)*dt/2.0
        self.acceleration2 += self.attractors.get_force(x,y)

    def do_move(self):
        if self.end():
            return self.do_move
        else:
            return None

    def end(self):
        
