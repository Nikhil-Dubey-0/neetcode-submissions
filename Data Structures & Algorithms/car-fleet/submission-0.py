class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = dict(zip(position, speed))
        positions = reversed(sorted(position))
        fleet = 0
        time_x = 0
        for position in positions:
            time = (target-position)/cars[position]
            if time > time_x:
                time_x = time
                fleet+=1
        return fleet
