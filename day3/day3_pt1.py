with open("day3_input.txt", "r") as f:
    print(sum([z - 38 if z < 91 else z - 96 for z in [ord(''.join(set(y[0]).intersection(y[1]))) for y in [[x[:len(x)//2], x[len(x)//2:]] for x in f.read().split("\n")]]]))