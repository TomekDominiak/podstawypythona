class car:
    acceleration = 10

    def __init__(self, numer):
        self.numer = numer
        self.in_motion = False
        self.speed = 0

    def drive(self):
        self.in_motion = True

    def acceleration(self,acceleration):
        if self.in_motion
            self.speed += self.acceleration
        else:
            print("jest w ruchu")
            print()

    def stop(self):
        self.in_motion = False
        self.speed = 0

    def print_info(self):
        print(f"acceleration is {self.acceleration}")
        print(f"numer is {self.numer}")
        print(f'speed is {self.speed}')
        print(f'in motion {self.in_motion}')

audi=car("wpr123")
mercedes=car('wpr1234')
volvo=car("wpr12345")

audi.print_info()
volvo.print_info()
