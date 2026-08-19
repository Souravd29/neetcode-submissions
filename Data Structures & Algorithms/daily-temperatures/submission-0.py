class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while output and temp>temperatures[output[-1]]:
                j = output.pop()
                result[j] = i - j
            output.append(i)

        return result