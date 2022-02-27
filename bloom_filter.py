import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):
    """
    Class modeling the logic and functionality of a Bloom filter, using murmur3 hash functions.

    Attributes
    ----------
    expected_item_count : int
        The number of items we expect to need to store.
    desired_false_positive_probability : float
        A float between 0 and 1 that represents our accepted probability of the Bloom filter returning a false positive.
    size : int
        The size of bit_array associated with the Bloom filter.
    bit_array : bitarray
        The bitarray used to determine if the Bloom filter already "contains" an item.
    hash_count : int
        The number of hash functions the Bloom filter uses when adding / checking for items in its storage.

    Methods
    -------
    add(item):
        Add the item argument to the Bloom filter.

    check(item):
        Check if the item argument exists in the Bloom filter.
    """
    def __init__(self, expected_item_count, desired_false_positive_probability):
        """
        Constructor for BloomFilter objects.
        Calculate the optimal size of the Bloom filter's bitarray based on the number of expected items and desired false positivity probability,
        and initialize a bitarray of that size with all bits set to 0.

        Parameters
        ----------
        expected_item_count : int
            The number of items we expect to need to store.
        desired_false_positive_probability : float
            A float between 0 and 1 that represents our accepted probability of the Bloom filter returning a false positive.
        """
        self.expected_item_count = expected_item_count
        self.desired_false_positive_probability = desired_false_positive_probability
        self.size = self.__calculate_size()
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        self.hash_count = self.__calculate_hash_count()

    def add(self, item):
        """
        Add the item argument to the Bloom filter.

        Parameters
        ----------
        item : str
            A str representing a username that we want to add to the Bloom filter.
        
        Returns
        -------
        None
        """
        for digest in self.__calculate_digests(item):
            self.bit_array[digest] = True

    def check(self, item):
        """
        Check if the item argument exists in the Bloom filter.
        Note: This check can return false positives, but will never return a false negative.

        Parameters
        ----------
        item : str
            A str representing a username that we want to check the availability of.
        
        Returns
        -------
        Boolean
        """
        return all([self.bit_array[index] for index in self.__calculate_digests(item)])

    def __calculate_size(self):
        """
        Determine the optimal size of the Bloom filter's bitarray based on the expected item count and 
        desired false positivity probability of the Bloom filter.

        Parameters
        ----------
        None
        
        Returns
        -------
        int
        """
        size = -(self.expected_item_count * math.log(self.desired_false_positive_probability)) / (math.log(2) ** 2)
        return int(size)

    def __calculate_hash_count(self):
        """
        Determine the number of hash functions to be used by the Bloom filter when adding or checking for items within itself.

        Parameters
        ----------
        None
        
        Returns
        -------
        int
        """
        return int((self.size / self.expected_item_count) * math.log(2))

    def __calculate_digests(self, item):
        """
        Perform hashing operations on the item argument and return an array of the digests that resulted from those hashing operations.

        Parameters
        ----------
        item : str
            A str representing a username that we want to calculate the digests of.
        
        Returns
        -------
        array
        """
        digests = []
        for i in range(self.hash_count):
            digests.append(mmh3.hash(item, i) % self.size)
        return digests
