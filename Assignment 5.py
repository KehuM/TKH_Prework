names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
odd_list = []
even_list = []

for name in names_list:
    if (len(name) % 2) == 0:
        even_list.insert(1, name)
    else:
        odd_list.insert(1, name)


def even():
    even_list[0] = "bernie"
    even_list[1] = "buture hendrix"
    even_list[2] = "bordan"


even()
odd_list[0] = "boc"
odd_list[1] = "max c"
odd_list[2] = "jimmc"
print(odd_list)
print(even_list)
