def cmprTime(time1,time2):
   time1InSecond = 3600*time1[0] + 60*time1[1] + time1[2]
   time2InSecond = 3600*time2[0] + 60*time2[1] + time2[2]
   
   if time1InSecond > time2InSecond:
       return True
   else:
       return False

athleteInformation = {}

flag = True
while flag:
    name = tuple(input("First and last name: ").split())
    country = input("Country: ")
    finishingTime = eval(input("Finishing time in hours, minutes, seconds: "))
    athleteInformation[name] = [country,finishingTime]
    
    condition = input("Do you want to continue Y/N? ")
    while condition not in ['Y','N']:
        print("Wrong option just Y for yes or N for no is valid")
        condition = input("Do you want to continue Y/N? ")
        
    if condition == 'N':
        flag = False

keys = list(athleteInformation.keys())
values = list(athleteInformation.values())
n = len(values)
#will sort athletes in an ascending order according to their finishing time
for i in range(n-1):
    for j in range(n-i-1):
        if cmprTime(values[j][1],values[j+1][1]) == True:
            values[j], values[j+1] = values[j+1], values[j]
            keys[j], keys[j+1] = keys[j+1], keys[j]
print("")
#will find and print the top 3 who are the winners of a medal
for key, value, rank in zip(keys,values,range(1,4)):
    name = ' '.join(key)
    country = value[0]
    
    if rank == 1:
        print("Gold Medal: ", name,', ', country)
    if rank == 2:
        print("Silver Medal: ", name,', ', country)
    if rank == 3:
        print("Bronze Medal: ", name,', ', country)
print("")
#will find and print Turkish Atlethes who run under 3 hours
flag = True
for key, value in zip(keys,values):
    country = value[0]
    time = value[1]
   
    if country == "Turkey" and time[0] < 3:
        if flag == True:
            print("Turkish athletes running under 3 hours: ", end='')
            flag = False
            
        name = ' '.join(key)
        print(name, end='   ')
