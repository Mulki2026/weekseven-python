# Part A — List Warmup

# 1. Create a list called fruits containing four fruits
fruits = ["apple", "banana", "cherry", "mango"]

# 2. Print the first and the last item using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 3. .append() a fifth fruit, then print the whole list
fruits.append("orange")
print(f"List after appending fifth fruit: {fruits}")

# 4. .remove() one fruit, then print the list again
fruits.remove("banana")
print(f"List after removing 'banana': {fruits}")

# 5. Print how many fruits remain using len()
print(f"Number of remaining fruits: {len(fruits)}")