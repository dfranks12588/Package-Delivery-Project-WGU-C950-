from Package import Package
from HashTable import HashTable


class Truck:
    def __init__(self, truck_id, capacity, speed, package_ids, mileage, address, depart_time, package_hash_table):
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.package_ids = package_ids
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.package_hash_table = package_hash_table
        self.packages = []

        #print(f"Initializing Truck {self.truck_id} with package ids: {self.package_ids}")
        for package_id in package_ids:
            package = package_hash_table.lookup(package_id)
            if package:
                self.packages.append(package)
                #print(f"Loaded package {package.id_num} for truck {self.truck_id}")

      #  print(f"Truck {truck_id} has {len(self.packages)} loaded packs")




    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
package_hash_table = HashTable()


