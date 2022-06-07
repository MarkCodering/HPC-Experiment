Investment2454 = []
Investment3293 = []
Investment3008 = []
Investment6732 = []
Investment2357 = []
orginalInvestment = 148000 #In NTD
investmentCost = []
dividendDict = {'2454': 73.00, '3293': 42, '3008': 39, '6732': 30, '2357': 26}
priceDict = {'2454': 890.00, '3293': 754.00, '3008': 1770.00, '6732': 337.50, '2357': 339.00}
investAmount = {'2454': 890.00, '3293': 754.00, '3008': 1770.00, '6732': 337.50, '2357': 339.00}
profit = []
maxInvestmentCost = 0

def stockProfileCalc(dividendDict, investAmount, investmentCost, priceDict):
    i = 0
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):
                for d in range(0, 1000):
                    for e in range(0, 1000):
                        investAmount['2454'] = a
                        investAmount['3293'] = b
                        investAmount['3008'] = c
                        investAmount['6732'] = d
                        investAmount['2357'] = e
                        investmentCost.append(investAmount['2454'] * priceDict['2454'] + investAmount['3293'] * priceDict['3293'] + investAmount['3008'] * priceDict['3008'] + investAmount['6732'] * priceDict['6732'] + investAmount['2357'] * priceDict['2357'])
                        profit.append(investAmount['2454'] * dividendDict['2454'] + investAmount['3293'] * dividendDict['3293'] + investAmount['3008'] * dividendDict['3008'] + investAmount['6732'] * dividendDict['6732'] + investAmount['2357'] * dividendDict['2357'])
                        print('Counter: ', i, 'Completed: ', round((i/(1000*1000*1000*1000*1000))*100, 2),'%', 'A:',a, 'B', b,'C', c,'D', d,'E', e,'Cost',investmentCost[i] ,'Profit:', profit[i])
                        i += 1

    return max(profit)

print("Result: maximum profit = ", stockProfileCalc(dividendDict, investAmount, investmentCost, priceDict))

def impossibleOptionFilter(orginialInvestment, investmentCost):
    for i in range(0, 1000^5):
        if investmentCost[i] > orginialInvestment:
            investmentCost[i] = 0

    for i in range(0, 1000^5):
        print(investmentCost[i])

    maxInvestmentCost = max(investmentCost)
    print(maxInvestmentCost)

    #Search for the parameter that is the highest value in the investmentCost list
    #If the value is greater than the orginialInvestment, then the investment is impossible
    #If the value is less than the orginialInvestment, then the investment is possible
    #If the value is equal to the orginialInvestment, then the investment is possible
    index = 0
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):
                for d in range(0, 1000):
                    for e in range(0, 1000):
                        if investmentCost[index] == maxInvestmentCost:
                            print('A:',a, 'B', b,'C', c,'D', d,'E', e, 'Max Investment Cost:', maxInvestmentCost, 'Profit:', profit[index])
                        index += 1 

impossibleOptionFilter(orginalInvestment, investmentCost)