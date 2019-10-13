import matplotlib.pyplot as plt 
import numpy as np

bias = 1
lr = 1
weights = [1.5, 1.5, 1.5]

commId = [5000,5001,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012,5013,5014,5015,5016,5017,5018,5019,5020,5021,5022,5023,5024,5025,5026,5027,5028,5029,5030,5031,5032,5033,5034,5035,5036,5037,5038,5039,5040,5041,5042,5043,5044,5045]
conVals = [[5000,5,2,3,0,17,12,34,16,34,16,20,2,8,49,26,32,34,16,20,2,8,49,26,32],
[5001,3,0,12,4,11,35,24,14,24,14,16,11,3,34,18,34,24,14,16,11,3,34,18,34],
[5002,2,0,4,5,26,29,25,14,25,14,16,8,15,21,23,30,25,14,16,8,15,21,23,30],
[5003,4,3,9,2,27,29,29,22,29,22,25,6,16,33,35,30,29,22,25,6,16,33,35,30],
[5004,5,2,5,4,23,33,27,17,27,17,18,8,5,25,26,41,27,17,18,8,5,25,26,41],
[5005,3,1,14,3,36,22,4,23,21,16,11,3,34,29,28,29,21,16,11,3,34,29,28,29],
[5006,1,4,4,3,36,26,3,36,19,16,8,15,21,27,26,47,19,16,8,15,21,27,26,47],
[5007,0,4,4,4,36,44,3,36,28,25,6,16,33,27,23,15,28,25,6,16,33,27,23,15],
[5008,5,5,8,6,27,43,4,36,27,18,8,5,25,28,32,36,27,18,8,5,25,28,32,36],
[5009,6,3,8,3,28,27,6,27,20,22,8,12,29,32,24,19,20,22,8,12,29,32,24,19],
[5010,4,2,11,2,27,29,3,28,20,37,5,18,27,42,20,20,20,37,5,18,27,42,20,20],
[5011,2,4,5,5,27,29,2,27,27,10,9,25,27,27,21,34,27,10,9,25,27,27,21,34],
[5012,5,5,9,3,26,20,5,27,29,25,5,17,28,36,26,36,29,25,5,17,28,36,26,36],
[5013,6,3,6,2,36,20,3,26,20,17,6,16,32,29,26,18,20,17,6,16,32,29,26,18],
[5014,7,1,7,1,27,18,2,36,24,25,10,30,42,18,23,34,24,25,10,30,42,18,23,34],
[5015,3,0,10,3,25,14,16,34,24,30,11,13,27,38,25,32,24,30,11,13,27,38,25,32],
[5016,2,5,7,5,33,20,20,24,21,17,6,15,36,24,31,33,21,17,6,15,36,24,31,33],
[5017,0,6,7,2,38,19,19,25,30,31,6,26,29,21,24,18,30,31,6,26,29,21,24,18],
[5018,0,4,10,1,30,18,14,29,22,20,5,16,18,33,26,20,22,20,5,16,18,33,26,20],
[5019,3,2,2,4,42,23,22,27,28,18,6,38,38,30,15,38,28,18,6,38,38,30,15,38],
[5020,2,5,6,5,30,14,15,20,23,21,6,15,24,21,27,28,23,21,6,15,24,21,27,28],
[5021,1,4,8,3,28,15,17,16,21,21,4,21,21,12,30,25,21,21,4,21,21,12,30,25],
[5022,4,4,3,7,37,12,16,16,15,10,36,24,25,10,27,15,15,10,36,24,25,10,27,15],
[5023,4,5,2,1,27,15,17,25,33,25,34,24,30,11,26,16,33,25,34,24,30,11,26,16],
[5024,1,6,3,1,48,10,18,18,17,17,24,21,17,6,22,38,17,17,24,21,17,6,22,38],
[5025,1,4,4,4,26,18,16,22,20,25,25,30,31,6,30,22,20,25,25,30,31,6,30,22],
[5026,1,6,5,2,28,18,25,37,31,30,29,22,20,5,25,18,31,30,29,22,20,5,25,18],
[5027,4,1,11,5,34,16,20,10,31,17,27,28,18,6,27,27,31,17,27,28,18,6,27,27],
[5028,4,4,1,3,28,17,15,25,15,31,20,23,21,6,21,22,15,31,20,23,21,6,21,22],
[5029,5,2,6,8,32,16,20,17,4,20,16,21,21,4,28,26,4,20,16,21,21,4,28,26],
[5030,6,2,7,3,46,16,21,25,17,18,16,15,10,23,20,24,17,18,16,15,10,23,20,24],
[5031,4,1,5,7,30,15,14,30,18,21,25,33,25,13,24,23,18,21,25,33,25,13,24,23],
[5032,6,8,3,5,24,17,11,17,12,21,12,16,16,15,10,36,12,21,12,16,16,15,10,36],
[5033,1,4,8,7,32,18,15,31,17,29,15,17,25,33,25,37,17,29,15,17,25,33,25,37],
[5034,4,4,6,16,36,13,18,20,8,12,10,18,18,17,17,27,8,12,10,18,18,17,17,27],
[5035,2,1,5,19,20,17,15,18,15,25,15,31,22,20,25,17,15,25,15,31,22,20,25,17],
[5036,2,4,2,12,37,29,29,21,19,17,4,20,37,31,30,31,19,17,4,20,37,31,30,31],
[5037,1,5,5,13,39,20,18,21,7,25,17,18,10,31,17,23,7,25,17,18,10,31,17,23],
[5038,8,2,3,15,22,14,17,29,11,30,18,21,25,15,31,30,11,30,18,21,25,15,31,30],
[5039,4,1,4,24,32,13,19,12,7,31,16,20,17,4,20,22,7,31,16,20,17,4,20,22],
[5040,4,4,2,14,28,17,15,16,8,32,16,21,25,17,18,27,8,32,16,21,25,17,18,27],
[5041,1,4,7,13,25,19,18,14,10,33,15,14,30,18,21,15,10,33,15,14,30,18,21,15],
[5042,4,1,3,17,39,19,10,14,10,34,17,11,17,12,21,17,10,34,17,11,17,12,21,17],
[5043,5,4,2,15,32,13,12,22,9,35,22,5,36,21,32,23,9,35,22,5,36,21,32,23],
[5044,6,5,5,20,14,10,24,17,6,36,2,2,39,26,30,17,6,36,2,2,39,26,30,17]]

