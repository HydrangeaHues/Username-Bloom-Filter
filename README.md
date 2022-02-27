# Username-Bloom-Filter
Implementation of a Bloom filter in Python that simulates using a Bloom filter to determine if usernames are available.

## About Bloom Filters
Bloom filters are a probabilistic data structure that are used to determine if an element is a member of a set. They are capable of telling you something is definitely not in a set, or that something probably is in a set. False positives are possible (saying something is in a set when it is not), but the odds of getting a false positive response can be tuned based on user's needs.

Bloom filters do not store the elements themselves, and it is impossible to "remove" an element from a standard Bloom filter. Removing an element from a Bloom filter could result in the filter thinking that other elements (other than the one that was removed) had also been removed from the filter. Modifications on the Bloom filter, such as the Counting Bloom filter, do allow for removing elements, but at the cost of space.

## About This Project
I was learning about Bloom filters and their uses and wanted to try implementing one of my own. I am still brushing up on my Python, so I chose that as my language.

## Places for Expansion and Improvememt
- Add validation of user input.
