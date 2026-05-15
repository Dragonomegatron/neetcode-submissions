class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        #Datatype is stack
        stack = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        #Sorting with Lambda functions
        pairs.sort(key = lambda x: x[0], reverse=True)
        #Logic
        for p,s in pairs:
            time_to_arrive = (target - p) / s
            if not stack or time_to_arrive > stack[-1]:
                stack.append(time_to_arrive)
        return len(stack)
