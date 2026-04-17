class TimeMap:
    def __init__(self):
        self.store = {} # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # you can avoid this by using a default dict
        if key not in self.store:
            self.store[key] = []
        # add it to the hashmap
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = "" # key
        # if it finds a match it will return its list 
        # if not it will return an empty list
        values = self.store.get(key, [])

        # bianry search
        left = 0 
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                # closest result we have seen so far
                result = values[mid][0]
                # slight optimization (found xact match)
                if values[mid][0] == timestamp:
                    return result
                left = mid + 1
            # value too big
            else:
                right = mid - 1

        return result

