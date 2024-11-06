import csv
import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck

package_hash_table = HashTable()
packages = []
address_dict = {}
address_list = []
distance_matrix = []

def load_package(file_name, hash_table):
    #print("Loading packages...")
    with open(file_name, mode='r') as pack_file:
        csv_reader = csv.reader(pack_file)
        for row in csv_reader:
            id_num = int(row[0])
            address = row[1].strip().title()
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            weight = row[6]
            status = row[7]

            p = Package(id_num, address, city, state, zip, deadline, weight, status)
            #print(f"Creating package ID: {id_num}, Address ID: {address}")
            hash_table.insert(id_num, p)
            #print(f"Loaded package ID: {id_num}, Address: {address}"
                #  f", Status: {status}")
   # print(f"Total packages loaded : {sum(len(bucket) for bucket in hash_table.table)}")
   # print(hash_table)



def load_distance(file_name):
    with open(file_name, mode='r') as distance_file:
        csv_reader = csv.reader(distance_file)
        for row in csv_reader:
            distance_row = []
            for distance in row:
                try:
                    distance_row.append(float(distance) if distance.strip() else 0.0)
                except ValueError:
                    print("Error converting distance")
                    distance_row.append(0.0)
            distance_matrix.append(distance_row)


def load_address(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = list(csv.reader(csv_file))
        for row in csv_reader:
            index = int(row[0].strip())
            address_name = row[1].strip()
            street_address = row[2].strip()
            address_full = f"{address_name.lower().strip().title()}, {street_address.lower().strip().title()}"
            address_dict[address_full] = index
            address_list.append(address_full)
            #print(f"Loaded address '{address_full} with the index {index}")


def address_lookup(address):
    return address_dict.get(address, None)

#truck_id, capacity, speed, package_id, mileage, address, depart_time
truck_1 = Truck(1, 16, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours=8), package_hash_table)
truck_2 = Truck(2, 16, 18, [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours = 10), package_hash_table)
truck_3 = Truck(3, 16, 18, [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours=11), package_hash_table)

truck_1_package_ids = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck_2_package_ids = [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38]
truck_3_package_ids = [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39]
def printout_truck_load(truck):
    for package in truck.packages:
        print(f"Package {package.id_num} to {package.address}")

def load_packages_onto_truck(truck, package_ids, package_hash_table):
    for package_id in package_ids:
        package = package_hash_table.lookup(package_id)
        if package is not None:
            truck.packages.append(package)
            #print(f"Package ID {package_id} is loaded onto the truck {truck.truck_id}")
        else:
            print(f"Package {package_id} was not found in hash table for truck {truck.truck_id}")




#print(package_hash_table)
load_address("CSV/addresses.csv")
load_package("CSV/packages.csv", package_hash_table)
load_distance("CSV/distances.csv")

load_packages_onto_truck(truck_1, truck_1_package_ids, package_hash_table)
#printout_truck_load(truck_1)
#load_packages_onto_truck(truck_2, truck_2_package_ids, package_hash_table)
#load_packages_onto_truck(truck_3, truck_3_package_ids, package_hash_table)

truck_1.deliver_packages(distance_matrix, address_dict)
for package_id in [1, 13, 14, 15, 16, 19, 20, 30, 31, 34, 37, 40]:
    result = package_hash_table.lookup(package_id)
    if result is None:
        print(f"Package ID {package_id} is not found")
   # else:
      #  print(f"Package ID {package_id} is successfully found")
printout_truck_load(truck_1)
#truck_2.deliver_packages(distance_matrix, address_dict)

