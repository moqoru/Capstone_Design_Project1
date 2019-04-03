# Name : Youngjune Seo (MOQORU)
# Date : 2019-04-03

import queue
import heapq


matrix = [[]]
Answer_B = []
Path_B = []
Answer_D = []
Path_D = []
Answer_F = [[]]
Path_F = [[]]

def Bellman_Ford(start) : # MAYBE enhance code with TUPLE?

    for i in range(size) :
        Answer_B.append(999999) # set path infinite value
        Path_B.append("NO PATH") # set error message for miss detection
        if matrix[start][i] != 0 : # if have edge
            qB.put_nowait(start) # enqueue start & end points
            qB.put_nowait(i)
    Answer_B[start] = 0
    Path_B[start] = str(start+1) # All path's starting point is same    
    
    for i in range(size) :
        if qB.empty() : break
        renew = qB.qsize() // 2
        for k in range(renew) :
            check_a = qB.get_nowait() # dequeue points
            check_b = qB.get_nowait()
            if (Answer_B[check_a] + matrix[check_a][check_b]) < Answer_B[check_b] : # if new path is shorter
                Answer_B[check_b] = Answer_B[check_a] + matrix[check_a][check_b] # path data renew
                Path_B[check_b] = Path_B[check_a] + " " + str(check_b+1)
                for can_go in range(size) : 
                    if matrix[check_b][can_go] != 0 : # if could go another edge from new path end point
                        qB.put_nowait(check_b) # enqueue found start & end points
                        qB.put_nowait(can_go)

def Dijkstra(start) :

    for i in range(size) :
        Answer_D.append(999999) 
        Path_D.append("NO PATH") 
        if matrix[start][i] != 0 : 
            heapD.append((matrix[start][i], start, i)) # push path data (length, start, end)
    Answer_D[start] = 0
    Path_D[start] = str(start+1) # All path's starting point is same    
    heapq.heapify(heapD) # set the least path data

    for i in range(size-1) : # loop until all nodes are linked
        while(1):
            check = heapq.heappop(heapD) # pop the least path data
            if Answer_D[check[2]] >= 999999 : # if the least path is pointing new node
                Answer_D[check[2]] = Answer_D[check[1]] + check[0] # path data renew
                Path_D[check[2]] = Path_B[check[1]] + " " + str(check[2]+1)
                for can_go in range(size) : 
                    if (matrix[check[2]][can_go] != 0 and Answer_D[can_go] >= 999999) : # if could go another edge from new path end point
                        heapD.append((matrix[check[2]][can_go], check[2], can_go)) # push path data
                break # if new node found, break to find next new node
            if not heapD : break # only breaks some node can't be visited
            heapq.heapify(heapD) # renew the least path data

def Floyd_Warshall(start) : # MAYBE list isn't good for this question... numpy is BETTER?

    for i in range(size) : # to calculate Floyd_Warshall, need 2-dimention list
        for j in range(size) :
            if matrix[i][j] != 0 :
                if len(Answer_F[-1]) == size :
                    Answer_F.append([matrix[i][j]])
                    Path_F.append([str(i+1) + " " + str(j+1)])
                else :
                    Answer_F[-1].append(matrix[i][j])
                    Path_F[-1].append(str(i+1) + " " + str(j+1))
            else :
                if len(Answer_F[-1]) == size :
                    Answer_F.append([999999])
                    Path_F.append(["NO PATH"])
                else :
                    Answer_F[-1].append(999999)
                    Path_F[-1].append("NO PATH")
    for k in range(size) : # k is bypass node
        for i in range(size) :
            for j in range(size) :
                if Answer_F[i][j] > Answer_F[i][k] + Answer_F[k][j] : # if new path found
                    Answer_F[i][j] = Answer_F[i][k] + Answer_F[k][j]
                    Path_F[i][j] = Path_F[i][k][0:-2] + " " + Path_F[k][j] # combine two paths

infile = open("hw2_input02.txt", "r")
size = int(infile.readline()) # read how many vertexes
qB = queue.Queue(size*2)
heapD = []

for line in infile :
    edge_list = line.split()
    for edge_line in edge_list :
        if len(matrix[-1]) == size :
            matrix.append([float(edge_line)])
        else :
            matrix[-1].append(float(edge_line))

Bellman_Ford(0)
Dijkstra(0)
Floyd_Warshall(0)

print("Bellman_Ford")
for i in range(1, size) :
    if Answer_B[i] < 999999 : # if have path
        print(Path_B[i], Answer_B[i])
    else :
        print(Path_B[i]) # prints only error message

print("\nDijkstra")
for i in range(1, size) :
    if Answer_D[i] < 999999 : # if have path
        print(Path_D[i], Answer_D[i])
    else :
        print(Path_D[i]) # prints only error message

print("\nFloyd_Warshall")
for i in range(1, size) :
    if Answer_F[0][i] < 999999 : # if have path
        print(Path_F[0][i], Answer_F[0][i])
    else :
        print(Path_F[0][i]) # prints only error message

infile.close() # don't forget close!
