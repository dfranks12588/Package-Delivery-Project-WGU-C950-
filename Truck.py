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
            #else:
            #    print(f" Package id {package_id} not found in hashtable")
      #  print(f"Truck {truck_id} has {len(self.packages)} loaded packs")

    def calculate_distance(self, from_address, to_address, distance_matrix, address_dict):
        print(f"Checking distances from {from_address} and to: {to_address}")
        full_from_address = address_dict.get(from_address)
        full_to_address = address_dict.get(to_address)

        if full_from_address is None:
            raise ValueError("You goofed with from_address")
        if full_to_address is None:
            raise ValueError("You goofed with to_address")

        return distance_matrix[full_from_address][full_to_address]

    def deliver_packages(self, distance_matrix, address_dict):
        current_location = self.address
        total_distance = 0.0

        print(f"Beginning delivery from {current_location} with {len(self.packages)} packages")


        while self.packages:
            nearest_package = min(
                self.packages,
                key = lambda pack: self.calculate_distance(current_location, pack.address,
                                                           distance_matrix, address_dict)
            )
            distance = self.calculate_distance(current_location, nearest_package.address
                                               , distance_matrix, address_dict)
            total_distance += distance
            self.mileage += distance
            current_location = nearest_package.address
            self.packages.remove(nearest_package)
            print(f"Delivering package{nearest_package.id_num} to {nearest_package.address} that travels "
                  f"{distance}")

        print(f"Total distance: {total_distance} traveled by Truck {self.truck_id}")

    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
    package_hash_table = HashTable()


