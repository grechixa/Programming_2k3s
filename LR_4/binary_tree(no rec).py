from collections import deque

# Root = 5; height = 6, left_leaf = root^2, right_leaf = root-2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; # главный корень
        self.left = left; # мама
        self.right = right; # папа
        
# ФУНКЦИЯ ПОСТРОЕНИЯ ДЕРЕВА
def build_tree():
    root = TreeNode(5) # root = 5

    queue = deque([root])
    current_height = 1
    max_height = 6

    while queue and current_height <= max_height:
        level_size = len(queue) # сколько узлов(node) на текущем уровне

        print(f"\n Переходим на уровень {current_height + 1}")
        print(f"Обрабатываем {level_size} узлов:")
        print("-" * 40)

        for _ in range(level_size):
            node = queue.popleft() # берем первый узел из очереди

            # создаем потомков только если не достигли макс высоты
            left_val = node.val ** 2
            right_val = node.val - 2

            node.left = TreeNode(left_val)
            node.right = TreeNode(right_val) 

            print(f"Узел {node.val} -> Левый {left_val}, Правый {right_val}")

            # добавляем созданных потомков в очередь только если следующий уровень
            # не будет превышать макс высота

            if current_height + 1 < max_height:
                queue.append(node.left) # ставим левого потомка в конец очереди
                queue.append(node.right) # ставим правого потомка в конец очереди

        current_height += 1

    print(f"\nДостигнута максимальная выcота {max_height}")
    return root

# ФУНКЦИЯ ВЫВОДА ДЕРЕВА
def print_tree(root, max_levels=6):
    if not root:
        print("Дерево пустое")
        return
    
    # создание очереди для обхода
    queue = deque([root])
    level_number = 1

    # пока в очереди есть узлы
    while queue and level_number <= max_levels:
        level_size = len(queue) # сколько узлов на текущем уровне
        level_value = [] # хранение значение текущего уровня

        print(f"Текущий уровень {level_number:2}: ", end="")

        # для всех узлов на одном уровне
        for _ in range(level_size):
            node = queue.popleft()
            level_value.append(str(node.val))

            if level_number < max_levels:
                # если есть левый потомок, добавляем в очередь 
                if node.left:
                    queue.append(node.left)
                # если есть правый потомок, добавляем в очередь
                if node.right:
                    queue.append(node.right)

        print(" -> ".join(level_value))
        level_number += 1

def tree_height(node):
    # вычисление высоты дерева
    if not node:
        return 0
    
    # высота = 1 + макс высота из левого и правого поддеревьев
    left_height = tree_height(node.left) # высота левого поддерева
    right_height = tree_height(node.right) # высота правого поддерева

    return 1 + max(left_height, right_height)



# === Запуск программы ===
root = build_tree()
print_tree(root)