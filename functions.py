class funcs:

# =============================================================================
    def mul_sma_final(self,close,ts):
        import talib as ta
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        np.array(close)
        opening_price=[]
        closing_price=[]
        profit=[]
        drawdown=0
        temp=[]
        temp2=[]
        opts=[]
        opts1=[]
        x=int(input("input fast sma "))
        y=int(input("input slow sma "))
        sma5=ta.SMA(close,x)
        sma20=ta.SMA(close,y)
        plt.plot(close)
        plt.plot(sma5)
        plt.plot(sma20)
        plt.show()
        length=len(close)
        for i in range(1,length):
            if sma5[i] > sma20[i] and sma5[i-1] < sma20[i-1]:
                x=close[i]
                opening_price.append(x)
                temp.append(i)
                ex1=ts[i]
                opts.append(ex1)
        for i in range(temp[0],length):
            if sma20[i] > sma5[i] and sma20[i-1] < sma5[i-1]:
                y=close[i]
                closing_price.append(y)
                temp2.append(i)
                ex2=ts[i]
                opts1.append(ex2)
        for i in range(len(opening_price)-2):
            z=closing_price[i]-opening_price[i]
            profit.append(z)
            final={'opts':opts,
                   'op prices':opening_price,
                   'cl prices':closing_price,
                   'clts':opts1,
                   'profit':profit,
                   'oparr len':temp,
                   'clarr len':temp2}
            finaldf=pd.DataFrame.from_dict(final, orient='index')
            finaldf = finaldf.transpose()
            net_profit=finaldf['profit'].sum()
            pd.set_option("display.max_rows", None,"display.max_columns",None)
        print(finaldf,'\n',"net profit=",net_profit,'\n',"no.of trades",len(profit))
        drawdown=min(profit)
        print("drawdown ", drawdown)
# =============================================================================
    def mul_final(self,close,x1,y1):
        import talib as ta
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        np.array(close)
        opening_price=[]
        closing_price=[]
        profit=[]
        temp=[]
        temp2=[]
        cap=100000
        capapp=[]
        sma5=ta.SMA(close,x1)
        sma20=ta.SMA(close,y1)
        # plt.plot(close)
        # # plt.plot(sma5)
        # # plt.plot(sma20)
        # plt.show()
        length=len(close)
        for i in range(1,length):
            if sma5[i] > sma20[i] and sma5[i-1] < sma20[i-1]:
                x=close[i]
                opening_price.append(x)
                temp.append(i)
        for i in range(temp[0],length):
            if sma20[i] > sma5[i] and sma20[i-1] < sma5[i-1]:
                y=close[i]
                closing_price.append(y)
                temp2.append(i)
        for i in range(len(opening_price)-2):
            z=closing_price[i]-opening_price[i]
            cap=((cap/opening_price[i])*z)+cap
            profit.append(z)
            capapp.append(cap)
            net_profit=sum(profit)
            lenm=len(profit)
        # print(temp[:20],'\n',temp2[:20],'\n',x1,y1)
        # plt.plot(sma5[:50])
        # plt.plot(sma20[:50])
        # plt.show()
        hold=close[length-1] - close[0]
        dict1={'ma combo':[[x1,y1]],
              'net_profit':[net_profit],
              'no.of.trades':[lenm],
              'capital appr':[cap],
              'hold':hold}  
        df=pd.DataFrame(dict1)
        print(df)
        drawdown=min(profit)
        print("drawdown ", drawdown)
        plt.plot(profit)
        plt.show()
        plt.plot(capapp)
        plt.show()
        # print("net profit=",net_profit,"/no.of trades",len(profit)
        # ,'/MA comb=',x1,y1,"/capital appriciation= ",cap)

# =============================================================================
    
