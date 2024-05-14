import random
import sys


class GraphGenerator:
    """
    Générateur de graphes selon la méthode de génération de graphes aléatoires de Erdos-Renyi
    """
    def __init__(self, proba: float, size: tuple[int, int]):
        self.proba = proba
        self.size = size

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


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python graph_generator.py <proba> <size x> <size y>")
        sys.exit(1)

    proba = float(sys.argv[1])
    size = (int(sys.argv[2]), int(sys.argv[3]))

    gg = GraphGenerator(proba=proba, size=size)
