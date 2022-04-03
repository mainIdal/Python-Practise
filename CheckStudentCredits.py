dic = {(1111,1.9):[("Cmpe 341", 17), ("Cmpe 312", 16)],
       (2222,2): [("SE 341", 24), ("SE 312", 16)],
       (3333,1.9):[("Cmpe 341", 18), ("Cmpe 312", 16)],
       (4444,2): [("SE 341", 25), ("SE 312", 16)]}
keys = dic.keys()
values = dic.values()
total = []
for val in values:
    sum = 0
    for course in val:
        sum += course[1]
    total.append(sum)
n = len(keys)
print(total)
for key, i in zip(keys,range(n)):
   if key[1] < 2.0 and total[i] <= 33:
      print("Courses of the student with ", key[0], "id: ")
      for val in dic[key]:
         print(val[0])
   elif key[1] < 2.0 and total[i] > 33:
       print("Student with ", key[0], " cannot take mroe than 33 credits")
   elif key[1] >= 2.0 and total[i] <= 40:
       print("Courses of the student with ", key[0], "id: ")
       for val in dic[key]:
         print(val[0])
   elif key[1] >= 2.0 and total[i] > 40:
       print("Student with ", key[0], " cannot take mroe than 40 credits")
