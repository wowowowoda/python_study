def trim(s) :
    if(s == ""):
        return s 
    if(s[0] == " ") :
        return trim(s[1:])
    if(s[-1] == " ") :
        return trim(s[:-1])
     
    return s 

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')