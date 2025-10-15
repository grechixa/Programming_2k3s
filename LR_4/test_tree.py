import unittest
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_specific_tree():
    """Исходная функция построения дерева"""
    root = TreeNode(5)
    queue = deque([root])
    current_height = 1
    max_height = 6
    
    while queue and current_height < max_height:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            left_val = node.val ** 2
            right_val = node.val - 2
            node.left = TreeNode(left_val)
            node.right = TreeNode(right_val)
            if current_height + 1 < max_height:
                queue.append(node.left)
                queue.append(node.right)
        current_height += 1
    return root

class TestBinaryTree(unittest.TestCase):
    
    def test_root_value(self):
        """Тест: корень дерева должен быть равен 5"""
        tree = build_specific_tree()
        self.assertEqual(tree.val, 5)
    
    def test_root_children(self):
        """Тест: проверка непосредственных потомков корня"""
        tree = build_specific_tree()
        # Левый потомок = 5² = 25
        self.assertEqual(tree.left.val, 25)
        # Правый потомок = 5-2 = 3
        self.assertEqual(tree.right.val, 3)
    
    def test_tree_height(self):
        """Тест: высота дерева должна быть 6"""
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        
        tree = build_specific_tree()
        height = get_height(tree)
        self.assertEqual(height, 6)
    
    def test_left_child_formula(self):
        """Тест: левый потомок = родитель²"""
        tree = build_specific_tree()
        # Проверяем несколько уровней
        self.assertEqual(tree.left.val, 25)  # 5² = 25
        self.assertEqual(tree.left.left.val, 625)  # 25² = 625
        self.assertEqual(tree.right.left.val, 9)   # 3² = 9
    
    def test_right_child_formula(self):
        """Тест: правый потомок = родитель-2"""
        tree = build_specific_tree()
        # Проверяем несколько уровней
        self.assertEqual(tree.right.val, 3)  # 5-2 = 3
        self.assertEqual(tree.left.right.val, 23)  # 25-2 = 23
        self.assertEqual(tree.right.right.val, 1)  # 3-2 = 1
    
    def test_tree_structure(self):
        """Тест: проверка общей структуры дерева"""
        tree = build_specific_tree()
        
        # Проверяем, что дерево не пустое
        self.assertIsNotNone(tree)
        
        # Проверяем, что у корня есть оба потомка
        self.assertIsNotNone(tree.left)
        self.assertIsNotNone(tree.right)
        
        # Проверяем, что дерево имеет ожидаемую структуру
        self.assertEqual(tree.val, 5)
        self.assertEqual(tree.left.val, 25)
        self.assertEqual(tree.right.val, 3)

def count_nodes(node):
    """Вспомогательная функция для подсчета узлов"""
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Альтернативный запуск без unittest (простой вариант)
def simple_test():
    """Простой тест без фреймворка"""
    print("Запуск простых тестов:")
    
    tree = build_specific_tree()
    
    # Тест 1: Корень
    assert tree.val == 5, f"Ошибка: корень должен быть 5, получено {tree.val}"
    print("Тест 1 пройден: корень = 5")
    
    # Тест 2: Потомки корня
    assert tree.left.val == 25, f"Ошибка: левый потомок должен быть 25, получено {tree.left.val}"
    assert tree.right.val == 3, f"Ошибка: правый потомок должен быть 3, получено {tree.right.val}"
    print("Тест 2 пройден: потомки корня корректны")
    
    # Тест 3: Формулы
    assert tree.left.left.val == 625, "Ошибка: формула левого потомка не работает"
    assert tree.left.right.val == 23, "Ошибка: формула правого потомка не работает"
    print("Тест 3 пройден: формулы работают корректно")
    
    # Тест 4: Количество узлов (для высоты 6 должно быть 63 узла в полном бинарном дереве)
    total_nodes = count_nodes(tree)
    assert total_nodes == 63, f"Ошибка: ожидалось 63 узла, получено {total_nodes}"
    print("Тест 4 пройден: количество узлов корректно")
    
    print("\nВсе тесты пройдены успешно!")

if __name__ == "__main__":
    # Запуск простых тестов
    simple_test()
    
    print("\n" + "="*50)
    
    # Запуск unittest (более подробные тесты)
    print("Запуск unittest...")
    unittest.main(argv=[''], verbosity=2, exit=False)