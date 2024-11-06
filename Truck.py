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

    def calculate_distance(self, from_address, to_address, distance_matrix, address_dict):
        from_address_normalized = from_address.lower().strip()
        to_address_normalized = to_address.lower().strip()

        full_from_address = next((full_address for full_address in address_dict if from_address_normalized
                                  in full_address.lower()), None)
        full_to_address = next((full_address for full_address in address_dict if to_address_normalized
                                in full_address.lower()), None)

        from_address_index = list(address_dict.keys()).index(full_from_address)
        to_address_index = list(address_dict.keys()).index(full_to_address)
        if not full_from_address:

            raise ValueError(f"Address '{from_address_normalized} not found in address_dict keys")
        if not full_to_address:
            raise ValueError(f"Address '{to_address_normalized} not found in address_dict keys")

        distance = distance_matrix[from_address_index][to_address_index]

        print(f"Distance: {distance} miles")
        return distance


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
            print(f"Delivering package {nearest_package.id_num} to {nearest_package.address} that travels "
                  f"{distance}")

        print(f"Total distance: {total_distance} traveled by Truck {self.truck_id}")

    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
package_hash_table = HashTable()


