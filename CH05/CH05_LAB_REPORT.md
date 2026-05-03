# Chapter 5: Hash Tables — Lab Report

## Student Information
- **Name:** David Diaz Cutie
- **Date:** 03/10/2026
- **Course:** COSC 2436

## Key Concepts

**Hashing:** Transforming a key into an integer index using a hash function. In this implementation, Python's built-in `hash()` function is combined with the modulo operator (`% self.size`) to map any key to a valid index within the array.

**Linear Probing:** A method of open addressing collision resolution. When a collision occurs (two keys map to the same index), the algorithm searches for the next available empty slot by incrementing the index by 1, wrapping around to the beginning of the array if necessary. The search function uses a `start_index` to detect when the entire table has been scanned, preventing an infinite loop when the table is full.

## Test Results

```
$ python3 hashtable.py

hash_table.search("apple")   → 100
hash_table.search("banana")  → 200
hash_table.search("orange")  → 300
hash_table.search("grape")   → None
```

| Key      | Value Inserted | Search Result | Notes                        |
|----------|---------------|---------------|------------------------------|
| "apple"  | 100           | 100           | ✅ Found                     |
| "banana" | 200           | 200           | ✅ Found                     |
| "orange" | 300           | 300           | ✅ Found                     |
| "grape"  | —             | None          | ✅ Correctly returns None    |

## What I Learned

I learned how to handle collisions without using separate chaining (linked lists). Instead of storing multiple items at one index, I learned how to "probe" or skip to the next available slot using linear probing. I also learned the importance of tracking the `start_index` during a search — without it, the search function could loop infinitely if the table is full and the key is not present. Additionally, implementing the update logic inside `insert` (checking if a key already exists before inserting) taught me that hash tables need to handle both new insertions and key updates in the same operation.

## Challenges

The most difficult part was ensuring the search and insert functions did not get stuck in an infinite loop. For `insert`, the loop exits naturally when an empty slot is found, but for `search`, there is no empty slot to signal termination if the key does not exist and the table is full. The solution was to record the starting index before the loop begins and break out as soon as the probe wraps back around to it, guaranteeing the loop always terminates.

## Reflection Questions

### What are the advantages of using a hash table?

The primary advantage of a hash table is speed. For insertion, deletion, and lookup, hash tables provide an average time complexity of O(1) — constant time. This means that whether you have 10 items or 10 million, finding a specific key takes roughly the same amount of time, which makes hash tables one of the most practical data structures for real-world applications like caches, dictionaries, and database indexes.

### How does the hash function affect the performance of a hash table?

The hash function is the core of the entire operation, and its quality determines whether the table stays fast or slows down significantly. A good hash function distributes keys uniformly across the array — if it is poor, many keys cluster around the same indices, turning O(1) operations into O(n) because of excessive probing. The function must also be fast to compute and deterministic, meaning it always produces the same output for the same input, otherwise stored values can never be reliably retrieved.

### What are other collision resolution techniques besides linear probing?

**Separate Chaining:** Each bucket in the array holds a linked list. If a collision occurs, the new item is appended to the list at that index, so multiple keys can coexist at the same slot without displacing each other.

**Quadratic Probing:** Instead of checking the next slot (+1, +2, +3), it uses a quadratic function (+1, +4, +9) to determine the next probe location. This reduces "primary clustering," where consecutive filled slots slow down all future insertions in that region.

**Double Hashing:** If a collision occurs, a second hash function determines the step size for probing. Because different keys follow different probe sequences, this produces more uniform distribution and avoids both primary and secondary clustering.
