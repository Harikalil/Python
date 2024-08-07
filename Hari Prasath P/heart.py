def print_heart_pattern(name):
    height = 7
    width = 2 * height - 1
    for i in range(height):
        for j in range(width):
            if (i == 3 and (j == 3 or j == 4)) or \
               (i == 2 and (j == 2 or j == 5)) or \
               (i == 2 and (j == 1 or j == 6)) or \
               (i == 3 and (j == 0 or j == 7)) or \
               (i == 4 and (j >= 1 and j <= 6)) or \
               (i == 5 and (j >= 2 and j <= 5)) or \
               (i == 6 and (j >= 3 and j <= 4)):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    center_row = height // 2 + 1
    center_space = (width - len(name)) // 2
    for i in range(center_row, center_row + 1):
        print(" " * center_space + name + " " * center_space)

print_heart_pattern("NAME")
