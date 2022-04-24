def test_function(flag):
    if flag == None:
        return 1
    if flag:
        print(f'flag is {flag}')
        return 3
    return 2

