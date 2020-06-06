import pandas as pd

if __name__=='__main__' :
    df = pd.read_csv('trade.csv')
    win = len(df[df["Profit"]>0]) / len(df)
    risk_reward = df[df["Profit"]>0]["Profit"].mean() / ((df[df["Profit"]<0]["Profit"].mean())*-1.0)
    risk_rate = (-1.0 * df[df["Profit"]<0]["Profit"].min()) / 1325153
    print("勝率(%): " + str(win*100) + "%")
    print("損益率（倍）: " + str(risk_reward))
    print("リスク資金比率(%): " + str(risk_rate*100) + "%")