#from Main import package_hash_table


class Truck:
    def __init__(self, truck_id, capacity, speed, package_ids, mileage, address, depart_time, package_hash_table):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.packages = []
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time

        for package_id in package_ids:
            package = package_hash_table.lookup(package_id)
            if package:
                self.packages.append(package)

    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
