from bloom_filter import BloomFilter
from random import shuffle

# Ask the user for input and initialize a Bloom filter based on their specs.
n = int(input("Please enter an estimate for the number of items you will be storing: "))
p = float(input("Please enter your desired false positive probability rate: "))
bloom_filter = BloomFilter(n, p)

# Print top level information about the Bloom filter
print("Bloom filter has a size of {}".format(bloom_filter.size))
print("Bloom filter has a false positive probability of {}".format(bloom_filter.desired_false_positive_probability))
print("Bloom filter is using {} hash functions".format(bloom_filter.hash_count))
print("======================")

usernames_to_add = ["Carpe", "Stitch", "Zunba", "Mang0", "Wumbo William", "Daedalus", "Rin", "Togashi", "Static", 
                  "Haksal", "Gianni", "Brain Surgeon", "Whatever", "Advisor", "Garnt", "Serph"]
for username in usernames_to_add:
    bloom_filter.add(username)

usernames_not_to_add = ["Orange", "Sideshow", "Stan", "Brandon", "Blue", "Lance", "Rivali", "Risotto", "KeyMain", "Orlando"]


# Shuffle the order of the username lists and create a new list of usernames to 
# check against the Bloom filter.
shuffle(usernames_to_add)
shuffle(usernames_not_to_add)
test_usernames = usernames_to_add[-5:] + usernames_not_to_add

for username in test_usernames:
    if bloom_filter.check(username):
        print("{} has probably already been taken.".format(username))
    else:
        print("{} has definitely not been taken yet.".format(username))
