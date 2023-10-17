student_data = {
    "name" : "Wahome",
    "year" : 2023,
    "gender": "male",
    "date": "12/12/2023"
}
print(student_data)
student_data.update({"color": "black"})
print(student_data)
student_data.pop("gender")
print(student_data)