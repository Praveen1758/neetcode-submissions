class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of days

        for i, current_temp in enumerate(temperatures):
            # Resolve all previous colder days
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)

        return result