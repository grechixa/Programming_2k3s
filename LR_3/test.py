import unittest
from binary_tree import gen_bin_tree

class TestGenBinTree(unittest.TestCase):
    def test_height_zero(self):
        """Дерево с высотой 0 должно быть пустым."""
        self.assertEqual(gen_bin_tree(0, 10), {})

    def test_single_node(self):
        """Дерево с высотой 1 должно содержать только корень."""
        self.assertEqual(
            gen_bin_tree(1, 7),
            {'root': 7, 'left': {}, 'right': {}}
        )

    def test_example_from_doc(self):
        """Проверка примера из документации."""
        expected = {
            'root': 3,
            'left': {'root': 9, 'left': {}, 'right': {}},
            'right': {'root': 1, 'left': {}, 'right': {}}
        }
        self.assertEqual(gen_bin_tree(2, 3), expected)

    def test_default_parameters(self):
        """Проверка работы с параметрами по умолчанию."""
        tree = gen_bin_tree()
        self.assertIsInstance(tree, dict)
        self.assertIn('root', tree)
        self.assertIn('left', tree)
        self.assertIn('right', tree)

    def test_custom_parameters(self):
        """Проверка работы с произвольными параметрами."""
        tree = gen_bin_tree(3, 2)
        self.assertEqual(tree['root'], 2)
        self.assertIsInstance(tree['left'], dict)
        self.assertIsInstance(tree['right'], dict)

if __name__ == '__main__':
    unittest.main()