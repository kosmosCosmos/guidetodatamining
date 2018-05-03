class Enron:
    def init( self, filename, k ):
        file = open(filename)
        lines = file.readlines()
        file.close()
        header = lines[0].split(',')
        self.cols = len(header)
        self.data = [[] for i in range(len(header))]
        header = lines[0].split(',')
        for line in lines[1:]:
            cells = line.split(',')
            for cell in range(self.cols):
                self.data[cell].append(cells[cell])
                print(self.data[cell])


km = Enron()
km.init('enrondata.txt', 2)
