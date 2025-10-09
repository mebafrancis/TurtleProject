class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_fins=2

    def swim(self):
        print("moving in water")

    def breathe(self):
        super().breathe()
        print("doing this underwater")

nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)
print(nemo.num_fins)