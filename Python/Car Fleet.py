class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)))[::-1]
        stack = []
        for i, car in enumerate(cars):
            stack.append((target - car[0]) / car[1])
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)