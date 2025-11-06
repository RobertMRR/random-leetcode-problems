# Average Salary Excluding the Minimum and Maximum Salary
def average(salary):
    salary.sort()
    total = 0
    for item in salary[1:len(salary)-1]:
        total += item
    return total/(len(salary)-2)

print(average([4000,3000,1000,2000]))