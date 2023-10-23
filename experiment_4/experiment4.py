def naughty_or_nice(data):
    naughty_count = 0
    nice_count = 0
    for mouth in data:
        for date ,status in data[mouth].items():
            if status == 'Naughty' :
                naughty_count +=1
            elif  status == 'Nice' :
                nice_count +=1  

    if naughty_count > nice_count:
        return "Naughty!"
    elif nice_count > naughty_count:
        return "Nice!"
    else:
        return "Nice!"
    



def get_pins(observed):
    # 定义数字的相邻关系
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    # 递归函数来生成所有可能的组合
    def generate_combinations(pin, remaining_digits):
        if not remaining_digits:
            combinations.append(pin)
        else:
            for neighbor in adjacent_digits[remaining_digits[0]]:
                generate_combinations(pin + neighbor, remaining_digits[1:])
    
    # 初始化结果数组
    combinations = []
    
    # 调用递归函数
    generate_combinations('', observed)
    
    return combinations

PROTEIN_DICT = {
    # Phenylalanine
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}
def protein(rna):
    anser = '' 
    i=0
    while i < len(rna):
        code = rna[i:i+3]
        acid = PROTEIN_DICT.get(code,'')
        if acid == 'Stop':
            break
        else :
            anser += acid
        i +=3
    return anser 

def fillable(stock, merch, n):
    if merch in stock:
        ans=stock.get(merch,'')
        if ans>=n:
            return True
        
    return False
