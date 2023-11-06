def spin_words(sentence):
    words = sentence.split()
    anser = []
    for word in words :
        if len(word) >= 5:
            # 如果单词长度大于等于5，就反转单词
            anser.append(word[::-1])
        else:
            anser.append(word)
    return " ".join(anser)


def find_outlier(integers):
    fg = 0
    fg2 = 0 
    for i in integers:
        if i % 2 == 0:
            fg = fg + 1
        else :
            fg2 = fg2 + 1
        if fg >= 2 : 
            fg2=0
            break
        if fg2 >=2 :
            fg = 0
            break
      
    if fg  :        #奇数为独数
        for i in integers:
            if i % 2 == 1:
                return i
    else :             #偶数为独数
        for i in integers:
            if i % 2 == 0:
                return i
    


def is_pangram(s):
    s=s.lower()
    abc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            abc[ord(char)-ord('a')] = 1 
    for ans in abc :
        if ans != 1 :
            return False
        
    return True 


def validate_sudoku(board):
    checkfg = [1,1,1,1,1,1,1,1,1]
    
    
    for row in range(9):
        for ro in range(9):
            if board[row][ro]<=0 or board[row][ro] > 9:
                return False
            checkfg[board[row][ro]-1]=0
        for check in checkfg:
            if check == 1:
                return False
        checkfg[:] = [1] * len(checkfg) #恢复check数组
        
    
    # 检查每一列
    for col in range(9):
        for co in range(9):
            checkfg[board[co][col]-1]=0
        for check in checkfg:
            if check == 1:
                return False
        checkfg[:] = [1] * len(checkfg) #恢复check数组

    # 检查每一个3x3子网格
    for d in range(3):
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    checkfg[board[3*d+i][3*k+j]-1]=0
            for check in checkfg:
                if check == 1:
                    return False
            checkfg[:] = [1] * len(checkfg) #恢复check数组

    return True




# 测试
sudoku_board =[[8,4,7,2,6,5,1,0,3],
				  [1,3,6,7,0,8,2,4,5],
				  [0,5,2,1,4,3,8,6,7],
				  [4,2,0,6,7,1,5,3,8],
				  [6,7,8,5,3,2,0,1,4],
				  [3,1,5,4,8,0,7,2,6],
				  [5,6,4,0,1,7,3,8,2],
				  [7,8,1,3,2,4,6,5,0],
				  [2,0,3,8,5,6,4,7,1]]
sudoku_board2  =  [
    [5,3,4,6,7,8,9,1,2],
	[6,7,2,1,9,5,3,4,8],
	[1,9,8,3,4,2,5,6,7],
	[8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

result = validate_sudoku(sudoku_board)
print(result)  # 输出：True
