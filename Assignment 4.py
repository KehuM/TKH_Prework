def big_name():
    names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
    longest_name = ""
    for names in names_list:
        if len(names) > len(longest_name):
            longest_name = names
        else:
            longest_name = ""
    print(longest_name)


big_name()
