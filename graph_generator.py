import random
import sys


def generateGraph1(proba: float, size: tuple[int, int]):
    try:
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

    except Exception as e:
        print("Error while generating the graph: ", e)
        sys.exit(1)


def generateGraph2(proba: float, nodes_number: int, edges_number: int):
    try :
        with open(f"graphes/graph_{proba}_{nodes_number}_{edges_number}.txt", 'w') as f:
            f.write(f"{nodes_number} {edges_number}\n")
            for i in range(edges_number):
                node1 = random.randint(0, nodes_number - 1)
                node2 = random.randint(0, nodes_number - 1)
                while node1 == node2:
                    node2 = random.randint(0, nodes_number - 1)
                cost = random.randint(1, 100)
                f.write(f"{node1} {node2} {cost}\n")

    except Exception as e:
        print("Error while generating the graph: ", e)
        sys.exit(1)



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
        generateGraph2(proba=proba, nodes_number=nodes_number, edges_number=edges_number)

