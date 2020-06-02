a = 1
b = 2
total = 2

c = 1
while(c < 4000001):
    c = a + b
    
    a = b
    b = c
    
    if(c % 2 == 0):
        total += c
        
print("Total is", total)
