import json
import tabulate


def readFromJSON(nme):
    with open(nme, 'r') as json_file:
        heroes = json.load(json_file)

        printListOfDict(heroes)

        sum_height = sum([float(row["Height"]) for row in heroes])
        sum_weight = sum([float(row["Weight"]) for row in heroes])
        count_heroes = len(heroes)
        average_height = sum_height / count_heroes
        average_weight = sum_weight / count_heroes

        print("\n***** Quick Analysis *****")
        print("Total number of heroes: {0}".format(count_heroes))
        print("Average height: {0:.2f}%".format(average_height))
        print("Average weight: {0:.2f}".format(average_weight))
        print("")

        count_female = 0
        count_male = 0

        for hero in heroes:
            if hero["Gender"] == 'Female':
                count_female += 1
            else:
                count_male += 1

        print("Heroes by gender: ")
        print("Female -> {0}".format(count_female))
        print("Male -> {0}".format(count_male))
        print("")

        color_yellow = 0
        color_blue = 0
        color_red = 0
        color_green = 0
        color_black = 0

        for hero in heroes:
            if hero["Eye color"] == 'Yellow':
                color_yellow += 1
            elif hero["Eye color"] == 'Blue':
                color_blue += 1
            elif hero["Eye color"] == 'Red':
                color_red += 1
            elif hero["Eye color"] == 'Green':
                color_green += 1
            else:
                color_black += 1

        print("Heroes with eye color of: ")
        print("Yellow -> {0}".format(color_yellow))
        print("Blue -> {0}".format(color_blue))
        print("Red -> {0}".format(color_red))
        print("Green -> {0}".format(color_green))
        print("Black -> {0}".format(color_black))
        print("")

        hair_no = 0
        hair_blue = 0
        hair_black = 0

        for hero in heroes:
            if hero["Hair color"] == 'No Hair':
                hair_no += 1
            elif hero["Hair color"] == 'Blue':
                hair_blue += 1
            else:
                hair_black += 1

        print("Heroes with hair colors of: ")
        print("No hair -> {0}".format(hair_no))
        print("Blue -> {0}".format(hair_blue))
        print("Black -> {0}".format(hair_black))
        print("")

        skin_grey = 0
        skin_blue = 0
        skin_white = 0
        skin_red = 0
        skin_green = 0

        for hero in heroes:
            if hero["Skin color"] == 'Grey':
                skin_grey += 1
            elif hero["Skin color"] == 'Blue':
                skin_blue += 1
            elif hero["Skin color"] == 'White':
                skin_white += 1
            elif hero["Skin color"] == 'Red':
                skin_red += 1
            else:
                skin_green += 1

        print("Heroes with skin color of: ")
        print("Grey -> {0}".format(skin_grey))
        print("Blue -> {0}".format(skin_blue))
        print("White -> {0}".format(skin_white))
        print("Red -> {0}".format(skin_red))
        print("Green -> {0}".format(skin_green))
        print("")

        good = 0
        bad = 0

        for hero in heroes:
            if hero["Alignment"] == 'Good':
                good += 1
            else:
                bad += 1

        print("Alignment: ")
        print("Bad -> {0}".format(bad))
        print("Good -> {0}".format(good))
        print("")

        marvel = 0
        dc = 0
        dark_horse = 0

        for hero in heroes:
            if hero["Publisher"] == 'Marvel Comics':
                marvel += 1
            elif hero["Publisher"] == 'DC Comics':
                dc += 1
            else:
                dark_horse += 1

        print("Heroes by publisher: ")
        print("Marvel Comics: -> {0}".format(marvel))
        print("DC Comics -> {0}".format(dc))
        print("Dark Horse Comics -> {0}".format(dark_horse))
        print("")

def printListOfDict(data):
    header = data[0].keys()
    rows = [x.values() for x in data]
    print(tabulate.tabulate(rows, header))


def main():
    jsonFileName = "Heroes.json"
    readFromJSON(jsonFileName)


if __name__ == "__main__":
    main()
