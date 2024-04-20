def exponent(base, exp):
    return int(base) ** int(exp)

input_base = input("base = ")
input_exponent = input("exponent = ")
result = exponent(input_base, input_exponent)

print(input_base + " raised to the power of " + input_exponent + " is " + str(result))
print(input_base + (" * " + input_base) * (int(input_exponent) - 1) + " = " + str(result))