# Them cac thu vien neu can
class packet:
    def __init__(self, xDes, yDes, volume, weight):
        self.xDes = xDes  # x of destination
        self.yDes = yDes  # y of destination
        self.vol = volume
        self.wgt = weight


def readInput(file_input):
    File = open(file_input, 'r')
    firstLine = File.readline()  # get first line
    secondLine = File.readline()  # get second line
    #=========GET X,Y OF WAREHOUSE FROM STRING==========#
    [X, Y] = [int(i) for i in firstLine.split(' ')]
    #===================================================#
    #=========GET NUMBER OF PACKET AND NUMBER OF DELIVERS========#
    [NUM_PACKETS, NUM_DELIVERS] = [int(i) for i in secondLine.split(' ')]
    #============================================================#
    #=========GET INFO OF ALL PACKETS===================#
    packetArray = []
    for line in File:  # get other line
        [xDes, yDes, volume, weight] = [
            int(i) for i in line.split(' ')]  # get number from string
        packetArray.append(packet(xDes, yDes, volume, weight))
    #===================================================#
    #=========CLOSE FILE AND RETURN=====================#
    File.close()
    return X, Y, NUM_PACKETS, NUM_DELIVERS, packetArray


def assign(file_input, file_output):
    # read input
    # note that readInput() function return 4 value
    # ====this is an example of using readInput()======================#
    [X, Y, NUM_PACKETS, NUM_DELIVERS, packetArray] = readInput(file_input)
    print(X, Y, NUM_PACKETS, NUM_DELIVERS)
    for obj in packetArray:
        print(obj.xDes)
    #==================================================================#
    # run algorithm
    # write output
    return


assign('input.txt', 'output.txt')
