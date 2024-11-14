from Package import Package
from HashTable import HashTable


class Truck:
    def __init__(self, truck_id, capacity, speed, weight, package_ids, mileage, address, depart_time, package_hash_table
                 ):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.weight = weight
        self.package_ids = package_ids
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.package_hash_table = package_hash_table
        self.packages = []

        for package_id in package_ids:
            package = package_hash_table.lookup(package_id)
            if package:
                self.packages.append(package)




package_hash_table = HashTable()


