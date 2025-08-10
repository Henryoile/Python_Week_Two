# my_list_script.py
my_list = []
print("Step 1 - created empty list:", my_list)

for value in (10, 20, 30, 40):
    my_list.append(value)
print("Step 2 - after appending 10, 20, 30, 40:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("Step 3 - after inserting 15 at second position (index 1):", my_list)

# Extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("Step 4 - after extending with [50, 60, 70]:", my_list)

# Remove last element
removed = my_list.pop()
print(f"Step 5 - removed the last element ({removed}):", my_list)

# Sort ascending
my_list.sort()
print("Step 6 - after sorting in ascending order:", my_list)

# Find and print index of 30
index_of_30 = my_list.index(30)
print("Step 7 - index of the value 30 in my_list:", index_of_30)

print("Final my_list:", my_list)
