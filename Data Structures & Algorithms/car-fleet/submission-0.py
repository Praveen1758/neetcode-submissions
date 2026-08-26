class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair positions with speeds and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time = 0.0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            # If this car takes more time than the fleet in front,
            # it forms a new fleet.
            if time > max_time:
                fleets += 1
                max_time = time
                
        return fleets