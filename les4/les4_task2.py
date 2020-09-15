old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [old_list[a + 1] for a, b in enumerate(old_list[:-1]) if b < old_list[a + 1]]

print(new_list)
