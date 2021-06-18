class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(numbers)):
            first = numbers[i]
            second = target - numbers[i]
            if second in numbers:
                second_index = numbers.index(second)+1
                if (i+1 in res and second_index in res) or i+1==second_index:
                    continue
                if i+1<second_index:
                    res.append(i+1)
                    res.append(second_index)
                else:
                    res.append(second_index)
                    res.append(i+1)

        return res