dic = {"A":"drama", "B":"dance", "C":"singing"}
a = []
b = []
c = []

for grp, rl in dic.items():
    if (dic[grp] == "drama"):
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            a.append(roll)
    
    elif dic[grp] == "dance":
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            b.append(roll)

    elif dic[grp] == "singing":
        num = int(input(f"Enter the no of students in {dic[grp]}: "))
        for i in range(num):
            roll = int(input("Enter the student Roll no: "))
            c.append(roll)

print(f"\nStudents of Drama:{a}\nStudents of Dance:{b}\nStudents of Singing:{c}")

def dram_danc(a, b):
    res = list(a)
    for i in b:
        if i not in a:
            res.append(i)
    return res

def inter(a,c):
    tem = []
    for i in a:
        if i in c:
            tem.append(i)
    return tem

def a_c(x):
    temp = []
    inte = dram_danc(a,c)
    for j in x:
        if j not in inte:
            temp.append(j)
    return temp
    
def either(x,y):
    res = []
    un = dram_danc(x,y)
    j = inter(x,y)
    for i in un:
        if i not in j:
            res.append(i)
    return res

print("\n")
if __name__ == '__main__':
    print("Students who participated in drama and dance:",dram_danc(a,b))
    print("\nStudents who participated either drama or singing but not both:",either(a,c))
    print("\nStudents who participated in neither drama nor singing:",a_c(b))


