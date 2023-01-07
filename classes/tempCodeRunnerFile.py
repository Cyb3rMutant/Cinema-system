def wrap_by_word(s, n):
    '''returns a string where \\n is inserted between every n words'''
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret


x = wrap_by_word(
    'There is a dog and fox fighting in the park and there is an apple falling down.', 4)
print(x)
