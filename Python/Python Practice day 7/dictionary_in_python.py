def dictionary_program():
    student_info = {
        'name': 'John',
        'age': 20,
        'grade': 'A',
        'courses': ['Math', 'English', 'Science']
    }

    # Displaying the original dictionary
    print("Original Dictionary:", student_info)

    # Accessing values using keys
    print("Name:", student_info['name'])
    print("Age:", student_info['age'])

    # Modifying a value in the dictionary
    student_info['age'] = 21

    # Displaying the dictionary after modification
    print("Dictionary after modification:", student_info)

    # Finding the number of key-value pairs in the dictionary
    dictionary_size = len(student_info)
    print("Number of key-value pairs in the dictionary:", dictionary_size)


dictionary_program()
