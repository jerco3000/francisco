

def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


class cola:
    def __init__(self):
        self.items = []

    def ingresa(self, item):
        self.items.append(item)

    def primero(self):
        return self.items[0]

    def ultimo(self):
        return self.items[-1]

    def length(self):
        return len(self.items)

