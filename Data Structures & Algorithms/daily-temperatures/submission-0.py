class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            results = [0]*len(temperatures)
            stack = []
            for i in range(len(temperatures)):
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index_to_update = stack.pop()
                    results[index_to_update] = i - index_to_update
                stack.append(i)
            return results