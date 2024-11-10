
from Package import Package

class HashTable:

    def __init__(self, size=40):
        self.table = [[] for i in range(size)]

    def insert(self, key, value):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                bucket_list[i] = (key, value)
                return True
        bucket_list.append((key, value))
        return True

    def lookup(self, key):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

        #print(f"Looking for key {key} at index {bucket_index}, bucket {bucket_list}")

        for item in bucket_list:
            if key == item[0]:
                return item[1]
       # print(f"Key {key} not found in bucket")
        return None


    def remove(self, key):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                del bucket_list[i]
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
        return result

#testing data
hash_table = HashTable(40)



#hash_table.insert(packagetest.id_num, packagetest)

#print(hash_table.lookup(1))
#hash_table.insert(packagetest.id_num, packagetest)
#hash_table.lookup(1)
#truck1 = Truck(truck_id=1, capacity=10, speed=50, package_ids=[1, 13, 14], mileage=0, address="Start", depart_time="08:00", package_hash_table=hash_table)
#insert_test = hash_table.lookup("grade_one")
#print(f"The value of the key is {insert_test}")

#remove_test = hash_table.remove("grade_one")
#print(f"Key 'grade_one' removed: {remove_test}" )