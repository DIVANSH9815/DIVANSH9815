class animal:
    alive = True
    
class dog(animal):
     def speak(self):
         print("whoo")

class cat(animal):
    def speak(self):
        print("meon")

class car:
    
    alive = False
    def speak(self):
        print("bhooo")

animals = [dog(),cat(),car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
