import argparse
import io

# 特性方程式(x = px^(k+1) + (1-p))のxの値を取得する。
def getX(incomeRate, winningRate):
    k = incomeRate
    p = winningRate
    
    resultX = 0.00
    memory = -0.01
    # px^(k+1) + (1-p) - xの式を
    # xを0.000～1.000まで0.001刻みで計算
    # x>=0の条件でもっとも0に近い値を算出する。
    for i in range(1, 1000, 1):
        x = i/1000
        check = p * pow(x, k+1) + (1 - p) - x
        if check < 0:
            check *= -1

        if memory == -0.01 or memory > check:
            memory = check
            resultX = x

    return resultX
    
# バルサラの破産確率を取得する
# 1st: costRate 資金に対する最大損失の割合
# 2st: incomePercent 損益率
# 3st: winningPercent 勝率
def getBankruptcyPercent(costRate, incomePercent, winningPercent):
    if winningPercent == 100:
        return 0.0

    incomeRate = incomePercent / 100
    winningRate = winningPercent / 100
    
    # p≦b/(a + b)の場合は必ず破産。
    # b/(a+b) = 1/(incomeRate+1)
    # b: 損失額 、 a: 利益額
    if winningRate <= 1/(incomeRate+1):
        return 1.0
    
    return pow(getX(incomeRate,winningRate),1/costRate)

if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    # 資金に対する損失率
    argParser.add_argument("costRate")
    args = argParser.parse_args()
    
    costRate    = float(args.costRate) # 資金に対する最大損失の割合
    winningPercent = 10         # 勝率[%]
    incomePercent  = 10         # 損益率[%]

    # 損益率は10%ずつ増やしていく
    incomeInterval = 10
    winInterval = 10
    
    print("," , end='')
    for i in range(9):
        print(str(winningPercent) + "," , end='')
        winningPercent += winInterval
    print()
    winningPercent = 20
    
    for i in range(20):
        winningPercent = 20
        bankruptcyPercentList = []
        # 勝率は10%ずつ増やしていく
        for j in range(9):
            bankruptcyPercentList.append(getBankruptcyPercent(costRate, incomePercent, winningPercent))
            winningPercent += winInterval
        
        print(str(incomePercent) + "," , end='')
        for k in bankruptcyPercentList:
            print( "{0:.2f}".format(k*100) + "," , end='')
        
        print()
        
        incomePercent += incomeInterval