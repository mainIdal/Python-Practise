def fun(List, x, y):
    lenList = len(List)
    listToAdd = [x] * y

    if lenList % 2 == 0:
        #List will be firstPartOfList + listToAdd + secondPartOfList
        List = List[ : lenList//2] + listToAdd + List[ lenList//2 : ]
    else:
        #List will be List + listToAdd
        List += listToAdd

    return List

def form(List, power):
    if len(List) == 0:
        return 0
    
    return List.pop(len(List)-1) * power + form(List, power * 10)

#For even number of elements 
lst = [2,3,4,5]
lst = fun(lst, 9, 2) #[2,3,9,9,4,5]
print(form(lst, 1))

#For odd number of elements
lst = fun([2,3,4], 9, 3) #[2,3,4,9,9,9]
print(form(lst, 1))
