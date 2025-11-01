def maximumWealth(accounts):
    maxWealth= 0
    for customer in accounts:
        wealth = 0
        for banks in customer:
            wealth += banks
        maxWealth = max(maxWealth, wealth)
    return maxWealth

print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))