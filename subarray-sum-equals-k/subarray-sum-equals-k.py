class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # use a default dict initializing to ints, so we can just
        # += on it. If our key wasn't there, we get a default of 0.
        previous_totals = defaultdict(int)
        total_sum = total_count = 0
        for value in nums:
            # Count each time we have seen the total_sum, it is
            # important to do this before value is added, or else
            # we will miss our array start of 0, and need the
            # conditional if total_sum = k:
            previous_totals[total_sum] += 1
            total_sum += value
            # Each time we see the difference (total_sum -k) in our
            # previous totals, this indicates a sub array start.
            # It is very important to note that because negative
            # numbers (and 0) can exist in they array, this means
            # we could have more than one start position for the
            # difference in question, so we have to += the total
            # times we have seen that previous_total, and not
            # simply += 1 (which would work if the array was all > 0)
            total_count += previous_totals.get(total_sum - k, 0)
        return total_count

