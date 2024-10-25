import csv


from HashTable import HashTable
from Package import Package

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

load_package("CSV/packages.csv", package_hash_table)
#package_test = package_hash_table.lookup(5)
#print(package_test)



def load_distance(file_name):
    with open(file_name, mode='r') as distance_file:
        csv_reader = csv.reader(distance_file)
        for row in csv_reader:
            distance_row = [float(distance) if distance.strip() else 0.0 for distance in row]
            distance_matrix.append(distance_row)

load_distance("CSV/distances.csv")
print(distance_matrix)


def load_address(file_name):
    with open(file_name, mode='r') as csv_file:
        csv_reader = list(csv.reader(csv_file))
        for index, row in enumerate(csv_reader):
            address = row[0].strip()
            address_dict[address] = index
            address_list.append(address)

def address_lookup(address):
    return address_dict.get(address, None)

load_address("CSV/addresses.csv")
address_test = address_lookup("Sugar House Park,1330 2100 S")
print(address_test)



