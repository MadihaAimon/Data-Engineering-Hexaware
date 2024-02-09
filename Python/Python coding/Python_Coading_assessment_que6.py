import json

# # JSON string representing a dictionary
# json_string_dict = '{"name": "Alice", "age": 30, "city": "New York"}'
#
# # Parse JSON string to a Python dictionary
# python_dict = json.loads(json_string_dict)
#
# print("Python Dictionary:", python_dict)
# print("Name:", python_dict['name'])
# print("Age:", python_dict['age'])
# print("City:", python_dict['city'])

# JSON string representing a list
json_string_list = '[1, 2, 3, 4, 5]'

# Parse JSON string to a Python list
python_list = json.loads(json_string_list)

print("\nPython List:", python_list)
print("Sum of List:", sum(python_list))