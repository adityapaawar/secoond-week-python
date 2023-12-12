#Given two sets of users - friends and followers
#Check if a specific user is a mutual friens and follower
friends = {"Alice", "Bob", "Carol"}
followers = {"Bob", "David", "Eve"}

specific_user = "Bob"

if specific_user in friends and specific_user in followers:
    print(f"{specific_user} is a mutual friend and follower.")
else:
    print(f"{specific_user} is not a mutual friend and follower.")
    
#using intersection method
print("in both",friends.intersection(followers))
