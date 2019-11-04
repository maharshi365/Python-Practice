def reveal(deck):
    ds = sorted(deck)
    toRet = [None]*len(ds)
    pos = list(range(len(ds)))
            

    while (len(ds) > 0 and len(pos) > 1):
        toRet[pos[0]] = ds[0]
        ds.pop(0)
        pos.pop(0)
        pos.append(pos.pop(0))
        print(toRet)
    
    toRet[pos[0]] = ds[0]
    print(toRet)

reveal([17,13,11,2,3,5,7])