class BMW:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

    def show_details(self):
        return f"BMW Model: {self.model}, Horsepower: {self.horsepower} HP"

    def start_engine(self):
        return f"The {self.model}'s engine roars to life with a smooth hum!"

class Ferrari:
    def __init__(self, model, horsepower):
        self.model = model
        self.horsepower = horsepower

    def show_details(self):
        return f"Ferrari Model: {self.model}, Horsepower: {self.horsepower} HP"

    def start_engine(self):
        return f"The {self.model}'s engine starts with an exhilarating roar!"

def car_action(car):
    print(car.show_details())
    print(car.start_engine())

bmw_car = BMW("X5", 300)
ferrari_car = Ferrari("488 Spider", 670)

car_action(bmw_car)
print()  
car_action(ferrari_car)