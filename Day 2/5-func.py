def area_shapes (shape, *args):
    if shape == "circle":
        radius = args[0]
        area = 3.14 * radius ** 2
        return area
    elif shape == "rectangle":
        length = args[0]
        breadth = args[1]
        area = length * breadth
        return area
    elif shape == "triangle":
        base = args[0]
        height = args[1]
        area = 0.5 * base * height
        return area
    else:
        return "Invalid shape"