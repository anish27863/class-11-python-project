#Bubble sort

def bubble_sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):

            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
    return(list1)

list1=[5,9,3,7,1,9,8,4,6,1,2,0,9,8]

print(f"The unsorted list is{list1}")
print(f"The sorted list is: {bubble_sort(list1)}")