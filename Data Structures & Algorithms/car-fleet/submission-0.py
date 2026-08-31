class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position in descending order
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        stack = []
        for p, s in pair:
            # Calculate time to reach target
            time = (target - p) / s
            stack.append(time)
            
            # If current car reaches earlier/same time as car ahead, 
            # it merges into the fleet ahead (pop current time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)