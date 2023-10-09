    
def nearest_sq(n):
# pass
    a = int(n**0.5)
    if( a == n**0.5):
        return a**2
    
    b = (a+1)**2
    c = (a-1)**2
    
    if(abs(b-n)<abs(c-n)):
        if(abs(b-n)<abs(a**2-n)):
            return b
        else:
            return a**2
    else:
        if(abs(c-n)<abs(a**2-n)):
            return c
        else:
            return a**2
    
def bouncing_ball(h, bounce, window):
    # your code
    if(window>=h or bounce<=0 or bounce>=1 or h<=0):
        return -1
    hit = 1
    len = h
    len = len*bounce
    
    while len>window:
        hit=hit+2
        len = len*bounce
    
    return hit

def get_count(sentence):
    check = "aeiou"
    count = 0
    for i in sentence:
        for k in check:
            if (i==k):
                count=count + 1  
                break
    return count


def even_or_odd(number):
    if (number % 2):
        return "Odd"
    else :
        return "Even"
    

print(even_or_odd(3))



    