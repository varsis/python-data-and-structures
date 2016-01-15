'''
Simple implementation using Lists
'''

class Map:
    def __init__(self,size=100):
        '''
        Key,Value Mappings
        Default Size 100
        :param size:
        :return:
        '''
        self.size = size

        # Store keys/values
        self.keys = [None] * size
        self.data = [None] * size

    def set(self,key,value):
        '''
        Set Key, Value in map
        :param key:
        :param value:
        :return:
        '''

        hashvalue = self.hash(key)

        # If collision try new value
        while not self.setKeyValueHash(hashvalue,key,value):
            # Get a new hash value
            # Note could cause infinite loop if all slots full.
            hashvalue = self.rehash(hashvalue)


    def setKeyValueHash(self,hash,key,value):
        '''
        Try Insert current key at hash, Return true is succesful
        Otherwise false
        :param self:
        :param hash:
        :param key:
        :param value:
        :return:
        '''
        currentValue = self.keys[hash]

        # Empty or is the key
        if currentValue == key:
            self.data[hash] = value
            return True

        if currentValue == None:
            self.keys[hash] = key
            self.data[hash] = value
            return True

        return False


    def hash(self,key):
        '''
        Get hash value of key
        :param key:
        :return:
        '''

        return hash(key) % self.size

    def rehash(self,hash):
        '''
        Get Secondary hash of hash value
        :param hash:
        :return:
        '''
        return (hash + 1) % self.size


    def delkey(self,key):
        '''
        Delete Key
        :param key:
        :return:
        '''

        hashvalue = self.hash(key)

        while self.keys[hashvalue] != None and self.keys[hashvalue] != key:
            hashvalue = self.rehash(hashvalue)

        self.data[hashvalue] = None
        self.keys[hashvalue] = None

    def get(self,key):
        '''
        Get Item with key
        :param key:
        :return:
        '''

        hashvalue = self.hash(key)

        while self.keys[hashvalue] != None and self.keys[hashvalue] != key:
            hashvalue = self.rehash(hashvalue)

        return self.data[hashvalue]

    def __setitem__(self, key, value):
        self.set(key,value)

    def __delitem__(self, key):
        self.delkey(key)

    def __getitem__(self, key):
        return self.get(key)