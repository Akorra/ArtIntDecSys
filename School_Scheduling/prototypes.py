#Reading the file into a dictionary with the set as key (T, R, W, S, A) and the value as a tuple of each element of the set
with open('input_1.txt') as fh:

        data = {}
        for line in fh.readlines():
            spltd = line.rstrip().split()
            data.update({spltd[0]: []})
            for el in spltd[1:]:
                if(spltd[0] in 'RS'):
                    data[spltd[0]].append(el)
                elif(spltd[0]=='A'):
                    data[spltd[0]].append(tuple(el.split(',')))
                else:
                    data[spltd[0]].append('(' + el.strip() + ')')

        D = ['(' + r + ',' + T[1:] for r in data['R'] for T in data['T']]
        domains = {W : D for W in data['W']}
        neighbours = {var : [w for w in data['W'] if w!=var] for var in data['W']}
        Assossiation = {c[0]: [sc[1] for sc in data['A'] if sc[0]==c[0]] for c in data['A']}

        print(Assossiation)

