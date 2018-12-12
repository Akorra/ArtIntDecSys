import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        self.solution = {} #Empty dictionary to hold csp solutions

        self.data = {}
        for line in fh.readlines():
            spltd = line.rstrip().split()
            self.data.update({spltd[0]: []})
            for el in spltd[1:]:
                if(spltd[0] in 'RS'):
                    self.data[spltd[0]].append(el)
                elif(spltd[0]=='A'):
                    self.data[spltd[0]].append(tuple(el.split(',')))
                else:
                    self.data[spltd[0]].append('(' + el.strip() + ')')

        self.D = ['(' + r + ',' + T[1:] for r in self.data['R'] for T in self.data['T']]
        self.domains = {W : self.D for W in self.data['W']}
        self.neighbours = {var : [w for w in self.data['W'] if w!=var] for var in self.data['W']}
        self.Assossiation = {c[0]: [sc[1] for sc in self.data['A'] if sc[0]==c[0]] for c in self.data['A']}

        def constraints_function(A,a,B,b):
            nA = self.str2tup(A)
            nB = self.str2tup(B)
            va = self.str2tup(a)
            vb = self.str2tup(b)

            # No 2 weekly classes of the same course and type may occur on the same weekday
            if((nA[0]==nB[0] and nA[1]==nB[1]) and va[1]==vb[1]):
                return False

            # No 2 weekly classes may occur at the same time in the same room
            if(va==vb):
                return False

            # Each Student clss can only attend one class at a time
            if(va[1]==vb[1] and va[2]==vb[2]):
                for key, value in self.Assossiation.items():
                    if((A[0] in value) and (B[0] in value)):
                        return False

            return True

        #csp class takes in parameter:
            #variables : list of variables (atomic ex. string)
            #domains : dict of {variable:[possible_value1, ... ]}
            #graph : dict of {variable:[variable,...]} -> neighbours
            #constraint_function: f(A,a,B,b) returns true if neighbours A,B satisfy the constraints when they have values A=a and B=b
        super().__init__(self.data['W'], self.domains, self.neighbours, constraints_function)


    def dump_solution(self, fh):
        # Place here your code to write solution to opened file object fh
        if not self.solution:
            #dictionary is empty
            fh.write('None')
            return
        else:
            for key,value in self.solution.items():
                sol = self.str2tup(value);
                fh.write(key[1:-1] + ' ' + sol[1] + ',' + sol[2] + ' ' + sol[0] +'\n')

    def str2tup(self, string):
        return tuple(string[1:-1].split(','))

def solve(input_file, output_file):
    p = Problem(input_file)
    # Place here your code that calls function csp.backtracking_search(self, ...)
    p.solution = csp.backtracking_search(p)
    p.dump_solution(output_file)
    print(p.solution)

if __name__ == "__main__":
    fh = open("input.txt", 'r')
    fo = open("output.txt", 'w')
    solve(fh,fo)
