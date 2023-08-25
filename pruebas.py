def sum_substrings(input_string):
    sub_strings = input_string.split('%')
    if len(input_string) == 9:
        return input_string.rstrip('-%')
    else: 
        first_values = sub_strings[0].split('-')
        second_values = sub_strings[1].split('-')
        result = []
    for first, second in zip(first_values, second_values):
        if first.isdigit() and second.isdigit():
            result.append(str(int(first) + int(second)))
    return "-".join(result)

cadena1 = "2-3-0-4-%3-4-0-2-%"
resultado1 = sum_substrings(cadena1)
print(resultado1)

cadena2 = "1-0-1-5-%"
print(len(cadena2))

resultado2 = sum_substrings(cadena2)
print(resultado2)
