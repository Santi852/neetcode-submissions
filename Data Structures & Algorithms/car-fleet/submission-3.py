class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        arrival = 0
        count = 1
        for p, s in cars:
            time = (target - p) / s
            if arrival == 0:
                arrival = time
            elif arrival >= time:
                continue
            elif arrival < time:
                count += 1
                arrival = time
        return count




        
        