"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

# 1. 
max_age = max(person["age"] for person in group.values())

# 2. 
average_relations = sum(len(person["relations"]) for person in group.values()) / len(group)
# 3. 
max_age_with_relations = max(person["age"] for person in group.values() if person["relations"])

# 4. 
max_age_with_friend = max(
    person["age"] for person in group.values() 
    if any(relation_type == "friend" for relation_type in person["relations"].values())
)


print(f"The maximum age of people in the group: {max_age}")
print(f"The average (mean) number of relations among members of the group: {average_relations:.2f}")
print(f"The maximum age of people in the group that have at least one relation: {max_age_with_relations}")
print(f"The maximum age of people in the group that have at least one friend: {max_age_with_friend}")
