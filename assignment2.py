# Them cac thu vien neu can
import numpy
import copy
import math
import random
X = 0 # x of ware house
Y = 0 # y of ware house
NUM_PACKETS = 0 # number of packet
NUM_SHIPPERS = 0 # number of shipper


def probab(deltaE, T):
    if deltaE>0:
        return True
    else:
        if T==0:
            return False
        prob = math.exp(deltaE/T)
        print("deltaE = ",deltaE,"|| T = ",T,"|| PROB = ",prob)
        if (prob>random.uniform(0,1)):
            print("return true")
            return True
        else:
            print("return false")
            return False
    

def distance(xDes1, yDes1, xDes2, yDes2):
    return math.sqrt(math.pow(xDes2 - xDes1, 2) + math.pow(yDes2 - yDes1, 2))

def distanceBetween(packetA, packetB):
    return distance(packetA.xDes,packetA.yDes,packetB.xDes,packetB.yDes)

def profit(packetArray):
    global X,Y
    if len(packetArray)==0:
        return 0
    revenueDeliver = 0
    for packet in packetArray:
        revenueDeliver += packet.costPacket
    
    total_distance = distance(X, Y, packetArray[0].xDes, packetArray[0].yDes)
    if(len(packetArray) > 1):
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
    [NUM_PACKETS, NUM_SHIPPERS] = [int(i) for i in secondLine.split(' ')]
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
    return X, Y, NUM_PACKETS, NUM_SHIPPERS, packetArray
class packet:
    def __init__(self, id , xDes, yDes, volume, weight):
        self.id = id
        self.xDes = xDes  # x of destination
        self.yDes = yDes  # y of destination
        self.volume = volume
        self.weight = weight
        self.costPacket = 5 + volume + weight * 2

class shipper:
    packetArray = []
    profit = 0
    def __init__(self, id):
        self.id = id
        self.profit = 0

    def appendPacket(self, packet):
        self.packetArray.append(packet)
        self.profit = profit(self.packetArray)

    def removeTail(self):
        self.packetArray.pop(-1)
        self.profit = profit(self.packetArray)

class state:
    global NUM_PACKETS,NUM_SHIPPERS
    packetArray = []
    shipperArray = []
    profitArray = []
    var = 0
    def __init__(self, packetArray):
        self.packetArray = packetArray
        for i in range(NUM_SHIPPERS):
            self.shipperArray.append(shipper(i))
            self.profitArray.append(self.shipperArray[i].profit)
        self.updateVar()

    def movePacketToShipper(self,packetIndex,shipperIndex):
        print("packet : ",self.packetArray[packetIndex].id,"to shipper: ",shipperIndex)
        self.shipperArray[shipperIndex].appendPacket(self.packetArray[packetIndex])
        self.packetArray.pop(packetIndex)
        self.updateProfitArray()
        self.updateVar()

    def updateVar(self):
        self.var = numpy.var(self.profitArray)
        for profit in self.profitArray:
            if(profit == 0):
                self.var = self.var + 1000 # if there is any shipper dont have profit yet, we add 1000 to increase var
    def updateProfitArray(self):
        for i in range(NUM_SHIPPERS):
            self.profitArray[i] = (self.shipperArray[i].profit)

def createNewState(currentState):
    newState = copy.deepcopy(currentState)
    rangeForPacket = len(newState.packetArray) - 1
    if(rangeForPacket < 0):
        return newState
    rangeForShipper = len(newState.shipperArray) - 1
    randomPacketIndex = random.randint(0, rangeForPacket)
    randomShipperIndex = random.randint(0, rangeForShipper)
    newState.movePacketToShipper(randomPacketIndex, randomShipperIndex)
    return newState


def assign(file_input, file_output):
    global X,Y,NUM_PACKETS,NUM_SHIPPERS # this line is very important
    # read input
    # note that readInput() function return 5 value
    # ====this is an example of using readInput() and profit()======================#
    [X, Y, NUM_PACKETS, NUM_SHIPPERS, packetArray] = readInput(file_input)
    print("X = ",X,"|| Y = ",Y)
    print("NUM_PACKETS = ",NUM_PACKETS,"|| NUM_SHIPPERS = ", NUM_SHIPPERS)
    for obj in packetArray:
        print(obj.id, obj.xDes, obj.yDes, obj.volume, obj.weight, obj.costPacket)
    #==================================================================#
    # run algorithm
    # write output
    currentState = state(packetArray)
    T = currentState.var
    count = 0
    for i in range(10):
        T = currentState.var
        print("T = ",T)
        if(T == 0 or count == 3):
            break
        newState = copy.deepcopy(createNewState(currentState))
        # print("newState.var = ",newState.var)
        # print("currentState.var = ",currentState.var)
        deltaE = currentState.var - newState.var
        print("deltaE = ",deltaE)
        if(deltaE > 0):
            currentState = copy.deepcopy(newState)
            count = 0
        else:
            if(probab(deltaE,T)):
                currentState = copy.deepcopy(newState)
            else:
                count = count+1

    print("final var = ",currentState.var)
    print(currentState.profitArray)
    print(currentState.shipperArray[0].packetArray[0].id)
    # for i in range(NUM_SHIPPERS):
    #     print("shipper : ",i)
    #     # for j in range(len(currentState.shipperArray[i].packetArray)):
    #     #     print(currentState.shipperArray[i].packetArray[j])
    #     print(len(currentState.shipperArray[i].packetArray))
    
    
    return 


assign('input.txt', 'output.txt')