with open('input_1.txt') as fh:

    inputInfo = dict()

    for line in fh.readlines():
        line = line.strip()
        split_line = line.split(' ')
        auxList = list()

        for value in split_line[1:]:
            auxList.append(value)
        
        newTuple = tuple(auxList)
        inputInfo.update({split_line[0]:newTuple})

    print(inputInfo)        