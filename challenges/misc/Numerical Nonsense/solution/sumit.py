with open("numbers.in", 'r') as fi:
    dump = fi.read().replace('"', '')  # Remove the double quotation marks
    numbers = dump.split('!@#')  # Split the numbers using the special characters
    number_list = [int(number) for number in numbers if number.strip()]  # Convert the numbers to integers, ignoring empty strings

with open("numbers.out", 'w') as fo:
    fo.write(str(sum(number_list)) + "\n")