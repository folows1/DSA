from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # Cria um nó inicial auxiliar para começar a nova lista
        aux = ListNode()
        # Mantém uma referência para o início da nova lista
        current = aux
        
        # Enquanto uma das listas não for completamente percorrida
        while list1 and list2:
            # Compara os valores das duas listas e adiciona o menor à nova lista
            if list1.val < list2.val:
                current.next = list1  # Adiciona list1 à nova lista
                list1 = list1.next  # Avança para o próximo nó de list1
            else:
                current.next = list2  # Adiciona list2 à nova lista
                list2 = list2.next  # Avança para o próximo nó de list2
                
            # Avança a referência current para o próximo nó da nova lista
            current = current.next
        
        # Se uma das listas ainda tiver nós, adiciona os nós restantes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Retorna o próximo nó de 'aux', que é o início da nova lista
        return aux.next
