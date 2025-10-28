'''Custom DSA Practice & Interview Questions
 A set of 60 original coding problems covering core Data Structures and Algorithms topics similar 
in style and depth to the provided dsa_practice.py. Each problem includes:

1.Problem description

2.Python implementation

3.Example usage

4.Time and space complexity notes

Arrays & Strings (10) — Questions and Solutions
1. Find First Unique Character
Problem: Find the first non-repeating character in a string and return its index. If none exists, return -1.

python'''
def first_unique_char(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    return -1

# Example:
print(first_unique_char("leetcode"))  # Output: 0
Time Complexity: O(n), Space Complexity: O(1)

'''2. Contains Duplicate II
Problem: Given an array, check if any value appears at least twice within k indices.

python'''
def contains_nearby_duplicate(nums, k):
    pos = {}
    for i, num in enumerate(nums):
        if num in pos and i - pos[num] <= k:
            return True
        pos[num] = i
    return False

print(contains_nearby_duplicate([1,2,3,1], 3))  # Output: True
'''3. Rotate Image (Matrix)
Problem: Rotate an n x n 2D matrix 90 degrees clockwise in place.

python'''
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

# Example:
mat = [[1,2,3],[4,5,6],[7,8,9]]
rotate(mat)
print(mat)  # Output: [[7,4,1],[8,5,2],[9,6,3]]
'''4. Intersection of Two Arrays II
Problem: Given two integer arrays, return their intersection.

python'''
from collections import Counter
def intersect(nums1, nums2):
    counts = Counter(nums1)
    res = []
    for num in nums2:
        if counts[num] > 0:
            res.append(num)
            counts[num] -= 1
    return res

print(intersect([1,2,2,1], [2,2]))  # Output: [2,2]
'''5. Maximum Product of Three Numbers
Problem: Find maximum product of any three numbers in an array.

python'''
def maximum_product(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(maximum_product([1,2,3,4]))  # Output: 24
'''6. Valid Anagram
Problem: Check if two strings are anagrams.

python'''
def is_anagram(s,t):
    return sorted(s)==sorted(t)

print(is_anagram("anagram", "nagaram"))  # Output: True
'''7. Plus One
Problem: Add one to a number represented as an array of digits.

python'''
def plus_one(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits

print(plus_one([1,2,9]))  # Output: [1,3,0]
'''8. Move Zeroes
Problem: Move all zeroes in array to the end while maintaining order.

python'''
def move_zeroes(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[j] = nums[j], nums[i]
            j+=1
    return nums

print(move_zeroes([0,1,0,3,12]))  # Output: [1,3,12,0,0]
'''9. Reverse String
Problem: Reverse a list of characters.

python'''
def reverse_string(s):
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left+=1
        right-=1

arr = ['h','e','l','l','o']
reverse_string(arr)
print(arr)  # Output: ['o','l','l','e','h']
'''10. Valid Palindrome
Problem: Check if string is palindrome ignoring non-alphanumeric chars.

python'''
def is_palindrome(s):
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    return filtered_chars == filtered_chars[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True

'''Linked Lists (8) — Questions and Solutions
1. Reverse a Linked List
Problem: Reverse a singly linked list.

python'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Example: 
# Input: 1->2->3->None 
# Output: 3->2->1->None
'''2. Detect Cycle in Linked List
Problem: Detect if a linked list has a cycle using Floyd’s cycle-finding algorithm.

python'''
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
'''3. Merge Two Sorted Linked Lists
Problem: Merge two sorted linked lists into one sorted list.

python'''
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
'''4. Remove N-th Node From End of List
Problem: Remove the nth node from the end of a linked list.

python'''
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n+1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
'''5. Copy List with Random Pointer
Problem: Deep copy a linked list where each node has an additional random pointer.

python'''
def copy_random_list(head):
    if not head:
        return None
    curr = head
    while curr:
        nxt = curr.next
        copy = ListNode(curr.val)
        curr.next = copy
        copy.next = nxt
        curr = nxt
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    dummy = ListNode(0)
    copy_curr, curr = dummy, head
    while curr:
        copy_curr.next = curr.next
        curr.next = curr.next.next
        curr = curr.next
        copy_curr = copy_curr.next
    return dummy.next
'''6. Palindrome Linked List
Problem: Check if a linked list is a palindrome.

python'''
def is_palindrome_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
'''7. Flatten Multilevel Doubly Linked List
Problem: Flatten a multilevel doubly linked list.

python'''
def flatten(head):
    curr = head
    stack = []
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        if not curr.next and stack:
            curr.next = stack.pop()
            curr.next.prev = curr
        curr = curr.next
    return head
'''8. Intersection of Two Linked Lists
Problem: Find the node where two singly linked lists intersect.

python'''
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a


'''Stacks & Queues (5) — Questions and Solutions
1. Valid Parentheses
Problem: Given a string containing characters ()[]{}, determine if the input string is valid. Valid means brackets are closed in the correct order.

python'''
def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# Example:
print(is_valid_parentheses("()[]{}"))  # Output: True
'''2. Min Stack
Problem: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

python'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Example usage:
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.get_min())  # Output: -3
ms.pop()
print(ms.top())      # Output: 0
print(ms.get_min())  # Output: -2
'''3. Implement Queue using Stacks
Problem: Implement a queue using two stacks.

python'''
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

# Example:
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # Output: 1
print(q.pop())   # Output: 1
print(q.empty()) # Output: False
'''4. Sliding Window Maximum
Problem: Given an array and a sliding window size k, find max sliding window values.

python'''
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i, num in enumerate(nums):
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k-1:
            res.append(nums[dq[0]])
    return res

# Example:
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
'''5. Next Greater Element
Problem: Find for each element the next greater element to its right; if none, output -1.

python'''
def next_greater_elements(nums):
    res = [-1]*len(nums)
    stack = []
    for i in range(len(nums)-1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res

# Example:
print(next_greater_elements([4,5,2,10]))  # Output: [5,10,10,-1]


Trees & Graphs (12) — Questions and Solutions
'''1. Maximum Depth of Binary Tree
Problem: Find the maximum depth of a binary tree.

python'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Usage:
# root = TreeNode(...)
# print(max_depth(root))
'''2. Lowest Common Ancestor (Binary Tree)
Problem: Find the lowest common ancestor of two nodes in a binary tree.

python'''
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right
'''3. Diameter of Binary Tree
Problem: Find length of longest path between any two nodes in the tree.

python'''
def diameter_of_binary_tree(root):
    diameter = 0
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    dfs(root)
    return diameter
'''4. Serialize and Deserialize Binary Tree
Problem: Convert a binary tree to string and back.

python'''
def serialize(root):
    res = []
    def helper(node):
        if not node:
            res.append('X')
            return
        res.append(str(node.val))
        helper(node.left)
        helper(node.right)
    helper(root)
    return ','.join(res)

def deserialize(data):
    vals = iter(data.split(','))
    def helper():
        val = next(vals)
        if val == 'X':
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    return helper()
'''5. Binary Tree Level Order Traversal
Problem: Traverse a binary tree level by level.

python'''
from collections import deque

def level_order(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
'''6. Number of Islands (DFS)
Problem: Count islands ('1's connected horizontally or vertically) in a grid.

python'''
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(r,c):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]=='0':
            return
        grid[r][c] = '0'
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
    count=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1':
                dfs(r,c)
                count+=1
    return count
'''7. Clone Graph (DFS)
Problem: Deep copy an undirected graph.

python'''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    old_to_new = {}
    def dfs(n):
        if n in old_to_new:
            return old_to_new[n]
        copy = Node(n.val)
        old_to_new[n] = copy
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy
    return dfs(node) if node else None
'''8. Course Schedule (Topological Sort)
Problem: Determine if all courses can be finished given prerequisites.

python'''
from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0]*num_courses
    for u,v in prerequisites:
        graph[v].append(u)
        indegree[u] += 1
    queue = deque([i for i in range(num_courses) if indegree[i]==0])
    visited = 0
    while queue:
        node = queue.popleft()
        visited +=1
        for nei in graph[node]:
            indegree[nei]-=1
            if indegree[nei]==0:
                queue.append(nei)
    return visited==num_courses
'''9. Dijkstra’s Shortest Path
Problem: Find shortest path distances from a start node to all others.

python'''
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nei, w in graph[node]:
            if dist[node] + w < dist[nei]:
                dist[nei] = dist[node] + w
                heapq.heappush(pq, (dist[nei], nei))
    return dist
'''10. Kruskal’s Minimum Spanning Tree (MST)
Problem: Find MST of weighted graph via Kruskal’s algorithm.

python'''
class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py: 
            return False
        self.parent[px] = py
        return True

def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort(key=lambda x:x[2])
    mst = []
    for u,v,w in edges:
        if uf.union(u,v):
            mst.append((u,v,w))
    return mst
'''11. Prim’s MST
Problem: Generate minimum spanning tree using Prim’s algorithm.

python'''
import heapq

def prim_mst(graph):
    start = next(iter(graph))
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst = []
    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for to, weight in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (weight, v, to))
    return mst
'''12. Graph Cycle Detection (Directed)
Problem: Detect a cycle in a directed graph.

python'''
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for nei in graph[node]:
            if nei not in visited and dfs(nei):
                return True
            elif nei in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    for node in graph:
        if node not in visited and dfs(node):
            return True
    return False

'''Dynamic Programming (10) — Questions and Solutions
1. Fibonacci Sequence
Problem: Return the nth Fibonacci number.

python'''
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibonacci(10))  # Output: 55
'''2. Longest Common Subsequence (LCS)
Problem: Find length of longest subsequence common to two strings.

python'''
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(lcs("abcde", "ace"))  # Output: 3
'''3. 0/1 Knapsack
Problem: Maximize value with item weights constrained by capacity.

python'''
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

print(knapsack([1,2,3], [6,10,12], 5))  # Output: 22
'''4. Coin Change
Problem: Find minimum coins needed to make amount from coin denominations.

python'''
def coin_change(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1,2,5], 11))  # Output: 3
'''5. Minimum Path Sum in Grid
Problem: Find minimum path sum from top-left to bottom-right of a grid.

python'''
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]

print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
'''6. Longest Increasing Subsequence (LIS)
Problem: Longest strictly increasing subsequence length.

python'''
def lis(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp) if dp else 0

print(lis([10,9,2,5,3,7,101,18]))  # Output: 4
'''7. Edit Distance
Problem: Minimum operations to convert one string to another.

python'''
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

print(edit_distance("horse", "ros"))  # Output: 3
'''8. Maximum Product Subarray
Problem: Find contiguous subarray with maximum product.

python'''
def max_product_subarray(nums):
    max_prod = min_prod = res = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        res = max(res, max_prod)
    return res

print(max_product_subarray([2,3,-2,4]))  # Output: 6
'''9. House Robber
Problem: Max amount robbed without alert (no two adjacent houses).

python'''
def house_robber(nums):
    if not nums: return 0
    n = len(nums)
    dp = [0]*(n+1)
    dp[1] = nums[0]
    for i in range(2, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
    return dp[n]

print(house_robber([1,2,3,1]))  # Output: 4
'''10. Unique Paths
Problem: Number of unique paths from top-left to bottom-right grid moving only right or down.

python'''
def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

print(unique_paths(3, 7))  # Output: 28


'''Recursion & Backtracking (5) — Questions and Solutions
1. N-Queens
Problem: Place N queens on an N×N chessboard so no two queens attack each other.

python'''
def solve_n_queens(n):
    res = []
    def backtrack(row, diagonals, anti_diagonals, cols, board):
        if row == n:
            res.append([''.join(r) for r in board])
            return
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                continue
            cols.add(col)
            diagonals.add(diag)
            anti_diagonals.add(anti_diag)
            board[row][col] = 'Q'
            backtrack(row+1, diagonals, anti_diagonals, cols, board)
            board[row][col] = '.'
            cols.remove(col)
            diagonals.remove(diag)
            anti_diagonals.remove(anti_diag)
    backtrack(0, set(), set(), set(), [['.']*n for _ in range(n)])
    return res

print(solve_n_queens(4))
'''2. Generate Parentheses
Problem: Generate all combinations of well-formed parentheses given n pairs.

python'''
def generate_parentheses(n):
    res = []
    def backtrack(s='', left=0, right=0):
        if len(s) == 2*n:
            res.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)
    backtrack()
    return res

print(generate_parentheses(3))
'''3. Subsets
Problem: Return all possible subsets of a set.

python'''
def subsets(nums):
    res = []
    def backtrack(path, index):
        res.append(path)
        for i in range(index, len(nums)):
            backtrack(path+[nums[i]], i+1)
    backtrack([], 0)
    return res

print(subsets([1,2,3]))
'''4. Word Search
Problem: Given a 2D grid and a word, check if the word exists in the grid (adjacent cells horizontally or vertically).

python'''
def exist(board, word):
    ROWS, COLS = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
            return False
        tmp = board[r][c]
        board[r][c] = '#'
        res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
        board[r][c] = tmp
        return res
    
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(exist(board, "ABCCED"))  # Output: True
'''5. Combination Sum
Problem: Find all unique combinations where candidate numbers sum to target. Candidates may be chosen unlimited times.

python'''
def combination_sum(candidates, target):
    res = []
    def backtrack(path, start, total):
        if total == target:
            res.append(list(path))
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(path, i, total + candidates[i])
            path.pop()
    backtrack([], 0, 0)
    return res

print(combination_sum([2,3,6,7], 7))

'''Miscellaneous / Advanced (10) — Questions and Solutions
1. LRU Cache
Problem: Design a cache that evicts the least recently used item when capacity is exceeded.

python'''
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example:
lru = LRUCache(2)
lru.put(1,1)
lru.put(2,2)
print(lru.get(1))  # Output: 1
lru.put(3,3)       # Evicts key 2
print(lru.get(2))  # Output: -1
'''2. Serialize / Deserialize N-ary Tree
Problem: Convert an N-ary tree to a string and back.

python'''
class NTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def serialize_nary(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(str(node.val))
        res.append(str(len(node.children)))
        for child in node.children:
            dfs(child)
    dfs(root)
    return ','.join(res)

def deserialize_nary(data):
    vals = iter(data.split(','))
    def dfs():
        val = int(next(vals))
        size = int(next(vals))
        node = NTreeNode(val)
        for _ in range(size):
            node.children.append(dfs())
        return node
    return dfs()
'''3. Median of Two Sorted Arrays
Problem: Find the median of two sorted arrays in O(log(min(n,m))) time.

python'''
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    x, y = len(nums1), len(nums2)
    low, high = 0, x
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX
        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]
        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]
        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1
'''4. Trapping Rain Water
Problem: Given heights, calculate trapped rain water.

python'''
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    left, right = 0, n - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += max(0, right_max - height[right])
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
'''5. Word Ladder
Problem: Find minimum steps to convert beginWord to endWord with word list.

python'''
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))
    return 0

print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5
'''6. Decode Ways
Problem: Count ways to decode a numeric string to alphabets.

python'''
def num_decodings(s):
    if not s:
        return 0
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1
    for i in range(2, n+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[n]

print(num_decodings("226"))  # Output: 3
'''7. Maximum Sum Rectangle in 2D Matrix
Problem: Find max sum subrectangle in 2D matrix.

python'''
def max_sum_rectangle(matrix):
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    res = float('-inf')
    for top in range(rows):
        temp = [0]*cols
        for bottom in range(top, rows):
            for i in range(cols):
                temp[i] += matrix[bottom][i]
            curr_sum = max_sum = temp[0]
            for val in temp[1:]:
                curr_sum = max(val, curr_sum + val)
                max_sum = max(max_sum, curr_sum)
            res = max(res, max_sum)
    return res
'''8. Maximum Rectangle of 1s in Binary Matrix
Problem: Largest rectangle containing all ones in a binary matrix.

python'''
def maximal_rectangle(matrix):
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0]*cols
    max_area = 0
    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        stack = []
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
    return max_area
'''9. Sliding Window Median
Problem: Calculate median for every sliding window of size k.

python'''
import heapq

def median_sliding_window(nums, k):
    minH, maxH = [], []
    res = []
    for i, num in enumerate(nums):
        heapq.heappush(maxH, -num)
        heapq.heappush(minH, -heapq.heappop(maxH))
        if len(minH) > len(maxH):
            heapq.heappush(maxH, -heapq.heappop(minH))
        if i >= k - 1:
            res.append(-maxH[0] if k % 2 else (-maxH[0] + minH[0]) / 2)
            out = nums[i - k + 1]
            if out <= -maxH[0]:
                maxH.remove(-out)
                heapq.heapify(maxH)
            else:
                minH.remove(out)
                heapq.heapify(minH)
    return res
10. Top K Frequent Elements
Problem: Return k most frequent elements in an array.

python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # Output: [1,2]



''' 11. Rat in a maze 
Problem : You are given a maze of nxn. At 0,0 there is rat and you have to move it to n-1 x n-1. and you have to find the all possible paths
Python'''

def findPath(maze, n):
    res = []
    cur_path = []
    visited = [[False] * n for _ in range(n)]
    def f(row,col):
        if row >= n or col >= n or row < 0 or col < 0 or maze[row][col] == 0 or visited[row][col] == True:
            return
        if row == n-1 and col == n-1 :
            res.append("".join(cur_path))
            return 
        visited[row][col] = True

        # Right
        cur_path.append("R")
        f(row,col+1)
        cur_path.pop()

        # Left
        cur_path.append("L")
        f(row,col-1)
        cur_path.pop()

        # Up
        cur_path.append("U")
        f(row-1,col)
        cur_path.pop()

        # Down
        cur_path.append("D")
        f(row+1,col)
        cur_path.pop()

        visited[row][col] = False

    f(0,0)
    if not res:
        return "-1"
    return res
