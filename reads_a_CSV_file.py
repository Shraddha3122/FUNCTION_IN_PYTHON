# Create a function that reads a CSV file and returns the contents as a list of dictionaries.

# import csv
import csv
# read csv file to a list of dictionaries
with open('C:/Users/iTA/Downloads/insurance_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
print(data)