def removeDuplicates(s: str) -> str:

    cont = True
    clearTo = 0

    while cont:
        if len(s) == 0 or len(s) == 1:
            cont = False
            return ""
        for idx in range(clearTo, len(s)):

            if idx == len(s)-1:
                cont = False
                break

            if s[idx] == s[idx+1]:
                if idx < 1:
                    clearTo = 0
                else:
                    clearTo = idx - 1
                s = s[:idx]+s[idx+1:]
                s = s[:idx]+s[idx+1:]
                break

    return s


def isValid(s) -> bool:

    check = []

    for i in s:
        if i == "(" or i == "{" or i == "[":
            check.append(i)
        else:
            if len(check) > 0:
                test = check.pop()
            else:
                return False
            if i == ")" and test != "(":
                return False

            if i == "}" and test != "{":
                return False

            if i == "]" and test != "[":
                return False

    if len(check) > 0:
        return False
    else:

        return True


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)


print(tree.print_tree("preorder"))


def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
