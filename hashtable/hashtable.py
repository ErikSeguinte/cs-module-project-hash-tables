class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __eq__(self, other):
        if self.key == other.key: return True


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY: capacity = MIN_CAPACITY
        self.capacity = capacity
        self.storage = [None] * capacity
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.load / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        offset = 0xcbf29ce484222325
        prime = 0x100000001b3

        hash = offset

        for char in key.encode("utf-8"):
            hash = hash ^ char
            hash = hash * prime


        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.load += 1
        index = self.hash_index(key)
        item = HashTableEntry(key, value)
        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index].value = value
                return
            node: HashTableEntry = self.storage[index] 
            while node.next is not None:
                node = node.next
                if node.key == key:
                    node.value = value
                    return
            node.next = item
        else:
            self.storage[index] = item

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        node = self.storage[i]
        prev = None

        while node is not None:
            if node.key == key:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.storage[i] = node.next
                return
            else:
                prev = node
                node = node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        if self.storage[i] is not None:
            node: HashTableEntry = self.storage[i]
            if node.key == key:
                return node.value
            while node.next is not None:
                node = node.next
                if node.key == key:
                    return node.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = self.storage
        self.storage = [None] * new_capacity
        self.capacity = new_capacity
        for e in old_table:
            if e is not None:
                k, v = e.key, e.value
                self.put(k, v)
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
