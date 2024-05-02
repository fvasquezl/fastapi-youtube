import os


class MyTree:
    def __init__(self, key, left, right1, right2):
        self.key = key
        self.left = left
        self.right1 = right1
        self.right2 = right2


def preorder(node):
    if node is not None:
        try:
            os.mkdir(node.key["mk"])
            print(f"Folder {node.key["mk"]} created")
        except:
            print(f"Folder {node.key["mk"]} already exists")
            
        os.chdir(node.key["cd"])
        preorder(node.left)
        preorder(node.right1)
        preorder(node.right2)


my_tree = MyTree(
    {"mk": "app", "cd": "app"},
    MyTree(
        {"mk": "api", "cd": "api"},
        MyTree(
            {"mk": "schemas", "cd": "."},
            MyTree(
                {"mk": "v1", "cd": "v1"},
                MyTree({"mk": "endpoints", "cd": "."}, None, None, None),
                MyTree({"mk": "models", "cd": "../.."}, None, None, None),
                None,
            ),
            None,
            None,
        ),
        None,
        None,
    ),
    MyTree({"mk": "auth", "cd": "."}, None, None, None),
    MyTree({"mk": "core", "cd": ".."}, None, None, None),
)


preorder(my_tree)



