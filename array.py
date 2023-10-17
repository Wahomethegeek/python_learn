class_names = ["Wahome", "Ian", "Ashely", "Jedidah", "Cliff"]
print(len(class_names))
print(class_names[-1])
print(class_names[0])
class_names.insert(0, "Njeri")
print((class_names))

class_names.remove("Wahome")
print(class_names[2:4])
print(class_names)
del class_names[0]
print(class_names)

grades = [12, 345, 34, 34, 34, 43]
grades.sort()
print(grades) #sorts in ascending order

# descending order
grades.sort(reverse=True)
print(grades)
print(8<3)
tuplelearn = ("Wahome", "kelvin")
print(tuplelearn)
# Tuples are not changeable, ordered but still use indexing for access
combined_list = list(tuplelearn) + class_names
print(combined_list)
if "Wahome" in combined_list:
    print("Student exist")
else:
    print("Add student")