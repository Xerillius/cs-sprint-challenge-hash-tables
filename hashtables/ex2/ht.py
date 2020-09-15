class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.entries = 0

    def get_num_slots(self):
        return len(self.buckets)

    def get_load_factor(self):
        load_factor = self.entries / self.capacity
        return load_factor

    def fnv1(self, key):
        pass

    def djb2(self, key):
        djb2_hash = 5381
        for x in key:
            djb2_hash = ((djb2_hash << 5) + djb2_hash) + ord(x)
        return djb2_hash & 0xFFFFFFFF

    def hash_index(self, key):
        index = self.djb2(key) % len(self.buckets)
        if index:
            return index
        else:
            return None

    def put(self, key, value):
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        bucket_pos = self.hash_index(key)
        cur_node = self.buckets[bucket_pos]
        while cur_node is not None:
            if cur_node.key == key:
                cur_node.value = value
                return
            cur_node = cur_node.next
        new_entry = HashTableEntry(key, value)
        if(self.buckets[bucket_pos] is None):
            self.buckets[bucket_pos] = new_entry
        else:
            cur_node = self.buckets[bucket_pos]
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_entry
        self.entries += 1

    def delete(self, key):
        bucket_pos = self.hash_index(key)
        cur_node = self.buckets[bucket_pos]
        if cur_node is not None:
            if cur_node.key == key:
                self.buckets[bucket_pos] = cur_node.next
                del cur_node
                self.entries -= 1
                return f"Deleted {key}"
            prev_node = cur_node
            cur_node = cur_node.next
            while cur_node is not None:
                if cur_node.key == key:
                    prev_node.next = cur_node.next
                    del cur_node
                    self.entries -= 1
                    return f"Deleted {key}"
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
            return "Key not found in bucket"
        else:
            return "Bucket Empty"

    def get(self, key):
        bucket_pos = self.djb2(key) % len(self.buckets)
        cur_node = self.buckets[bucket_pos]
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next
        return None

    def resize(self, new_capacity):
        self.capacity = new_capacity
        if self.capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY

        old_buckets = self.buckets
        self.buckets = [None] * self.capacity

        for bucket in old_buckets:
            if bucket is not None:
                cur_node = bucket
                while cur_node is not None:
                    key = cur_node.key
                    value = cur_node.value
                    self.put(key, value)
                    cur_node = cur_node.next
        del old_buckets