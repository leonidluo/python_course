def count_developers(lst):

    european_js_devs = list(filter(lambda dev: dev['continent'] == 'Europe' and dev['language'] == 'JavaScript', lst))
    
    return len(european_js_devs)



############################
def zero(func=None):
    return func(0) if func else 0

def one(func=None):
    return func(1) if func else 1

def two(func=None):
    return func(2) if func else 2

def three(func=None):
    return func(3) if func else 3

def four(func=None):
    return func(4) if func else 4

def five(func=None):
    return func(5) if func else 5

def six(func=None):
    return func(6) if func else 6

def seven(func=None):
    return func(7) if func else 7

def eight(func=None):
    return func(8) if func else 8

def nine(func=None):
    return func(9) if func else 9

def plus(num):
    return lambda x: x + num

def minus(num):
    return lambda x: x - num

def times(num):
    return lambda x: x * num

def divided_by(num):
    return lambda x: x // num

#################################


def shorten_number(suffixes, base):
    def filter_func(num):
            if not isinstance(num, str):
                return str(num)
            if not num.isdigit():
                return str(num)
            
            num = int(num)
            for suffix in suffixes:
                if num > base:
                    num /= base
                else:
                    return f"{int(num)}{suffix}"   
                
            return f"{int(num*base)}{suffix}"       
        
    return filter_func


def oldest_developers(lst):
    # 使用 max 函数，比较的关键是 'age'，同时保留原始顺序
    max_age = max(lst, key=lambda dev: dev['age'])['age']
    # 使用列表推导式筛选出所有最年长的开发人员，保留原始顺序
    oldest_devs = [dev for dev in lst if dev['age'] == max_age]
    
    return oldest_devs


filter1 = shorten_number(['', 'k', 'm'], 1000)

print(filter1(234324))  # 输出: '234k'
print(filter1('98234324'))  # 输出: '98m'
print(filter1([1, 2, 3]))  # 输出: '[1, 2, 3]'
