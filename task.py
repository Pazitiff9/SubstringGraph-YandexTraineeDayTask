def generate_letter_combinations():
    """Создание буквосочетаний длинной 3"""
    meeting_rooms_count = int(input())
    combinations_array = [[] for _ in range(meeting_rooms_count)]
    for i in range(meeting_rooms_count):
        meeting_room = input()
        n = len(meeting_room)
        for c in range(0, n - 2):
            combinations_array[i].append(meeting_room[c:c + 3])
    return combinations_array


def adding_graph(graph, data):
    """Заполнение графа"""
    first = data[0]  # Wi
    for second in data[1:]:  # Wi+1
        if first in graph:
            if second in graph[first]:
                graph[first][second] += 1
            else:
                graph[first][second] = 1
        else:
            graph[first] = {second: 1}
        first = second
    return graph


if __name__ == "__main__":
    my_graph = {}

    # Заполнение графа + подсчет кол-ва вершин
    nodes = []
    for combinations in generate_letter_combinations():
        nodes.extend(combinations)
        my_graph = adding_graph(my_graph, combinations)

    # Кол-во вершин
    print(len(set(nodes)))

    # Кол-во ребер
    number_of_edges = 0
    for vert in my_graph.values():
        number_of_edges += len(vert)
    print(number_of_edges)

    # Вывод всех ребер с ценой
    for vert in my_graph:
        for edg, cost in my_graph[vert].items():
            print(f"{vert} {edg} {cost}")