# -*- coding: utf-8 -*-
# @Author  : JUN
# @Time    : 2022/7/24 16:26
# @Software: PyCharm

# From leetcode 20.Valid Parentheses(https://leetcode.cn/problems/valid-parentheses)

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

from Stack.stack import Stack


def brace_match(s: str) -> bool:
    stack = Stack()
    for c in s:
        if c in ["(", "[", "{"]:
            stack.push(c)

        else:
            if stack.isEmpty():
                return False
            elif c == ")":
                if not stack.pop() == "(":
                    return False
            elif c == "]":
                if not stack.pop() == "[":
                    return False
            elif c == "}":
                if not stack.pop() == "{":
                    return False

    return stack.isEmpty()


if __name__ == '__main__':
    s1 = "[]{}[]()"  # True
    s2 = "{}[(())][][[][][{}}}}"  # False
    s3 = "{}])()"  # False
    for s in [s1, s2, s3]:
        print(brace_match(s))
