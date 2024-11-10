import csv
import datetime
from email.headerregistry import Address

from unicodedata import normalize

from HashTable import HashTable
from Package import Package
from Truck import Truck

package_hash_table = HashTable()
packages = []
total_mileage = 0.0
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
            #print(f"Loaded package ID: {id_num}, Address: {address}")
                #  f", Status: {status}")
   # print(f"Total packages loaded : {sum(len(bucket) for bucket in hash_table.table)}")
   # print(hash_table)


def distance_between(a, b):
    distance = csv_distance[a][b]
    if distance == "":
        distance = csv_distance[b][a]

    return float(distance)

def address_lookup(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])




truck_1 = Truck(1, 16, 18,0.0,  [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=8),
                package_hash_table = package_hash_table)
truck_2 = Truck(2, 16, 18, 0.0, [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours = 10),
                package_hash_table= package_hash_table)
truck_3 = Truck(3, 16, 18, 0.0,  [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=11),
                package_hash_table = package_hash_table)

#truck_1_package_ids = [1, 13, 14, 15, 16]#19, 20, 29, 30, 31, 34, 37, 40]
#truck_2_package_ids = [3, 6, 10, 11, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38]
#truck_3_package_ids = [2, 4, 5, 7, 8, 9, 12, 17, 32, 33, 35, 39]


def load_packages_onto_truck(truck, package_ids, package_hash_table):
    for package_id in package_ids:
        package = package_hash_table.lookup(package_id)
        if package is not None:
            truck.packages.append(package)
           # print(f"Package ID {package_id} is loaded onto the truck {truck.truck_id}")
        else:
            print(f"Package {package_id} was not found in hash table for truck {truck.truck_id}")


def delivery(truck):
    undelivered = []
    truck.mileage = 0.0
    truck.address = "4001 South 700 East"

    for package_id in truck.package_ids:
        package = package_hash_table.lookup(package_id)
        if package is not None:

            undelivered.append(package)
        else:
            print(f"Package {package_id} not found in ht for truck {truck.truck_id}")
    truck.package_ids.clear()

    while undelivered:
        next_address = float("inf")
        next_package = None

        for package in undelivered:

            truck_index = address_lookup(truck.address)
            package_index = address_lookup(package.address)

            if truck_index is not None and package_index is not None:
                distance = distance_between(address_lookup(truck.address), address_lookup(package.address))
                if distance < next_address:

                    next_address = distance
                    next_package = package


        if next_package:
            truck.packages.append(next_package)
            undelivered.remove(next_package)
            truck.mileage += next_address
            truck.address = next_package.address
            truck.depart_time += datetime.timedelta(hours= next_address / truck.speed)
            next_package.delivery_time = truck.depart_time
            next_package.depart_time = truck.depart_time
        else:
            print("No valid package breaking loop")
            break


load_package("CSV/packages.csv", package_hash_table)
load_packages_onto_truck(truck_1, truck_1.package_ids, package_hash_table)

delivery(truck_1)

print(f" Truck {truck_1.truck_id} delivered packages: {[package.id_num for package in truck_1.packages]} ")
print(f"It took {truck_1.mileage} miles")

delivery(truck_2)
print(f" Truck {truck_2.truck_id} delivered packages: {[package.id_num for package in truck_2.packages]} ")
print(f"It took {truck_2.mileage} miles")

delivery(truck_3)
print(f" Truck {truck_3.truck_id} delivered packages: {[package.id_num for package in truck_3.packages]} ")
print(f"It took {truck_3.mileage} miles")
total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
print(total_mileage)
#print(package_hash_table)