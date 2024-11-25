list = [1,3,4,6,2,5,9,7]

#key = int(input("input key here:"))


#linear seach
def linersearch(key):
    for i in range(len(list)):
        if (list[i] == key):
            print(i)




def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if(list[j] > list[j+1]):
                t = list[j]
                list[j] = list[j + 1]
                list[j+1] = t

    return list





def binarysearch(key):
    low = list[0]

    high = list[len(list) - 1]

    mid = (low + high)/2

    while(low < high):
        if (key == mid):
            return list
        elif (key > mid):
            low = list[list[mid] + 1]
        else:
            high = list[list[mid] - 1]








#linersearch(key)

newlist = bubblesort(list)
print(newlist)