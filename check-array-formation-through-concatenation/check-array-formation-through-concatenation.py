class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        p_len = len(pieces)
        pieces.sort()

        i = 0
        while i < n:
            left = 0
            right = p_len - 1
            found = -1
            # use binary search to find target piece:
            while left <= right:
                mid = (left + right)//2
                if pieces[mid][0] == arr[i]:
                    found = mid
                    break
                elif pieces[mid][0] > arr[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            if found == -1:
                return False
            # check target piece
            target_piece = pieces[found]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True
            