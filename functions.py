import random

# Takes the name of a .txt file and, line by line, creates a list from the strings.  Returns the list
def make_list_from_file(file):
    list = []
    with open(file, 'r') as f:
        str = ""

        for readline in f:
            line_strip = readline.strip()
            str = line_strip
            list.append(str)
    return list

# Initializes the list adultTraits in main from the files that apply
def initialize_adult_trait_list():
    list = []
    newList = []
    newList = make_list_from_file("AdultExclusiveTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("TeenExclusiveTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("BaseTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("CityTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("CottageTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("EcoTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("FamousTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("IslandTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("OutdoorTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("SnowyTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("StrangerTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("TogetherTraits.txt")
    list.extend(newList)
    return list

# Initializes the list teenTraits in main from the files that apply
def initialize_teen_trait_list():
    list = []
    newList = make_list_from_file("TeenExclusiveTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("BaseTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("CityTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("CottageTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("EcoTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("FamousTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("IslandTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("OutdoorTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("SnowyTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("StrangerTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("TogetherTraits.txt")
    list.extend(newList)
    return list

# Initializes the list childTraits in main from the files that apply
def initialize_child_trait_list():
    list = []
    newList = make_list_from_file("BaseTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("CottageTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("EcoTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("IslandTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("OutdoorTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("SnowyTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("StrangerTraits.txt")
    list.extend(newList)
    newList = make_list_from_file("TogetherTraits.txt")
    list.extend(newList)

    return list

# Initializes the list toddlerTraits in main from the files that apply
def initialize_toddler_trait_list():
    list = []
    newList = make_list_from_file("ToddlerExclusiveTraits.txt")
    list.extend(newList)
    return list

# returns a random item (string) from a parameter list
def generate_random_item_from_list(list):
    r = random.randint(0, len(list)-1)
    return list[r]