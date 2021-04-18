"""
hashing: best case is O(1) but because of collisions, number of collisions is not so simple
    load factor is most important piece of information to analyze hash table
    if load factor is small, then it means that the table is not so full, and the chances of collision are smaller, so items should be where we expect
    otherwise, if load factor is large, the table is filling up and and there are more and more collisions.

remainder method: divides item by table size
    h(item) = item % len(table) i.e. h(item) =  item % 11 (if table is len 11)
** load factor: load factor = number_of_items / tablesize
collision: if 44 and 77 are both items for the hash table, they both will produce remainder 0 if table size is 11.

still want to keep the table size from getting too big, wasting memory
folding method: divide the item into equal size pieces and then add together. Then divide by table size and get remainder
    i.e. phone number 436-555-4601 -> 43,65,55,46,01, and take the sum of those pieces -> 210 % table_size
mid-square method: first square the item, then extract some portion of the resulting digits, then get remainder after dividing by table size
    i.e. 44 ** 2 -> 1936, then extract middle two digits -> 93 % table_size

strings
convert each character to ordinal number. Can use the position of the character as weight because anagrams will give the same values (i.e. mop and pom)

rehashing: general term for looking for another slot after collision has occurred.
    rehash(pos) = (pos + skip) % size_of_table. To ensure that all the slots will be visited by the skip method, suggested to use a prime number as the table size
"""


def modulohash(numlist, tablesize):
    res = ['_' for i in range(tablesize)]
    for i in numlist:
        hash = i % tablesize
        # check for collision. if the spot is empty, insert value
        if res[hash] == '_':
            res[hash] = i
        else:
            # if there is a collision, iterate from that position to the end of the table
            # won't wrap around
            for j in range(tablesize - hash):
                # check for collisions until an empty spot is found
                if res[hash + j] == '_':
                    res[hash + j] = i
    if '_' not in res:
        return 'Hash is full'
    return res


# print(modulohash([113, 117, 97, 100, 114, 108, 116, 105, 99], 11))


def hash(astring, tablesize):
    """hash a string, taking position of character as weight"""
    sum = 0
    for pos in range(len(astring)):
        sum = sum + (pos + 1) * ord(astring[pos])
    return sum % tablesize


# print(hash('cat', 11))
# print(hash('tac', 11))

class HashTable:
    """
    implements the simple remainder method and plus 1 method for hash collisions
    """
    def __init__(self):
        self.size = 11
        # slots holds the keys
        self.slots = [None] * self.size
        # data holds the values
        self.data = [None] * self.size

    def hashfunc(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        # plus one method
        return (oldhash + 1) % size

    def put(self, key, val):
        hashval = self.hashfunc(key=key, size=len(self.slots))
        if self.slots[hashval] is None:
            self.slots[hashval] = key
            self.data[hashval] = val
        else:
            if self.slots[hashval] == key:
                # replace the value
                self.data[hashval] = val
            else:
                # if the key occupying this slot is a different one, that's a collision, use the plus one method
                nextslot = self.rehash(oldhash=hashval, size=len(self.slots))
                # keep rehashing until empty slot and the nextslot is not the same key. If one criteria is met, it will
                # exit the while loop because it's an "and" condition
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(oldhash=nextslot, size=len(self.slots))
                # check the condition. if nextslot is None, if so then enter in the new key val pair
                if self.nextslot is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = val
                else: # if the same key was found, replace the value
                    self.data[nextslot] = val

    def get(self, key):
        startslot = self.hashfunc(key=key, size=len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # move to the next slot
                position = self.rehash(oldhash=position, size=len(self.slots))
                if position == startslot:
                    # if we circle all the way around, stop. data will be None and returned
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key=key)

    def __setitem__(self, key, val):
        self.put(key=key, val=val)

H = HashTable()
H[54]="cat"
H[41]="dog"
H[26]="dinosaur"
print(H[54])
H[54]="duck"
print(H[54])


