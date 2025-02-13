class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value
    
dll = DoublyLinkedList()

# Testando inserção no início
print("Adicionando 10 ao início")
dll.add_to_front(10)
print("Head:", dll.head.value, "| Tail:", dll.tail.value)  # Deve ser 10 | 10

print("Adicionando 20 ao início")
dll.add_to_front(20)
print("Head:", dll.head.value, "| Tail:", dll.tail.value)  # Deve ser 20 | 10

# Testando inserção no final
print("Adicionando 30 ao final")
dll.add_to_end(30)
print("Head:", dll.head.value, "| Tail:", dll.tail.value)  # Deve ser 20 | 30

# Testando remoção do início
print("Removendo do início:", dll.remove_from_front())  # Deve imprimir 20
print("Head:", dll.head.value, "| Tail:", dll.tail.value)  # Deve ser 10 | 30

# Testando remoção do final
print("Removendo do final:", dll.remove_from_end())  # Deve imprimir 30
print("Head:", dll.head.value, "| Tail:", dll.tail.value)  # Deve ser 10 | 10

# Testando remoção até esvaziar a lista
print("Removendo do início:", dll.remove_from_front())  # Deve imprimir 10
print("Head:", dll.head, "| Tail:", dll.tail)  # Deve ser None | None

# Testando remoção em lista vazia
print("Tentando remover do início em lista vazia:", dll.remove_from_front())  # Deve imprimir None
print("Tentando remover do final em lista vazia:", dll.remove_from_end())  # Deve imprimir None
