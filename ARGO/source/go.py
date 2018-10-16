class Game:    
    def __init__(self):
        print("[+] Game Created, please load a game board to proceed...")
        self.board = None
        
    def to_move(self, s):
        self.test_method_failure()
        p = 1 #player
        return p
    
    def terminal_test(self, s):
        self.test_method_failure()
        return True
    
    def utility(self, s, p):
        self.test_method_failure()
        payoff = 1
        return payoff
    
    def actions(self, s):
        '''
            This is only returning empty spaces, available actions should not allow for KO rule breakers
            and maybe even stupid moves
        '''
        self.test_method_failure()
        return [(self.to_move(s), i, j) for i in range(self.n) for j in range(self.n) if go.board[i][j] == 0] 
    
    def result(self, s, a):
        self.test_method_failure()
        state = s
        return state
    
    def load_board(self, s):
        '''
            Loads the board from an opened file stream and saves it to the class field 'board'
            as weel as board dimension 'n', and first player 'p'
            this is done while checking for file integrity
        '''
        
        print("[+] Loading Board...")
        contents = s.read().split()
        try:
            self.n = int(contents[0]) # get board dimension
            self.p = int(contents[1]) # get first player to move
            self.board = [list(map(int, lst)) for lst in contents[2:] # load board into 2D list
                          if len(lst)==self.n or                      # check if each row has the correct number of elements
                          any(c in lst for c in ['3', '4', '5', '6', '7', '8', '9'])] #check if any digits above 2 in each row
        except ValueError:
            # if at any point a non numeric value is found failure is issued
            self.load_failure()
            return
        
        if len(self.board) == self.n:
            print("\t[+] Game Board Successfuly Loaded!")
        else:
            # if dimensions dont match return failure
            self.load_failure()
    
    def load_failure(self):
        print("\t[-] Bad File...")
        print("\t[-] Please try another file...")
        self.board = None
    
    def test_method_failure(self):
        if not self.board:
            print('[-] Game not initiated, please lad a game borad...')
            raise Exception('Error: Game not initiated.')