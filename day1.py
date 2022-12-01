with open("day1_input.txt", "r") as f:
    print(max([sum(list(map(lambda n: int(n), x.split("\n")))) for x in f.read().split("\n\n")]))