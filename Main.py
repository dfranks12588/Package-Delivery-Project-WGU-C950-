import csv
import datetime
from HashTable import HashTable
from Package import Package
from Truck import Truck
#Daniel Franks WGU C950 Student ID: 006310287

# Creates an instance of the hash table
package_hash_table = HashTable()

#Opens two CSV files for later use using the csv library
with open("CSV/distances.csv", encoding="utf-8-sig") as distance_csv:
    csv_distance = csv.reader(distance_csv)
    csv_distance = list(csv_distance)


with open ("CSV/addresses.csv") as address_csv:
    csv_address = csv.reader(address_csv)
    csv_address = list(csv_address)

#Loads the package details onto the hash table with the .insert function
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

#Alters the delivery address of package #9 at the time WGUPS is notified of the change
    package_9 = hash_table.lookup(9)
    if package_9:
        package_9.address = "410 S State St"
        package_9.city = "Salt Lake City"
        package_9.state = "UT"
        package_9.zip = "84111"
        package_9.corrected_time = datetime.timedelta(hours=10, minutes=20)


#Reads the addresses from the csv_address and returns the ID which is at index 0
def address_lookup(address):
    for row in csv_address:
        if address in row[2]:
            return int(row[0])

#Retrieves the distance between two locations from the csv_distance table
def distance_between(a, b):
    distance = csv_distance[a][b]
    if distance == "":
        distance = csv_distance[b][a]
    return float(distance)

#Manually loads the trucks in accordance with the package restrictions
truck_1 = Truck(1, 16, 18,0.0,  [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=8))
truck_2 = Truck(2, 16, 18, 0.0, [3, 6, 10, 11, 12, 18, 21, 22, 23, 24, 25, 26, 27, 28, 36, 38],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours =9, minutes=5))
truck_3 = Truck(3, 16, 18, 0.0,  [2, 4, 5, 7, 8, 9, 17, 32, 33, 35, 39],
                0.0, "4001 South 700 East", depart_time=datetime.timedelta(hours=11))

#Simulates the deliveries of the packages assigned to trucks using the truck object parameter
def delivery(truck):
    undelivered = []
    truck.address = "4001 South 700 East"

# Calculates the distance for all packages on the truck
    for package_id in truck.package_ids:
        package = package_hash_table.lookup(package_id)
        distance = distance_between(address_lookup(truck.address), address_lookup(package.address))
        undelivered.append((distance, package))

# Clears the truck package list after all packages are loaded onto undelivered
    truck.package_ids.clear()

    while undelivered:
# Finds the packages with the shortest distance and remove it from undelivered
        next_package = min(undelivered, key=lambda  x:x[0])
        undelivered.remove(next_package)
# Get the distance and package details
        distance, next_package = next_package
        next_address = distance_between(address_lookup(truck.address), address_lookup(next_package.address))

# Update the truck milage, address, and time
        truck.mileage += next_address
        truck.address = next_package.address
        truck.time += datetime.timedelta(hours=next_address / truck.speed)

# Update the package delivery details
        next_package.delivery_time = truck.time
        next_package.depart_time = truck.depart_time

# Re-calculate the distance for the other remaining packages
        undelivered = [(distance_between(address_lookup(truck.address), address_lookup(pack.address)), pack)
                       for distance, pack in undelivered]

# Calls the load package function
load_package("CSV/packages.csv", package_hash_table)

# Assigns truck ID's to package for the user interface
for package_id in truck_1.package_ids:
    package = package_hash_table.lookup(package_id)
    if package:
        package.truck_id = truck_1.truck_id
for package_id in truck_2.package_ids:
    package = package_hash_table.lookup(package_id)
    if package:
        package.truck_id = truck_2.truck_id
for package_id in truck_3.package_ids:
    package = package_hash_table.lookup(package_id)
    if package:
        package.truck_id = truck_3.truck_id
# Calls the delivery function to simulate delivery with each of three trucks
delivery(truck_1)
delivery(truck_2)
delivery(truck_3)

# Calculates the total mileage
total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage

# Terminal window user interface function
def user_interface():
    # Prints out total mileage and gives user three initial options and loops continuously until the user exits.
    print(f"The total mileage of all trucks is: {total_mileage:.2f}")
    while True:
        print("To see the status of all packages at a given time, enter '1'")
        print("To see the status of a certain package at a given time, enter '2'")
        print("To exit, enter '3'")
        user_input = input("Please select an option (1/2/3): ")

        if user_input == "1":
        # If "1" is entered, allows user to enter a time to see the delivery status of all packages
            try:
                time_input = input("Please enter a time to check the status "
                                   "of all packages in the following format: HH:MM:SS ")
                # Converts user input into the correct format for comparison
                (hours, minutes, seconds) = time_input.split(":")
                converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

                # Loops through all packages in the hash table to display the status
                print(f"Status of all packages at {converted_time}")
                for package_id in range(1, len(package_hash_table.table) +1):
                    package = package_hash_table.lookup(package_id)

                    # Special handling for package 9 which has a corrected address after 10:20:00
                    if package.id_num == 9 and converted_time >= package.corrected_time:
                        package.address = package.corrected_address

                    package.status_update(converted_time)
                    print(f"Package {package_id} status at {converted_time} : {package.status}")

            # Only prints out if user entered something other than the correct format of HH:MM:SS
            except ValueError:
                print("Invalid input, please try again")


        elif user_input == "2":
        # Option 2 displays the status of a particular package at a user chosen time

            package_id = input("Enter a package ID to check its status: ")

            try:
            # Uses the lookup function from the hash table by package ID
                package = package_hash_table.lookup(int(package_id))

                if package:
                    package_time = input(f"Enter a time you wish to check {package_id}'s status (HH:MM:SS)")

                    try:
                        (hours, minutes, seconds) = package_time.split(":")
                        converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

                        # Updates and displays package status
                        package.status_update(converted_time)
                        print(f"Package {package_id} status at : {package.status}")

                        # Checks if the package was delivered at the specific time
                        if package.delivery_time is not None and converted_time >= package.delivery_time:
                            print(f"Package {package_id} was delivered to {package.address} at {package.delivery_time}")
                        else:
                            print(f"Package {package_id} has not been delivered yet.")
                    except ValueError:
                        print("Invalid time format, please enter time as HH:MM:SS")

                else:
                    # Handles case where package is not found in the hash table
                    print(f"Package {package_id} not found")


            except ValueError:
                print("Please enter a valid package ID.")

        elif user_input == "3":
            print("Exiting...")
            return

        else:
            print("Invalid choice, please select 1, 2, or 3.")
user_interface()






