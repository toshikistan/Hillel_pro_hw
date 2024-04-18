def new_format(string):
    num_groups = []
    while len(string) > 3:
        num_groups.append(string[-3:])
        string = string[:-3]
    num_groups.append(string)
    num_groups.reverse()
    formatted_num = ".".join(num_groups)
    return formatted_num


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

print("Everything fine!")
