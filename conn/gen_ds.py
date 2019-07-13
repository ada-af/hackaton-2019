with open('ds_parsed.txt', 'wb') as ds:
    with open('../ds.txt', 'rb') as old_ds:
        for i in old_ds.read().split(b'\n'):
            if b'c++' in i.lower():
                j = 0
            elif b'linux' in i.lower():
                j = 1
            elif b'git' in i.lower():
                j = 2
            elif b'socket' in i.lower():
                j = 3
            elif b'windows' in i.lower():
                j = 4
            elif b'python' in i.lower():
                j = 5
            elif b'ssh' in i.lower():
                j = 6
            elif b'port' in i.lower():
                j = 7
            elif b'sql' in i.lower():
                j = 8
            elif b'css' in i.lower():
                j = 9
            elif b'html' in i.lower():
                j = 10
            elif b'xml' in i.lower():
                j = 11
            else:
                j = 16

            ds.write(i+'~~~{}\n'.format(j).encode())