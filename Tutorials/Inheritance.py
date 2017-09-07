class Anim:
    def __init__(self,first_name):
        self.first_name = first_name
    def swim(self):
        print("Varssdan")

class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Trout(Anim,Fish):
    def __init__(self,first_name):
        super().swim(Fish)
        self.eyelids="Vardan"
        self.first_name=first_name

terry = Trout("Terry")
#print(terry.first_name + " ")# + terry.last_name)
#print(terry.skeleton)
#terry.swim_backwards()

#Multiple inheritance is possible in python
