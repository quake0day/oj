class NDM():

    face = [] # 0 , 1, 2, ... m
    count = [] # 

    times = {} # record NDM all points frequency

    def __init__(self, m, n):
        # n : number of dice
        # m : faces for each dice

        self.n = n
        self.m = m
        self.face = []
        self.count = []
        self.times = {}
        self.xh = []


        for i in range(1, m+1):
            self.face.append(i) #face[i] means i'th face's val

        for i in range(n):
            # count[i] represents i'th dice face
            self.count.append(0)

        self.count[0] = -1
        for i in range(n, m*n+1):
            self.times[i] = 0  # init as 0


    def funCompute(self):
        
