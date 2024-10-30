class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.packages = []
       # self.current_location = 0
       # self.distance_traveled = 0.0

    def load_package(self, package):
        self.packages.append(package)

    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
