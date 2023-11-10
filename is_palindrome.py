def is_palindrome_compex(s):
    str_s = str(s)
    str_t = "" 
    for i in range(len(str_s)) :
        str_t += str_s[-1-i] 
    
    t = int(str_t) 
    return (t == s)

def is_palindrome(n):
    return str(n) == str(n)[::-1] 


it = filter(is_palindrome,range(1,100)) 
print(list(it))