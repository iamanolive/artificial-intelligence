def print_table(table_data):
    longest_count = []
    list_count = len(table_data)
    string_count = len(table_data[0])
    for i in table_data:
        current_longest = 0
        for j in i:
            if len(j) > current_longest:
                current_longest = len(j)
        longest_count.append(current_longest)
    for i in range(0, string_count):
        for j in range(0, list_count):
            print(table_data[j][i].rjust(longest_count[j]), end = " ")
        print(end = "\n")

input_table = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"]
]

print_table(input_table)