def nextGreaterElement(nums1, nums2):
    stack = []
    nge_map = {}

    for num in nums2:
        while stack and stack[-1] < num:
            prev = stack.pop()
            nge_map[prev] = num
        stack.append(num)

    # 남은 건 더 큰 수가 없는 것
    for num in stack:
        nge_map[num] = -1

    return [nge_map[num] for num in nums1]