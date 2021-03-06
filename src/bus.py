from unittest.signals import registerResult

from src.bus_stop import BusStop


class Bus:
    def __init__(self,route_number,destination,price,capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers = []
    def route_number(self):
        return self.route_number

    def destination(self):
        return self.destination

    def price(self):
        return self.price

    def capacity(self):
        return self.capacity

    def pick_up(self,person):
        self.passengers.append(person)
        return len(self.passengers)

    def drop_off(self,person):
        self.passengers.remove(person)
        return len(self.passengers)

    def empty(self):
        self.passengers.clear()
        return len(self.passengers)




    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def remaining_capacity(self):
        return self.capacity - len(self.passengers)
    
    def pick_up_from_stop(self,person):
        BusStop.add_to_queue(person)

    
