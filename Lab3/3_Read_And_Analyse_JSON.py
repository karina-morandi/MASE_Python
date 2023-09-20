import json
import tabulate


def readFromJSON(nme):
    with open(nme, 'r') as json_file:
        grades = json.load(json_file)

    print("\n Working with a list of dictionaries leaded from JSON file")
    printListOfDict(grades)
    # Print and calculate information about the file
    # Use the key name to reference the row
    # Other calculations are the same
    sum_ages = sum([float(row["Age"]) for row in grades])
    sum_grades = sum([float(row["Grade"]) for row in grades])
    count_students = len(grades)
    average_grade = sum_grades / count_students
    average_age = sum_ages / count_students

    print("\n***** Quick Analysis *****")
    print("Total number of students: {0}".format(count_students))
    print("Average grade: {0:.2f}%".format(average_grade))
    print("Average student age: {0:.2f}".format(average_age))


def printListOfDict(data):
    header = data[0].keys()
    rows = [x.values() for x in data]
    print(tabulate.tabulate(rows, header))


def main():
    jsonFileName = "Grades.json"
    readFromJSON(jsonFileName)


if __name__ == "__main__":
    main()
