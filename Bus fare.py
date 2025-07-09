class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def display_info(self):
        return f"Vehicle Name: {self.name}, Capacity: {self.capacity}"


class Bus(Vehicle):
    def __init__(self, name, capacity, fare_per_person):
        super().__init__(name, capacity)
        self.fare_per_person = fare_per_person

    def calculate_total_fare(self, passengers):
        if passengers > self.capacity:
            return "Error: Number of passengers exceeds bus capacity!"
        total_fare = passengers * self.fare_per_person
        return f"Total Fare: ${total_fare}"

school_bus = Bus("School Bus", 50, 2.5)
print(school_bus.display_info())  
print(school_bus.calculate_total_fare(40))   
print(school_bus.calculate_total_fare(60))  
