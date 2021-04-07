import string


class RouteTrieNode:
    def __init__(self, path: string = '', handler: string = ''):
        self.path = path
        self.handler = handler
        self.children: [path, RouteTrieNode] = {}


class Router:
    def __init__(self, root_handler: string = '', not_found_handler: string or None = None):
        self.root = RouteTrieNode('', root_handler)
        self.not_found_handler = not_found_handler

    def validate_handler(self, handler):
        if not handler:
            raise Exception("handler is not valid")

    def validate_path(self, path: string):
        if path is None or (path[0] != '/' and len(path) == 1):
            raise Exception("path is not valid")

    def check_if_handler_added(self, path):
        found_handler = self.search_handler(path)

        if found_handler:
            raise Exception("handler is already added")


    def is_root_handler(self, path: string) -> bool:
        return len(path) == 1 and path[0] == '/'

    def add_handler(self, path: string, handler: string):
        self.validate_handler(handler)
        self.validate_path(path)
        self.check_if_handler_added(path)

        valid_path = self.split_path(path)
        is_last = len(valid_path) - 1
        node = self.root

        for i, sub_path in enumerate(valid_path):
            if i == is_last:
                node.children[sub_path] = RouteTrieNode(sub_path, handler)
                return
            if sub_path in node.children:
                node = node.children[sub_path]
            else:
                node.children[sub_path] = RouteTrieNode(sub_path)
                node = node.children[sub_path]

    def search_handler(self, path: string) -> string or None:
        self.validate_path(path)
        valid_path = self.split_path(path)
        is_last = len(valid_path) - 1
        node = self.root

        for i, sub_path in enumerate(valid_path):
            if sub_path not in node.children:
                return None
            if i == is_last:
                node: RouteTrieNode = node.children[sub_path]
                if node.handler:
                    return node.handler
                return None
            node = node.children[sub_path]
        return None

    def lookup(self, path: string) -> string:
        if self.is_root_handler(path):
            return self.root.handler

        found_handler = self.search_handler(path)
        if not found_handler:
            return self.not_found_handler
        return found_handler

    def split_path(self, path: string) -> list[string]:
        path_steps = path.split('/')
        if path_steps[-1] == '':
            return path_steps[1:-1]
        return path_steps[1:]


print("Test usual cases")
# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

print("\nTest add existing handler handler")
try:
    router.add_handler("/home/about", "about handler")
except Exception:
    print("passed")

print("\nTest invalid path")
try:
    router.lookup("")
except Exception:
    print("passed")