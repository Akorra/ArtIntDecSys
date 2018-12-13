import csp

class Problem(csp.CSP):

    def __init__(self, fh):
        self.solution = {}                      #Empty dictionary to hold csp solutions
        self.J = None                           #Cost variable, starts set to None in order to ignore optimization on 1st iteration
        self.data = {}                          #dictionary to hold lists read from file
        for line in fh.readlines():             
            spltd = line.rstrip().split()
            self.data.update({spltd[0]: []})
            for el in spltd[1:]:
                if(spltd[0] in 'RS'):
                    self.data[spltd[0]].append(el)
                else:
                    self.data[spltd[0]].append(tuple(el.split(',')))
                    
        # for each line in the file we extract a list of tupples or single values (strings/ints)
        # depending if the list identified by the first char expects tuples or single values according to the project description

        ''' Since any variable can take any value in the domain, all domais are 
            the same for each variable, since a class can take place in any day 
            and in any room as long as this assossiation doesn't break any constraint.
            Neighbours represent all variables that participate in constraints together, 
            in this case all class/(room,timeslot) assossiations must be tested against 
            eachother since they all may incur in constraints together 
            (ex: no 2 classes can happen at the same room at the same time)'''
            
        self.D = [(R,T[0],T[1]) for R in self.data['R'] for T in self.data['T']]                             #Possible values for any variable (ROOM,DAY,HOUR), i.e., Domain                   
        self.domains = {W : self.D for W in self.data['W']}                                                  #Set of domains, in this case, same domain for each variable
        self.neighbours = {var : [w for w in self.data['W'] if w!=var] for var in self.data['W']}            #Dictionary that for each variable (key) holds a list (value) of variables that are involved in constraints with the key variable
        self.Assossiation = {c[0]: [sc[1] for sc in self.data['A'] if sc[0]==c[0]] for c in self.data['A']}  #Dictionary with all classes each student class takes
        
        def constraints_function(A,a,B,b):
            nA = A
            nB = B
            va = a
            vb = b

            # Check if no 2 weekly classes of the same course and type take place on the same weekday
            if((nA[0]==nB[0] and nA[1]==nB[1]) and va[1]==vb[1]):
                return False    #constraint broken

            # Check if 2 weekly classes take place at the same time in the same room
            if(va==vb):
                return False    #constraint broken

            ''' Check if any 2 classes taken by the same student class take place at the same time
                this is done by, if the 2 classes take place at the same time,
                checkin the assossiation dictionary and if the classes being checked 
                are both in the same student class list of classes '''
            if(va[1]==vb[1] and va[2]==vb[2]):
                for key, value in self.Assossiation.items():
                    if((nA[0] in value) and (nB[0] in value)):
                        return False
            
            ''' if self.J has a value it means we are including optimization, in that case,
                if the time for either value being checked is above the time value in the cost variable J
                then we dont want to consider that solution
            '''
            if self.J:
                if(int(va[2])>self.J or int(vb[2])>self.J):
                    return False
            return True

        ''' csp class takes in parameter:
             - variables : list of variables (atomic ex. string)
             - domains : dict of {variable:[possible_value1, ... ]}
             - graph : dict of {variable:[variable,...]} -> neighbours
             - constraint_function: f(A,a,B,b) returns true if neighbours A,B satisfy the constraints when they have values A=a and B=b
        '''
        super().__init__(self.data['W'], self.domains, self.neighbours, constraints_function)

    
    ''' dump_solution
            - parameters: opened file stream, in write mode
            - Writes to file stream solution with a variable and value (space separated) per line 
    '''
    def dump_solution(self, fh):
        #write solution to opened file object fh
        if not self.solution:
            fh.write('None')
            return
        else:
            for key,value in self.solution.items():
                sol = value
                fh.write(key[0] + ',' +  key[1] + ',' +  key[2] + ' ' + sol[1] + ',' + sol[2] + ' ' + sol[0] +'\n')

def solve(input_file, output_file):
    p = Problem(input_file)
    # forward checking allows for a greater speed of iteration, since it prechecks the coherence of the folloing variables
    # and prunes iteration if they lead to worst cases
    p.solution = csp.backtracking_search(p, csp.first_unassigned_variable, csp.unordered_domain_values, csp.forward_checking) #csp.mrv, csp.lcv, csp.mac)
    
    #start optimization by setting J to the latest time value obtained in the first backtracking search solution
    p.J = 0
    for key,value in p.solution.items():
        sol = int(value[2]);
        if(sol>p.J):
            p.J = sol
    
    ''' Optimize by trying to minimize J, if the decrement of J leads to empty solution then dont 
        consider the solution obtained in latest backtracking search and exit optimization
        keeping the last valid solution only.
        Otherwise keep backtracking and decrementing J at each step.
    '''
    while True:
        p.curr_domains = None
        p.nassigns = 0
        sol = csp.backtracking_search(p, csp.first_unassigned_variable, csp.unordered_domain_values, csp.forward_checking) #csp.mrv, csp.lcv, csp.mac)
        if sol:
            p.J -= 1
            p.solution = sol
        else:
            break
    
    p.dump_solution(output_file)
    
    print(p.solution)