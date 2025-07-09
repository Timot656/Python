class Dog:
    species = "Canis lupus familiaris"
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Species: {Dog.species}")
        print("-" * 30)
dog1 = Dog(name="Buddy", breed="Golden Retriever", age=3)
dog2 = Dog(name="Luna", breed="German Shepherd", age=5)

dog1.display_details()
dog2.display_details()