def solution(number):
    sum = 0
    for i in range(1,number):
        if i%3==0 or i%5==0:
            sum+=i
    return sum




def duplicate_encode(word):
    word = word.lower()  # 将字符串转换为小写字母
    result = ''
    for char in word:
        if word.count(char) > 1:
            result += ')'
        else:
            result += '('
    return result


def validBraces(string):
    stack = []  # 用于模拟栈的列表

    # 定义一个字典，将右括号映射到对应的左括号
    mapping = {')': '(', '}': '{', ']': '['}

    # 遍历输入字符串中的每个字符
    for char in string:
        if char in mapping:  # 如果是右括号
            # 如果栈为空或栈顶不匹配当前右括号，返回 False
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # 如果是左括号，将其入栈
            stack.append(char)

    # 最终，如果栈为空，说明所有括号都匹配，否则无效
    return not stack

def disemvowel(string_):
    vowels = "AEIOUaeiou"  # 定义一个包含所有元音字母的字符串
    result = ""
    for char in string_:
        if char not in vowels:
            result += char
    return result

print(solution(16))
