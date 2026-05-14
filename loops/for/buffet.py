dishes = (
    "misto quente", 
    "omelete", 
    "salada", 
    "sanduíche natural", 
    "asinhas de frango"
)

print("O buffet oferece os seguintes pratos:")

for dish in dishes:
    print(f"- {dish}")

# This will raise a TypeError since tuples are immutable.
# dishes[0] = "pizza"  

# To change the dishes, we need to create a new tuple.
dishes = (
    "pizza", 
    "omelete", 
    "salada", 
    "fritas com cheddar e bacon", 
    "asinhas de frango"
    )

print("\nO buffet agora oferece os seguintes pratos:")

for dish in dishes:
    print(f"- {dish}")