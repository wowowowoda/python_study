L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_scores(t):
    return t[1] 

a1 = sorted(L,key = by_name) 
a2 = sorted(L, key = by_scores)
print(a1) 
print(a2) 