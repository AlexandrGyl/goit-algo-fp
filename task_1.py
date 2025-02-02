import random

class Node:
    def __init__(self, data: int = None):
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None 

    # Функція для додавання елемента в кінець списку
    def append(self, data: int):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            return
        last = self.head
        while last.next:  
            last = last.next
        last.next = new_node  
    
    # Функція для виведення елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Функція для сортування методом вставок
    def insertion_sort(self):
        if self.head is None:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list


    # Функція для об'єднання двох відсортованих списків
    def merge_sorted(self, list2):
        p1 = self.head
        p2 = list2.head
        merged_list = LinkedList()

        while p1 and p2:
            if p1.data < p2.data:
                merged_list.append(p1.data)
                p1 = p1.next
            else:
                merged_list.append(p2.data)
                p2 = p2.next

        while p1:
            merged_list.append(p1.data)
            p1 = p1.next

        while p2:
            merged_list.append(p2.data)
            p2 = p2.next

        return merged_list


# Функція генерації випадкового списку
def generate_list(size, start, end):
    return random.choices(range(start, end), k=size)


print("Робота з однозв'язним списком" "\n" "Генеруємо випадковий список чисел")
start = int(input("Ведіть початкове число для генерації: "))
end = int(input("Ведіть кінцеве число для генерації: "))
size = int(input("Ведіть кількість елементів у списку: "))

# Генерація списку
random_list = generate_list(size, start, end)


list1 = LinkedList()
for value in random_list:
    list1.append(value)

print("\nСписок перед сортуванням:")
list1.print_list()

print("\nСписок після сортування вставками:")
list1.print_list()

print("Список після реверсування:")
list1.reverse()
list1.print_list()

# Створення другого списку для злиття
list2 = LinkedList()
for value in random_list[::-1]:
    list2.append(value)

print("\nСписок 2 перед сортуванням:")
list2.print_list()

list2.insertion_sort()

print("\nСписок 2 після сортування вставками:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = list1.merge_sorted(list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()