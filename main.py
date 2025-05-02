def hotel_cost(night):
    return 140*nights
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    def rental_car_cost(days):
        if days>=7 : 
            return 40*days - 50
        elif days>=3 :
            return 40*days - 20
        else: