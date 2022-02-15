def parse(data):
    val = 0
    res = []
    for i in range(len(data)):
        if data[i] == 'i':
            val +=1
        if data[i] == 'd':
            val -=1
        if data[i] == 's':
            val *=val
        if data[i] =='o':
            res.append(val)
    return res