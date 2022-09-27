class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"(Val: {self.value}, Next: " + ("None" if self.next is None else str(self.next.value)) + ")"

    def __repr__(self):
        return self.__str__()



def solution_part1():
    with open("inputs/day23.txt", "r") as f:
        nodes = [Node(int(c)) for c in f.readline()[:-1]]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = nodes[0]

        current_node = nodes[0]

        nodes.sort(key=lambda x: x.value)

        for _ in range(100):
            # Remove 3 cups
            move_head = current_node.next
            move_body = move_head.next
            move_tail = move_body.next
            current_node.next = move_tail.next

            # Get destination cup
            destionation_node = nodes[current_node.value - 2]
            while destionation_node in (move_head, move_body, move_tail):
                destionation_node = nodes[destionation_node.value - 2]

            # Move 3 cups
            move_tail.next = destionation_node.next
            destionation_node.next = move_head

            current_node = current_node.next

        value = ""
        current_node = nodes[0].next
        while (current_node != nodes[0]):
            value += str(current_node.value)
            current_node = current_node.next

        print(value)


def solution_part2():
    with open("inputs/day23.txt", "r") as f:
        nodes = [Node(int(c)) for c in f.readline()[:-1]]
        nodes += [Node(i) for i in range(len(nodes) + 1, 1000001)]

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = nodes[0]

        current_node = nodes[0]

        nodes.sort(key=lambda x: x.value)

        for i in range(10000000):
            # Remove 3 cups
            move_head = current_node.next
            move_body = move_head.next
            move_tail = move_body.next
            current_node.next = move_tail.next

            # Get destination cup
            destionation_node = nodes[current_node.value - 2]
            while destionation_node in (move_head, move_body, move_tail):
                destionation_node = nodes[destionation_node.value - 2]

            # Move 3 cups
            move_tail.next = destionation_node.next
            destionation_node.next = move_head

            current_node = current_node.next

        print(nodes[0].next.value * nodes[0].next.next.value)

solution_part2()
