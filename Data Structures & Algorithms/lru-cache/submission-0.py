class LRUCache:
    def __init__(self, capacity: int):
        self.n = capacity
        self.size = []
        self.maps = {}

    def get(self, key: int) -> int:
        if key in self.maps:
            self.size.remove(key)
            self.size.append(key)
            return self.maps[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.maps[key] = value
            self.size.remove(key)
            self.size.append(key)
        else:
            if len(self.size) == self.n:
                removed = self.size.pop(0)
                del self.maps[removed]
            self.size.append(key)
            self.maps[key] = value
