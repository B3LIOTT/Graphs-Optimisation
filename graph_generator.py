import random
import sys


def generateGraph1(proba: float, size: tuple[int, int]):

    with open(f"graphes/graph_{proba}_{size[0]}_{size[1]}.txt", 'w') as f:
        f.write(f"{size[0]} {size[1]}\n")
        s = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        t = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        for i in range(size[0]):
            for j in range(size[1]):
                if (i, j) == s:
                    f.write("2 ")
                elif (i, j) == t:
                    f.write("3 ")

                elif random.randint(0, 100) < proba*100:
                    f.write("1 ")
                else:
                    f.write("0 ")
            f.write("\n")


def generateGraph2():
    raise NotImplementedError


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage to generate a graph for the shortest path problem: python graph_generator.py 1 <proba> <size x> <size y>")
        print("Usage to generate a graph for the traveling salesman problem: python graph_generator.py 2 <proba> <nodes number> <edges number>")
        sys.exit(1)

    if int(sys.argv[1]) == 1:
        proba = float(sys.argv[2])
        size = (int(sys.argv[3]), int(sys.argv[4]))
        generateGraph1(proba=proba, size=size)
    else:
        proba = float(sys.argv[2])
        nodes_number = int(sys.argv[3])
        edges_number = int(sys.argv[4])
        generateGraph2()

