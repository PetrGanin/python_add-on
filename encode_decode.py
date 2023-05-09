s = 'Hello world Мир'
print(type(s))
sb = b'Hello world'
print(type(sb))
print(sb[1])


sm = s.encode('utf-8')
print(sm)
s = sm.decode('utf-8')
print(s)
