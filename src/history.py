class History:
    def __init__(self):
        self.items = []

    def add(self, entry):
        self.items.append(entry)

    def get_last(self, n=10):
        return self.items[-n:][::-1]

    def clear(self):
        self.items.clear()
