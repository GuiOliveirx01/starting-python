places = [
    'nova zelândia', 
    'canadá', 
    'japão', 
    'estados unidos', 
    'austrália'
]

print("Here is the original list:")
print(places)

# sorted() creates a sorted copy without changing the original list
print("\nHere is the sorted list:")
print(sorted(places))

print("\nHere is the original list again:")
print(places)

# reverse() reverses the current order of the list
places.reverse()

print("\nHere is the reverse list:")
print(places)

places.reverse()

print("\nHere is the original list one more time:")
print(places)

# sort() permanently changes the list
places.sort()

print("\nHere is the sorted list again:")
print(places)

# Order in reverse order (Z → A)
places.sort(reverse=True)

print("\nHere is the reverse sorted list:")
print(places)