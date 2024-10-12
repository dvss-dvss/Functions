def arges(*args):
    negative = []
    positive = []
    for arg in args:
        if arg >= 0:
            positive.append(arg)
        elif arg < 0:
            negative.append(arg)
    sorted_positive_tuple = sorted(positive)
    sorted_negative_tuple = sorted(negative,reverse = True)
    return sorted_negative_tuple, sorted_positive_tuple

print(arges(25,52,-7,53,-14,-3,20,-22,-2))