class animal:
    
    def __init__(self,name):
        self.name = name
			
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

class predator(animal):
        def hunt(self):
            print(f"{self.name} is hunting")

class pray(animal):
        def flee(self):
            print(f"{self.name} is fleeing")

class fish(pray):
        pass

class hawk(predator):
        pass

class dog(pray,predator):
        pass

fish = fish("vail")
hawk = hawk("whoh")
dog = dog("vhooo")
fish.sleep()
