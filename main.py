def get_data():
    e_data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = (line[:len(line)] + line[len(line) + 1:]).split()
            for x in range(len(temp)):
                temp[x] = int(temp[x])
            e_data.append(temp)
            print(line, end='')
        print()
    return e_data


def create_adjacency_matrix(e_data):
    matrix = [0] * e_data[0][0]
    for x in range(e_data[0][0]):
        matrix[x] = [0] * e_data[0][0]

    for y in range(1, len(e_data)):
        matrix[e_data[y][0] - 1][e_data[y][1] - 1] = 1
        matrix[e_data[y][1] - 1][e_data[y][0] - 1] = 1
    return matrix


def close_height(matrix, number):
    for x in range(len(matrix)):
        matrix[x][number] = 0


def show_action(queue_value, counter_value=-1):
    if counter_value == -1:
        print("\t-\t|\t-\t|", end=" ")
    else:
        print("\t" + str(queue_value[-1] + 1) + "\t|\t" + str(counter_value) + "\t| ", end="")
    for x in range(len(queue_value)):
        print((queue_value[x] + 1), end=" ")
    print()


def get_position_of_neighbour(adjacency, number):
    for x in range(len(adjacency)):
        if adjacency[number][x] == 1:
            return x
    return -1


data = get_data()

adjacency_matrix = create_adjacency_matrix(data)

choice = int(input("Натисніть 1 для алгоритму пошуку вшир, 2 в глиб: "))
startPoint = int(input("Введіть з якої вершини почати обхід : "))
queue = [startPoint - 1]
close_height(adjacency_matrix, queue[0])
counter = 1
if choice == 1:
    print("Вершина |BFS\t|Вміст черги")
    print("----------------------------")
    show_action(queue, counter)

    while len(queue) != 0:
        position = get_position_of_neighbour(adjacency_matrix, queue[0])
        if position == -1:
            queue.remove(queue[0])
            show_action(queue)
        else:
            queue.append(position)
            close_height(adjacency_matrix, position)
            counter += 1
            show_action(queue, counter)
elif choice == 2:
    print("Вершина |DFS\t|Вміст черги")
    print("----------------------------")
    show_action(queue, counter)
    while len(queue) != 0:
        position = get_position_of_neighbour(adjacency_matrix, queue[-1])
        if position == -1:
            queue.remove(queue[-1])
            show_action(queue)
        else:
            queue.append(position)
            close_height(adjacency_matrix, position)
            counter += 1
            show_action(queue, counter)
else:
    print("Enter is incorrect!")