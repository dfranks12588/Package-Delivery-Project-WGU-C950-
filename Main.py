import csv
import datetime
from email.headerregistry import Address

from HashTable import HashTable
from Package import Package
from Truck import Truck

package_hash_table = HashTable()
packages = []

with open("CSV/distances.csv") as distance_csv:
    csv_distance = csv.reader(distance_csv)
    csv_distance = list(csv_distance)

with open("CSV/addresses.csv") as address_csv:
    csv_address = csv.reader(address_csv)
    csv_address = list(csv_address)

with open("CSV/packages.csv") as package_csv:
    csv_package = csv.reader(package_csv)
    csv_package = list(csv_package)


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


def distance_between(a, b):
    distance = csv_distance[a][b]
    if distance == "":
        distance = csv_distance[b][a]

    return distance

def address_lookup(address):
    for row in csv_address:
        full_address = f"{row[1].strip()}, {row[2].strip()}"
        if address == full_address:
            print(f"Found address: {row[2]} with index {row[0]}")
            return int(row[0])
    print(f"Address {address} not found.")
    return None


truck_1 = Truck(1, 16, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours=8), package_hash_table)
truck_2 = Truck(2, 16, 18, [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours = 10), package_hash_table)
truck_3 = Truck(3, 16, 18, [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39],
                0.0, "Western Governors University, 4001 South 700 East", datetime.timedelta(hours=11), package_hash_table)

#truck_1_package_ids = [1, 13, 14, 15, 16]#19, 20, 29, 30, 31, 34, 37, 40]
#truck_2_package_ids = [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38]
#truck_3_package_ids = [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39]


def load_packages_onto_truck(truck, package_ids, package_hash_table):
    for package_id in package_ids:
        package = package_hash_table.lookup(package_id)
        if package is not None:
            truck.packages.append(package)
            #print(f"Package ID {package_id} is loaded onto the truck {truck.truck_id}")
        else:
            print(f"Package {package_id} was not found in hash table for truck {truck.truck_id}")

def delivery(trucks):
    undelivered_packages = trucks.packages.copy
    total_distance = 0.0
    current_location = address_lookup(trucks.start_location)
    current_time = trucks.depart_time

    while undelivered_packages:
        nearest_package = None
        nearest_distance = float("distance")

    for package in undelivered_packages:
        pass



#print(package_hash_table)

load_package("CSV/packages.csv", package_hash_table)



#printout_truck_load(truck_1)
#load_packages_onto_truck(truck_2, truck_2_package_ids, package_hash_table)
#load_packages_onto_truck(truck_3, truck_3_package_ids, package_hash_table)

#truck_1.deliver_packages(distance_matrix, address_dict)
for package_id in [1, 13, 14, 15, 16, 19, 20, 30, 31, 34, 37, 40]:
    result = package_hash_table.lookup(package_id)
    if result is None:
        print(f"Package ID {package_id} is not found")
   # else:
      #  print(f"Package ID {package_id} is successfully found")
#printout_truck_load(truck_1)
#truck_2.deliver_packages(distance_matrix, address_dict)

