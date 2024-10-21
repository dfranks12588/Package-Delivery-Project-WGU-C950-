class HashTable:

    def __init__(self, size=50):
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
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for pair in bucket_list:
            if pair[0] == key:
                return pair[1]

        return None

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for index, pair in enumerate(bucket_list):
            if pair[0] == key:
                del bucket_list[index]
                return True

        return False




hash_table = HashTable()
hash_table.insert("grade_one", 3)

insert_test = hash_table.lookup("grade_one")
print(f"The value of the key is {insert_test}")

remove_test = hash_table.remove("grade_one")
print(f"Key 'grade_one' removed: {remove_test}" )