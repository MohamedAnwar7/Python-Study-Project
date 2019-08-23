# Empty file for code testing
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for value in a:
    if value < 5:
        new_list.append(value)

print("Num less than 5 :{}".format(new_list))
