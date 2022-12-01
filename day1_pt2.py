with open("day1_input.txt", "r") as f:
    print(sum(sorted([sum(list(map(lambda n: int(n), x.split("\n")))) for x in f.read().split("\n\n")])[-3:]))