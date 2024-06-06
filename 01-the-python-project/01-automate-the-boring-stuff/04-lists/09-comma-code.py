def comma_seperated_string(list_value):
    string_value = ", ".join(list_value[:-1])
    string_value += " and " + list_value[-1]
    return string_value

spam = ["apples", "bananas", "tofu", "cats"]
print(comma_seperated_string(spam))