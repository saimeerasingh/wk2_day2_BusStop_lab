
class BusStop:
    def __init__(self,stop_name):
        self.stop_name = stop_name
        self.queue = []

    def add_to_queue(self,person):
        
        self.queue.append(person)

    def remove_from_queue(self,person):
        self.queue.remove(person)

