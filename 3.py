def is_even(number):
    lst = []
    for i in str(number):
        lst+=i
    print(lst)
    print(lst[-1])
    last_num = int(lst[-1])
    if last_num == 0 or last_num == 2 or last_num == 4 or last_num == 6 or last_num == 8:
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
