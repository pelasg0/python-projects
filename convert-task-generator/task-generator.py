

def binary_to_decimal(binary_number): 
    """Convert a binary to a decimal number"""
    res = 0
    elements = list(binary_number)
    elements.reverse()
    elements_val = []
    
    i = 0

    while i <= len(elements) - 1: 
        for element in elements: 
            if element == '1': 
                res += 2 ** i
                i+=1
            elif element == '0': 
                res += 0 
                i+=1
    return print(res) 

binary_to_decimal(input("Give a binary"))
