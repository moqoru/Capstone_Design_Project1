# Name : Youngjune Seo (MOQORU)
# Date : 2019-04-02

max_heap, min_heap = [], []

def reheap_up(side) :
    if side == "max" :
        i = len(max_heap)-1 # start node : maximum
        while i > 0 : # loop until the second node (not first node for avoid overrun)
            if max_heap[(i-1)//2] < max_heap[i] : # if parent node is smaller than child node
                max_heap[(i-1)//2], max_heap[i] = max_heap[i], max_heap[(i-1)//2] # swap
                i = (i-1)//2 # use //, kept int type
            else : # else finish at once
                break
    else : # vice versa
        i = len(min_heap)-1
        while i > 0 :
            if min_heap[(i-1)//2] > min_heap[i] :
                min_heap[(i-1)//2], min_heap[i] = min_heap[i], min_heap[(i-1)//2]
                i = (i-1)//2
            else :
                break

def reheap_down(side) :
    i = 0 # start node : first
    if side == "max" :
        while i < len(max_heap) : # loop until the last node
            if i*2+2 < len(max_heap) : # avoid overrun
                if (max_heap[i] < max_heap[i*2+2] and max_heap[i*2+1] < max_heap[i*2+2]) : # if right child node is bigger than parent node
                    max_heap[i], max_heap[i*2+2] = max_heap[i*2+2], max_heap[i] # swap
                elif max_heap[i] < max_heap[i*2+1] : # if left child node is bigger than parent node
                    max_heap[i], max_heap[i*2+1] = max_heap[i*2+1], max_heap[i]
                else : # else finish at once
                    break
            elif i*2+1 < len(max_heap) : # avoid overrun
                if max_heap[i] < max_heap[i*2+1] : # if left child node (= final node) is bigger than ...
                    max_heap[i], max_heap[i*2+1] = max_heap[i*2+1], max_heap[i]
                else :
                    break
            else :
                break
    else : # vice versa
        while i < len(min_heap) :
            if i*2+2 < len(min_heap) :
                if (min_heap[i] > min_heap[i*2+2] and min_heap[i*2+1] > min_heap[i*2+2]) :
                    min_heap[i], min_heap[i*2+2] = min_heap[i*2+2], min_heap[i]
                elif min_heap[i] > min_heap[i*2+1] :
                    min_heap[i], min_heap[i*2+1] = min_heap[i*2+1], min_heap[i]
                else :
                    break
            elif i*2+1 < len(min_heap) :
                if min_heap[i] > min_heap[i*2+1] :
                    min_heap[i], min_heap[i*2+1] = min_heap[i*2+1], min_heap[i]
                else :
                    break
            else :
                break

def Heap4Median_AddItem(value) :
    if len(max_heap) <= len(min_heap) :
        if len(max_heap) == 0 : # if max heap has no data
            max_heap.append(value)
        elif value <= min_heap[0] : # if new data is smaller than min heap root node
            max_heap.append(value) # add new data in max heap
            reheap_up("max") # reheap up for max heap
        else :
            min_heap[0], value = value, min_heap[0] # swap new data & min heap root node
            max_heap.append(value) # add swaped data in min heap
            reheap_down("min") # reheap down for min heap
            reheap_up("max") # reheap up for max heap
    else : # vice versa
        if len(min_heap) == 0 : # if min heap has no data
            min_heap.append(value)
            if max_heap[0] > min_heap[0] : # if max heap has bigger data
                min_heap[0], max_heap[0] = max_heap[0], min_heap[0]
        elif value >= max_heap[0] :
            min_heap.append(value)
            reheap_up("min")
        else :
            max_heap[0], value = value, max_heap[0]
            min_heap.append(value)
            reheap_down("max")
            reheap_up("min")


infile = open("input1234567.txt","r")
number = infile.readline() # read how many numbers (no need?)

for line in infile :
    num_list = line.split() # split numbers by blanks
    for num_line in num_list :
        Heap4Median_AddItem(int(num_line)) # add numbers one by one

print("The median is", max_heap[0]) # max heap's first node is median

