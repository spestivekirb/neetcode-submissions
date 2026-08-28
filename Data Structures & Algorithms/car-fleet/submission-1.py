class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos + speed * time = target
        # time = (target - pos) / speed
        infoArray = sorted(zip(position, speed), reverse=True)
        stack = []
        fleets = 1
        for car in infoArray:
            if not stack:
                stack.append(car)
            else:
                leadingTime = (target - stack[-1][0])/stack[-1][1]
                trailingTime = (target - car[0])/car[1]

                if trailingTime > leadingTime:
                    fleets += 1
                    stack.append(car)
        return fleets







