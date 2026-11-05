# ye hacker rank waly

# 1. Solve Me First
def solve_me_first():
    a = int(input())
    b = int(input())
    print(a + b)


# 2. Simple Array Sum
def simple_array_sum():
    input()
    print(sum(map(int, input().split())))


# 3. Compare the Triplets
def compare_the_triplets():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    alice = sum(x > y for x, y in zip(a, b))
    bob = sum(y > x for x, y in zip(a, b))
    print(alice, bob)


# 4. A Very Big Sum
def a_very_big_sum():
    input()
    print(sum(map(int, input().split())))


# 5. Diagonal Difference
def diagonal_difference():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    primary = sum(m[i][i] for i in range(n))
    secondary = sum(m[i][n - 1 - i] for i in range(n))
    print(abs(primary - secondary))


# 6. Plus Minus
def plus_minus():
    n = int(input())
    a = list(map(int, input().split()))
    print(f"{sum(x > 0 for x in a) / n:.6f}")
    print(f"{sum(x < 0 for x in a) / n:.6f}")
    print(f"{sum(x == 0 for x in a) / n:.6f}")


# 7. Staircase
def staircase():
    n = int(input())
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)


# 8. Mini-Max Sum
def mini_max_sum():
    a = sorted(map(int, input().split()))
    print(sum(a[:4]), sum(a[1:]))


# 9. Birthday Cake Candles
def birthday_cake_candles():
    input()
    a = list(map(int, input().split()))
    print(a.count(max(a)))


# 10. Time Conversion
def time_conversion():
    s = input().strip()
    hour = int(s[:2])
    suffix = s[-2:]
    rest = s[2:-2]
    if suffix == 'AM':
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12
    print(f"{hour:02d}{rest}")


# 11. Grading Students
def grading_students():
    n = int(input())
    for _ in range(n):
        g = int(input())
        if g >= 38 and (5 - g % 5) < 3:
            g += 5 - g % 5
        print(g)


# 12. Apple and Orange
def apple_and_orange():
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    print(sum(s <= a + d <= t for d in apples))
    print(sum(s <= b + d <= t for d in oranges))


# 13. Kangaroo
def kangaroo():
    x1, v1, x2, v2 = map(int, input().split())
    if v1 == v2:
        print("YES" if x1 == x2 else "NO")
    else:
        t = (x2 - x1) / (v1 - v2)
        print("YES" if t >= 0 and t == int(t) else "NO")


# 14. Between Two Sets
def between_two_sets():
    from math import gcd

    def lcm(x, y):
        return x * y // gcd(x, y)

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    L = 1
    for x in a:
        L = lcm(L, x)

    G = 0
    for x in b:
        G = gcd(G, x)

    print(sum(G % k == 0 for k in range(L, G + 1, L)))


# 15. Breaking the Records
def breaking_the_records():
    n = int(input())
    s = list(map(int, input().split()))
    hi = lo = s[0]
    hi_count = lo_count = 0
    for x in s[1:]:
        if x > hi:
            hi = x
            hi_count += 1
        elif x < lo:
            lo = x
            lo_count += 1
    print(hi_count, lo_count)


# ye yahan sey leet code shuru ho rye

from typing import List, Optional


# Definition for singly-linked list (used by problems 3 and 4)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. Two Sum
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i


# 2. Valid Parentheses
class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack


# 3. Reverse Linked List
class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


# 4. Merge Two Sorted Lists
class MergeTwoSortedLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next


# 5. Maximum Subarray
class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best