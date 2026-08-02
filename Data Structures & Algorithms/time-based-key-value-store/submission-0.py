class TimeMap:
    #goal: design a time-based key-value data structure so store multiple values 
    #for the same key at different time stamps and retrieve the key's value at a certain timestamp
    #use binary serach for get, normal for set, and normal for init
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        bot = 0 
        values = self.store.get(key, [])

        top = len(values) - 1

        while bot <= top: 
            mid = bot + (top-bot) // 2
            if values[mid][1] <= timestamp: 
                res = values[mid][0]
                bot = mid + 1
            else: 
                top = mid - 1
        return res
            



