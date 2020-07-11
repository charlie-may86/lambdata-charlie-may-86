from pdb import set_trace as breakpoint

class Dog():
    def __init__(self, name, age, housebroke, bread):
        self.name = name
        self.age = age
        self.housebroke = housebroke
        self.bread = bread
    

    def is_housebroke(self):
        if self.housebroke == True:
            print(f'{self.name} is a good pup')
        else:
            print(f'{self.name} needs work')


class Beagle(Dog):
    pass


if __name__ == '__main__':
    
    lucky = Dog('Lucky', 2, True, 'Beagle')
    breakpoint()