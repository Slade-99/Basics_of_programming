class Human:
    x = " yay"
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(self.name + " is walking" + self.y )

    def run(self):
        print(self.name + " is running")

    def talk(self):
        print(self.name + "is talking")

    def strength(self):
        print(self.name + " is strong")

    @staticmethod
    def play():
        print("Playing")


class Male(Human):
    y = "55"

    def talk(self):
        print(self.name + " is talking in low pitched voice" + self.x)

    def strength(self):
        print(self.name + " has great strength")

class Female(Human):

    def talk(self):
        print(self.name + " is talking in high pitched voice")

    def strength(self):
        print(self.name + " has futile strength")

    def reproduce(self):
        return True


Azwad = Male("Azwad")
Azwad.walk()
Azwad.strength()
Azwad.talk()

##Trajectory = Female("Trajectory")

#Trajectory.strength()
#x = Trajectory.reproduce()
#print(x)


#### To treat the methods in the class like a function . Use the @staticmethod  and do not use self and cannot use self. variables

Human.play()