import csv


def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            # Creating a CSV reader object
            csv_reader = csv.reader(csvfile)

            # Reading and printing each row in the CSV file
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'your_file.csv'
read_csv_file("file.txt")
