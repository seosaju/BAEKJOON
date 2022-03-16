heights = []
for _ in range(9):
    heights.append(int(input()))


def print_heights(heights_list):
    for height in heights_list:
        print(height)


def get_heights(heights_list):
    total = sum(heights_list)
    for i in range(len(heights_list)):
        for j in range(i + 1, len(heights_list)):
            if total - (heights_list[i] + heights_list[j]) == 100:
                val_i, val_j = heights_list[i], heights_list[j]
                heights_list.remove(val_i)
                heights_list.remove(val_j)
                heights_list.sort()
                return heights_list


print_heights(get_heights(heights))