maxMin = [4360591960611.0, 4360591960611.0]

axis = [[], []]

def sigmoid(val):
    return 1/(1+np.exp(-1))

def Perceptron(input1, input2, output):
    print("For Comunity : "+str(input1)+" and Time Slot "+str(input2)+" Original Output is "+str(output), end=" ")
    outputGot = weights[0]*input1 + weights[1]*input2 + weights[2]*bias
    if(outputGot>maxMin[0]):
        maxMin[0] = outputGot
    if(outputGot < maxMin[1]):
        maxMin[1] = outputGot
    
    axis[0].append(outputGot)
    outputGot = sigmoid(outputGot)
    print("Estimated Output : ",outputGot)
    # if(outputGot > 0):
    #     outputGot = 1
    # else:
    #     outputGot = 0
    error = output - outputGot
    weights[0] += error*input1*lr
    weights[1] += error*input2*lr
    weights[2] += error*bias*lr
    
for z in range(1000):
    for i in range(45):
        for j in range(1,25, 1):
            Perceptron(commId[i], j, conVals[i][j])
    
    

outputGot = weights[0]*(5017) + weights[1]*(0) + weights[2]*bias
print("Final Out : ",outputGot)    
print(maxMin)

axis[1].append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
# plt.plot(axis[0], axis[1])
# plt.show() 

    
    