class clashofclass:
    def __init__(self):
        self.data = {}
    
    def __setitem__(self,key,value):
        self.data[key] = value
        
    # def __getitem__(self,key):
    #     #  return self.data.get(key," is not existing")
    
    def __getitem__(self, key):
        return self.data.get(key, "Key not found")
               
    def __delitem__(self,key):
        if key in self.data:    
            print(f"{key} is deleting")
            del self.data[key]
        else:
            print(f"{key} not found")


obj = clashofclass()
obj ["name"] = "Divansh"
obj["age"] = 21

print(obj["name"])    
        
del obj["name"]

print(obj["name"])
