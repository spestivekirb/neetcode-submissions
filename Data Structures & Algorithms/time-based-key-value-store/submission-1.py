class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps strictly increase means we assume sorted
        self.map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        valuelist = self.map[key]

        l = 0
        r = len(valuelist) - 1
        ans = ""

        while l <= r:
            m = (l + r) // 2

            if valuelist[m][0] <= timestamp:
                ans = valuelist[m][1]
                l = m + 1
            else:
                r = m - 1
            

        return ans

        
