class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                pass
            seen.add(num)
        unique_elements = set(nums)
        has_duplicates = len(unique_elements) < len(nums)
        return has_duplicates