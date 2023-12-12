#Given user preferences and recommended items
#Find items that the user has not yet tried from the recommendations

user_preferences = {"apple", "banana", "cherry", "grape"}
recommended_items = {"cherry", "grape", "kiwi", "orange"}

nottried_items=recommended_items-user_preferences

print("items not yet tried:")
for x in nottried_items:
    print(x)

#without Difference
untried_items = [item for item in recommended_items if item not in user_preferences]

print("Untried items:", untried_items)
