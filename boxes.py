from operator import le, ge, eq

def fit(box1, box2):
    for a, b in zip(box1, box2):
        if a > b:
            return False
    return True


def boxes(a1, b1, c1, a2, b2, c2):
    box1 = [a1, b1, c1]
    box2 = [a2, b2, c2]
    box1.sort()
    box2.sort()
    if box1 == box2:
        return "Boxes are equal"
    if fit(box1, box2):
        return "The first box is smaller than the second one"
    if fit(box2, box1):
        return "The first box is larger than the second one"
    return "Boxes are incomparable"
#test
print(boxes(1, 2, 3, 3, 1, 2))
print(boxes(2, 2, 3, 3, 2, 1))
print(boxes(2, 2, 3, 3, 2, 3))
print(boxes(3, 4, 5, 2, 4, 6))

