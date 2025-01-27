"""task.py"""

# Завдання 1: Алгоритм для знаходження максимального значення у двійковому дереві пошуку або в AVL-дереві.
def get_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.key

# Завдання 2: Алгоритм для знаходження мінімального значення у двійковому дереві пошуку або в AVL-дереві.
def get_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

# Завдання 3: Алгоритм для знаходження суми всіх значень у двійковому дереві пошуку або в AVL-дереві.
def get_sum_nodes_values(node):
    if not node:
        return 0
    return node.key + get_sum_nodes_values(node.left) + get_sum_nodes_values(node.right)

# Клас для створення AVL-дерева:
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(y):
    x = y.left
    T3 = x.right
    x.right = y
    y.left = T3
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert(root, key):
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    return root

# Завдання 4: Реалізація структури даних для системи коментарів.
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []  # Список відповідей
        self.is_deleted = False  # Прапорець, чи був коментар видалений

    def add_reply(self, comment):
        self.replies.append(comment)  # Додати відповідь до коментаря

    def remove_reply(self):
        self.text = "Цей коментар було видалено."  # Заміна тексту на стандартне повідомлення
        self.is_deleted = True  # Помітити як видалений

    def display(self, level=0):
        # Виведення коментаря з усіма відступами на основі рівня ієрархії
        if not self.is_deleted:
            print("\t" * level + f"{self.author}: {self.text}")
        else:
            print("\t" * level + f"Цей коментар було видалено.")  # Виведення для видаленого коментаря
        for reply in self.replies:
            reply.display(level + 1)  # Рекурсивно вивести всі відповіді

# Основний код для тестування
if __name__ == "__main__":
    # Тестування AVL-дерева:
    root = None
    keys = [15, 10, 2, 20, 8, 12, 25, 18, 5]

    print("Вставка ключів у AVL-дерево:")
    for key in keys:
        root = insert(root, key)

    print("\nAVL-Дерево:")
    print(root)

    print("\nЗавдання 1: Максимальне значення у дереві")
    print("Максимальне значення у дереві:", get_max_value(root))

    print("\nЗавдання 2: Мінімальне значення у дереві")
    print("Мінімальне значення у дереві:", get_min_value(root))

    print("\nЗавдання 3: Сума всіх значень у дереві")
    print("Сума всіх значень у дереві:", get_sum_nodes_values(root))

    # Тестування системи коментарів
    print("\nЗавдання 4: Система коментарів")

    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видаляємо одну з відповідей
    reply1.remove_reply()

    # Виведення коментарів
    root_comment.display()
