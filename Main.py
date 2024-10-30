import csv


from HashTable import HashTable
from Package import Package
from Truck import Truck

package_hash_table = HashTable()
packages = []
address_dict = {}
address_list = []
distance_matrix = []

def load_package(file_name, hash_table):
    with open(file_name, mode='r') as pack_file:
        csv_reader = csv.reader(pack_file)
        next(csv_reader)
        for row in csv_reader:
            address_id = address_dict.get(row[1].strip())
            package_id = int(row[0])
            package = Package(
                id_num = package_id,
                address = row[1],
                city = row[2],
                state = row[3],
                zip = row[4],
                deadline = row[5],
                weight = row[6],
                status = row[7]
            )
            package.address_id = address_id
            packages.append(package)
            hash_table.insert(package_id, package)


def load_distance(file_name):
    with open(file_name, mode='r') as distance_file:
        csv_reader = csv.reader(distance_file)
        for row in csv_reader:
            distance_row = []
            for distance in row:
                try:
                    distance_row.append(float(distance) if distance.strip() else 0.0)
                except ValueError:
                    print("Error")
                    distance_row.append(0.0)
            distance_matrix.append(distance_row)


def load_address(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = list(csv.reader(csv_file))
        for row in csv_reader:
            index = int(row[0].strip())
            address_name = row[1].strip()
            address_full = f"{address_name}, {row[2].strip()}"
            address_dict[address_full] = index
            address_list.append(address_full)
            #print(f"Loaded address '{address_full} with the index {index}")



def address_lookup(address):
    return address_dict.get(address, None)

load_package("CSV/packages.csv", package_hash_table)
load_address("CSV/addresses.csv")
load_distance("CSV/distances.csv")

#address_test = address_lookup("Western Governors University, 4001 South 700 East")
#package_test = package_hash_table.lookup(1)
#print(address_test)
#print(distance_matrix[:3])
#print(package_test)

truck_1 = Truck(1)
truck_1.load_package(packages[0])
truck_2 = Truck(2)
truck_3 = Truck(3)

def printout_truck_load(truck):
    for package in truck.packages:
        print(f"Package {package.id} to {package.address}")

printout_truck_load(truck_1)
