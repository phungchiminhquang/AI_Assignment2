# Them cac thu vien neu can
import math
import random

class packet:
    def __init__(self, ID , xDes, yDes, volume, weight):
        self.ID = ID
        self.xDes = xDes  # x of destination
        self.yDes = yDes  # y of destination
        self.volume = volume
        self.weight = weight
        self.costPacket = 5 + volume + weight * 2

class shipper:
    packetArray = []
    profit = 0
    def __init__(self, ID , X, Y, packetArray):
        self.ID = ID
        self.X = X
        self.Y = Y
        self.packetArray = packetArray
        self.profit = profit(X, Y, packetArray)

    def appendPacket(self, value):
        self.packetArray.append(value)
        self.profit = profit(self.X, self.Y, self.packetArray)

    def removeTail(self):
        self.packetArray.pop(-1)
        self.profit = profit(self.X, self.Y, self.packetArray)


def probab(deltaE, T):
    if deltaE>0:
        return True
    else:
        if T==0:
            return True
        prob = math.exp(deltaE/T)
        if (prob>random.uniform(0,1)):
            return True
        else:
            return False
    

def distance(xDes1, yDes1, xDes2, yDes2):
    return math.sqrt(math.pow(xDes2 - xDes1, 2) + math.pow(yDes2 - yDes1, 2))

def distanceBetween(packetA, packetB):
    # print("packetA : ( ",packetA.xDes,", ",packetA.yDes,')')
    # print("packetB : ( ",packetB.xDes,", ",packetB.yDes,')')
    return distance(packetA.xDes,packetA.yDes,packetB.xDes,packetB.yDes)

def profit(X, Y, packetArray):
    if len(packetArray)==0:
        return 0
    revenueDeliver = 0
    for packet in packetArray:
        revenueDeliver += packet.costPacket
    
    total_distance = distance(X, Y, packetArray[0].xDes, packetArray[0].yDes)
    for x in range(len(packetArray)-1):
        total_distance += distanceBetween(packetArray[x],packetArray[x+1])

    transportation_costs = total_distance / 40 * 20 +10
    return revenueDeliver - transportation_costs

def readInput(file_input):
    File = open(file_input, 'r')
    firstLine = File.readline()  # get first line
    secondLine = File.readline()  # get second line
    #GET X,Y OF WAREHOUSE FROM FIRST LINE#
    [X, Y] = [int(i) for i in firstLine.split(' ')]
    #GET NUMBER OF PACKET AND NUMBER OF DELIVERS FROM SECOND LINE#
    [NUM_PACKETS, NUM_DELIVERS] = [int(i) for i in secondLine.split(' ')]
    #GET INFO OF ALL PACKETS#
    packetArray = []
    ID = 0
    for line in File:  # get other line
        [xDes, yDes, volume, weight] = [
            int(i) for i in line.split(' ')]  # get number from string
        packetArray.append(packet(ID, xDes, yDes, volume, weight))
        ID += 1
    #=========CLOSE FILE AND RETURN=====================#
    File.close()
    return X, Y, NUM_PACKETS, NUM_DELIVERS, packetArray


def assign(file_input, file_output):
    # read input
    # note that readInput() function return 5 value
    # ====this is an example of using readInput() and profit()======================#
    [X, Y, NUM_PACKETS, NUM_DELIVERS, packetArray] = readInput(file_input)
    print(X, Y)
    print(NUM_PACKETS, NUM_DELIVERS)
    
    for obj in packetArray:
        print(obj.ID, obj.xDes, obj.yDes, obj.volume, obj.weight, obj.costPacket)
    print(distanceBetween(packetArray[0],packetArray[1]))
    print(profit(X,Y,packetArray))
    #==================================================================#
    # run algorithm
    # write output
    return


assign('input.txt', 'output.txt')