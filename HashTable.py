
from Package import Package

class HashTable:

    def __init__(self, size=40):
        self.table = [[] for i in range(size)]

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for pair in bucket_list:
            if pair[0] == key:
                pair[1] = value
                return True

        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    def lookup(self, key):
        index = hash(key) % len(self.table)
        bucket= self.table[index]

        print(f"Looking for key {key} at index {index}, bucket {bucket}")

        if bucket:
            for pair in bucket:
                if pair[0] == key:
                    print(f"looking up key: {key} found {pair[1]}")
                    return pair[1]
            print(f"Looking up key {key} and found none!")
            return None


    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for index, pair in enumerate(bucket_list):
            if pair[0] == key:
                del bucket_list[index]
                return True
        return False

    def __str__(self):
        result = "Hashtable contents : \n"
        for i, bucket in enumerate(self.table):
            if bucket:
                for key, value in bucket:
                    result += f" Bucket {i} : Key = {key}, Value = {value}\n"
            else:
                result += f"Bucket {i} : Empty\n"
        return result if result != "Hashtable contents : \n" else "Hashtable is emptity bempity"
#testing data
hash_table = HashTable(40)


packagetest = Package(
    id_num=1,
    address="a",
    city="a",
    state="a",
    zip="1234",
    deadline="eod",
    weight=5.0,
    status="At hub"
)


#hash_table.insert(packagetest.id_num, packagetest)

#print(hash_table.lookup(1))
#hash_table.insert(packagetest.id_num, packagetest)
#hash_table.lookup(1)
#truck1 = Truck(truck_id=1, capacity=10, speed=50, package_ids=[1, 13, 14], mileage=0, address="Start", depart_time="08:00", package_hash_table=hash_table)
#insert_test = hash_table.lookup("grade_one")
#print(f"The value of the key is {insert_test}")

#remove_test = hash_table.remove("grade_one")
#print(f"Key 'grade_one' removed: {remove_test}" )