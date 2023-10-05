ascii_art = {
    'H': '''
    H   H
    H   H
    HHHHH
    H   H
    H   H
    ''',
    'e': '''
    eeeee
    e
    eeee
    e
    eeeee
    ''',
    'l': '''
    l
    l
    l
    l
    lllll
    ''',
    'o': '''
    oooo
    o  o
    o  o
    o  o
    oooo
    ''',
    ' ': '''
    
    
    ''',
    'a': '''
    aaaaa
    a   a
    aaaaa
    a   a
    a   a
    ''',
    'c': '''
    ccccc
    c
    c
    c
    ccccc
    ''',
    'k': '''
    k   k
    k  k
    k k
    k  k
    k   k
    ''',
    't': '''
    ttttt
      t
      t
      t
      t
    ''',
    'b': '''
    bbbb
    b   b
    bbbb
    b   b
    bbbb
    ''',
    'r': '''
    rrrr
    r   r
    rrrr
    r r
    r   r
    ''',
    'f': '''
    fffff
    f
    ffff
    f
    f
    ''',
    's': '''
    ssss
    s
    ssss
        s
    ssss
    '''
}

text = "Hello Hacktoberfest"

for letter in text:
    if letter in ascii_art:
        print(ascii_art[letter])
    else:
        print('\n')
