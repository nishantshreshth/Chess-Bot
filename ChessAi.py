import math
"""def init():
	available=[]
	visited=[]
	ourPos=(2,2)
	size=8
"""
def heuristic(options, oppPos):
    """
    heuristic function
    """
    print "Heuristic :"+str(options)
    answer = ()
    minVal = 10000000000
    for i in options: 
        currVal = math.sqrt((i[0]-oppPos[0])**2 + (i[1]-oppPos[1])**2)
        if currVal < minVal :
            minVal = currVal
            answer = i
    ##print "Answer:" +str(answer)
    return answer

def mainAI(oppPos):
    global ourPos,available,size,visited
    visited.append(oppPos)
    """
    returns next position and next done list
    """
    x_diff = abs(oppPos[0]-ourPos[0])
    y_diff = abs(oppPos[1]-ourPos[1])
    if math.sqrt(((x_diff)**2 +(y_diff)**2))<2 : 
	print math.sqrt(((x_diff)**2 +(y_diff)**2))
        ourPos = oppPos
	print "won"
        return ourPos
    else: 
        flag = 0
        trialState = (ourPos[0],ourPos[1]+1) ##1
        if trialState[1]>size:
            visited.append(trialState)
        if trialState in visited:
	    pass
        else:
            available.append(trialState)
            flag = 1


        trialState = (ourPos[0]+1,ourPos[1]) ##2
        if trialState[0]>size:
            visited.append(trialState)
        if trialState in visited:
	    pass
        else:
            available.append(trialState)
            flag = 1

	trialState = (ourPos[0]-1,ourPos[1]) ##3
        if trialState[0]<1:
            visited.append(trialState)
        if trialState in visited:
	    pass
        else:
            available.append(trialState)
            flag = 1

	trialState = (ourPos[0],ourPos[1]-1) ##4
        if trialState[1]<1:
            visited.append(trialState)
        if trialState in visited:
	    pass
        else:
            available.append(trialState)
            flag = 1


	trialState = (ourPos[0]+1,ourPos[1]+1) ##5
        if trialState[0]>size or trialState[1]>size:
            visited.append(trialState)
        if trialState in visited:
	    pass
        else:
            available.append(trialState)
            flag = 1
        
        trialState = (ourPos[0]-1,ourPos[1]-1) ##6
        if trialState[1]<1 or trialState[0]<1:
            visited.append(trialState)
        if trialState in visited:
            pass
        else:
            available.append(trialState)
            flag = 1

	trialState = (ourPos[0]-1,ourPos[1]+1) ##7
        if trialState[1]>size or trialState[0]<1:
            visited.append(trialState)
        if trialState in visited:
            pass
        else:
            available.append(trialState)
            flag = 1
        
        trialState = (ourPos[0]+1,ourPos[1]-1) ##8
        if trialState[1] < 1 and trialState[0]>size: 
            visited.append(trialState)
        if trialState in visited:
	   pass
        else:
            available.append(trialState)
            flag = 1
        
        if flag == 0 :
            print "we lose"
        else: 
            """
            we have possibleStates and doneStates
            """
            finalState = ()
            """
            one level optimization

            """
	    print "Available Positon:"
	    print available
            options = []
            for i in available : 
                x_diff_1 = abs(oppPos[0]-i[0])
                y_diff_1 = abs(oppPos[1]-i[1])
                if (abs(x_diff_1)**2 + abs(y_diff_1)**2)<5: 
                    continue
		elif ((size-i[0])**2 + (size-i[1])**2)<5:
		   continue
                else:
                    options.append(i)
            # opt1 is the first level optimizatin
	    print "Options:"
            print options
	    if len(options)>1:
            	finalState = heuristic(options,oppPos)
	    else:
		finalState= heuristic(available,oppPos)
	    ## print "####### FinalState: "+ str(finalState)
	    k=available.pop(available.index(finalState))
	    visited.append(finalState)
	    ourPos=finalState
        return finalState

## available=[]

ourPos=(1,1)
visited=[ourPos]
size=8

while 1:
	available=[]
	print "visited:"
	print visited
	print "Our Position:"
	print ourPos
	print "Enter Opponent Position"
	x,y= map(int, raw_input().strip().split())
	oppPos=(x,y)
	mainAI(oppPos)
