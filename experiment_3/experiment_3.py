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

print(solution(16))
