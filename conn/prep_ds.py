with open('ds_parsed.txt', 'rb') as f:
    with open('ds_end.txt', 'wb') as p:
        for i in f.read().split(b'\n'):
            if b"~~~16" not in i:
                p.write(i+b"\n")