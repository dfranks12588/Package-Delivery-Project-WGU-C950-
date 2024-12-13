
class HashTable:
# Creates an instance of a hash table with an empty list for each bucket
    def __init__(self, size=40):
        self.table = [[] for i in range(size)]

# Inserts the key-value pairs into the hash table
    def insert(self, key, value):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

        # If the key already exists the value is replaced
        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                bucket_list[i] = (key, value)
                return True

        #Otherwise append a new kay-value pair
        bucket_list.append((key, value))
        return True

# Finds the index of the bucket where the key should be to lookup packages
    def lookup(self, key):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

# Loops through the items in the buckets to find the key-value pair
        for item in bucket_list:
            # If the key matches, this returns the associated value
            if key == item[0]:
                return item[1]
        return None

# Finds the index of the bucket where the key should be to remove packages
    def remove(self, key):
        bucket_index = key % len(self.table)
        bucket_list = self.table[bucket_index]

        for i, (k, v) in enumerate(bucket_list):
            if k == key:
                del bucket_list[i]
                return True
        return False



