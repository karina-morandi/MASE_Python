import random
import matplotlib.pyplot as plt


def generate_random_list(size):
    # The underscore here is to indicate that the/a loop counter is not used
    return [random.randint(1, 10) for _ in range(size)]

def countDistinct(unique, data):
    # Create 2 storage units
    plotdata = []
    count = []
    for item in unique:
        plotdata.append(item)
        count.append((data.count(item)))
        print("{0} -> {1}".format(item, data.count(item)))

    fig, ax = plt.subplots()
    ax.bar(plotdata, count)
    ax.set_ylabel("Occurrences")
    ax.set_title("Set Items")
    plt.xticks(plotdata)
    plt.show()

def main():
    list_size = 30
    random_list = generate_random_list(list_size)
    print("Data generated: \n {0}".format(random_list))
    list_set = list(set(random_list))
    print("Unique items: {0}".format(list_set))
    countDistinct(list_set, random_list)


if __name__ == "__main__":
    main()
