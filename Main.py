import csv
import datetime
from HashTable import HashTable
from Package import Package
from Truck import Truck

package_hash_table = HashTable()

with open("CSV/distances.csv", encoding="utf-8-sig") as distance_csv:
    csv_distance = csv.reader(distance_csv)
    csv_distance = list(csv_distance)


with open("CSV/packages.csv", encoding="utf-8-sig") as package_csv:
    csv_package = csv.reader(package_csv)
    csv_package = list(csv_package)


with open ("CSV/addresses.csv") as address_csv:
    csv_address = csv.reader(address_csv)
    csv_address = list(csv_address)



def load_package(file_name, hash_table):
    with open(file_name, mode='r', encoding="utf-8-sig") as pack_file:
        csv_reader = csv.reader(pack_file)
        for row in csv_reader:
            id_num = int(row[0].strip())
            address = row[1].strip().title()
            city = row[2].strip().title()
            state = row[3].strip().upper()
            zip = row[4].strip()
            deadline = row[5].strip()
            weight = row[6]
            status = row[7]

            package = Package(id_num, address, city, state, zip, deadline, weight, status)
            hash_table.insert(id_num, package)

def address_lookup(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])

def distance_between(a, b):
    distance = csv_distance[a][b]
    if distance == "":
        distance = csv_distance[b][a]
    return float(distance)

truck_1 = Truck(1, 16, 18,0.0,  [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=8))
truck_2 = Truck(2, 16, 18, 0.0, [3, 6, 10, 11, 12, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours =9, minutes=5))
truck_3 = Truck(3, 16, 18, 0.0,  [2, 4, 5, 7, 8, 9, 17, 32, 33, 35, 39],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=11))

def delivery(truck):
    undelivered = []
    truck.address = "4001 South 700 East"

    for package_id in truck.package_ids:
        package = package_hash_table.lookup(package_id)
        distance = distance_between(address_lookup(truck.address), address_lookup(package.address))
        undelivered.append((distance, package))

    #undelivered.sort(key=lambda x: x[0])
    truck.package_ids.clear()

    while undelivered:


        next_package = min(undelivered, key=lambda  x:x[0])
        undelivered.remove(next_package)

        distance, next_package = next_package
        next_address = distance_between(address_lookup(truck.address), address_lookup(next_package.address))

        truck.mileage += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / truck.speed)

        next_package.delivery_time = truck.time
        next_package.depart_time = truck.depart_time

        """print(f"Delivered package {next_package.id_num} to {next_package.address}")
        print(f"Truck mileage: {truck.mileage:.2f} miles")
        print(f"Delivery time: {truck.time}")
        print(f"Truck's new address: {truck.address}")"""

        undelivered = [(distance_between(address_lookup(truck.address), address_lookup(pack.address)), pack)
                       for distance, pack in undelivered]


load_package("CSV/packages.csv", package_hash_table)


delivery(truck_1)
delivery(truck_2)
delivery(truck_3)
total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage


def print_delivery_times():
    print("Delivery time for all packages:")
    for package_id in range(1, len(package_hash_table.table) +1):
        package = package_hash_table.lookup(package_id)
        if package:
            print(f"Package {package.id_num} delivered at {package.delivery_time}")
print_delivery_times()


"""print(f"The total mileage of all trucks is: {total_mileage}")
print(f"Truck 1's total mileage is: {truck_1.mileage}")
print(f"Truck 2's total mileage is: {truck_2.mileage}")
print(f"Truck 3's total mileage is: {truck_3.mileage}")"""

def user_interface():
    print(f"The total mileage of all trucks is: {total_mileage}")
    while True:
        print("To see the status of all packages at a given time, enter '1'")
        print("To see the status of a certain package at a given time, enter '2'")
        print("To exit, enter '3'")
        user_input = input("Please select an option (1/2/3): ")

        if user_input == "1":

            try:
                time_input = input("Please enter a time to check the status "
                                   "of all packages in the following format: HH:MM:SS ")
                (hours, minutes, seconds) = time_input.split(":")
                converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
                print(f"Status of all packages at {converted_time}")
                for package_id in range(1, len(package_hash_table.table) +1):
                    package = package_hash_table.lookup(package_id)
                    package.status_update(converted_time)
                    print(f"Package {package_id} status at {converted_time} : {package.status}")

            except ValueError:
                print("Invalid input, please try again")



        elif user_input == "2":
            package_id = input("Enter a package ID to check its status: ")

            try:
                package = package_hash_table.lookup(int(package_id))

                if package:
                    package_time = input(f"Enter a time you wish to check {package_id}'s status (HH:MM:SS)")

                    try:
                        (hours, minutes, seconds) = package_time.split(":")
                        converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
                        package.status_update(converted_time)
                        print(f"Package {package_id} status at : {package.status}")

                    except ValueError:
                        print("Invalid time format, please enter time as HH:MM:SS")

                else:
                    print(f"Package {package_id} not found")


            except ValueError:
                print("Please enter a valid package ID.")

        elif user_input == "3":
            print("Exiting...")
            return

        else:
            print("Invalid choice, please select 1, 2, or 3.")
user_interface()






