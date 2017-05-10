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
        self.acceleration2 += self.attractors.get_force(self.position)

    def do_move(self):
        if self.end():
            return self.do_move
        else:
            return None

    def end(self):
        if self.attractors.min_distance(self.position) < self.args.pot_d and abs(self.velocity) < self.args.term_v: # close to the city and low velocity
            return True




         if(((min < magnetSize)&&(sqrt(vx*vx+vy*vy)<abortVel))) // blisko i mala predkosc
							run = 0;
					   if((sqrt(vx*vx+vy*vy)<minimalVel)&&(ct > minSteps)) // mala predkosc, wykonano duzo krokow, ale dalej niz magnet size
							run = 0;
					   if(ct > maxSteps) // jezeli daleko i duza predkosc przez amplitude white noise
							run = 0;
