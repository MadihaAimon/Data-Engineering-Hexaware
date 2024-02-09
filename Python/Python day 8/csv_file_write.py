import csv


def csv_file_write(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            csv_read = csv.reader(csvfile)

            with open("example2.csv", 'a') as csvfile2:
                csv_write = csv.writer(csvfile2, delimiter='-')

                for row in csv_read:
                    csv_write.writerow(row)
    except FileNotFoundError:
        print("File not found ")


csv_file_write("example.csv")
