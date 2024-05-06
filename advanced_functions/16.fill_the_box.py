def fill_the_box(height, width, length, *args):
    size = height * width * length
    result = ''
    for boxes in args:
        if boxes == 'Finish':
            break
        size -= int(boxes)

    if size > 0:
        result += f"There is free space in the box. You could put {size} more cubes."
    else:
        result += f"No more free space! You have {abs(size)} more cubes."

    return result

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))