class funcs:
    def check_profit(self,close):
        import talib as ta
        import pandas as pd
        opening_price=[]
        closing_price=[]
        profit=[]
        temp=[]
        temp2=[]
        sma5=ta.SMA(close,20)
        sma20=ta.SMA(close,50)
        length=len(close)
        for i in range(0,length):
            if sma5[i] > sma20[i] and sma5[i-1] < sma20[i-1]:
                x=close[i]
                opening_price.append(x)
                temp.append(i)
        for i in range(temp[0],length):
            if sma20[i] > sma5[i] and sma20[i-1] < sma5[i-1]:
                y=close[i]
                closing_price.append(y)
                temp2.append(i)
        for i in range(4):
            z=closing_price[i]-opening_price[i]
            profit.append(z)
            
        dict1={'sma5':sma5,'sma7':sma20}
        df=pd.DataFrame(dict1)
        print(df)
        print("**op prices**","\n",opening_price)  
        print("**cl prices**","\n",closing_price)
        print("**profit**","\n",profit)
        print("**op price sma array length**","\n",temp)
        print("**cl price sma array length**","\n",temp2)
    
#--------------------------------------------------------------------------------------
    def mul_sma(self,close):
        import talib as ta
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        #import seaborn as sns
        np.array(close)
        sma_fast=[5,9,20,100]
        sma_slow=[9,20,50,200]
        opening_price=[]                  #FAILURE
        closing_price=[]
        profit=[]
        temp=[]
        temp2=[]
        length=len(close)
        for i in range(0,3):
            fast_sma=ta.SMA(close,sma_fast[i])
            slow_sma=ta.SMA(close,sma_slow[i])
            plt.plot(fast_sma)
            plt.plot(slow_sma)
            plt.show()
# =============================================================================
#             ma={'fast_ma':fast_sma,'slow_ma':slow_sma}
#             df3=pd.DataFrame(ma)
#             print(df3)
# =============================================================================
            for i in range(1,length):
                if fast_sma[i] > slow_sma[i] and fast_sma[i-1] < slow_sma[i-1]:
                    x=close[i]
                    opening_price.append(x)
                    temp.append(i)
            for i in range(temp[0],length):
                if slow_sma[i] > fast_sma[i] and slow_sma[i-1] < fast_sma[i-1]:
                    y=close[i]
                    closing_price.append(y)
                    temp2.append(i)
            for i in range(5):
                z=((closing_price[i])-(opening_price[i]))
                profit.append(z)
                final={'op prices':opening_price,
                       'cl prices':closing_price,
                       'profit':profit,
                       'oparr len':temp,
                       'clarr len':temp2}
                finaldf=pd.DataFrame.from_dict(final, orient='index')
                finaldf = finaldf.transpose()
                net_profit=finaldf['profit'].sum()
                pd.set_option("display.max_rows", None,"display.max_columns",None)
            print(finaldf,'\n',"net profit=",net_profit) 
            del fast_sma
            del slow_sma
            final.clear()
            del finaldf
            for i in opening_price:
                opening_price.remove(i)
            for i in closing_price:
                closing_price.remove(i)
            for i in temp:
                temp.remove(i)
            for i in temp2:
                temp2.remove(i)
            print(opening_price,closing_price,temp,temp2)
            
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
# # =============================================================================
    def ma_pro3(self,close,x1,y1,z1):
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
        cap=30000
        sma5=ta.SMA(close,x1)
        sma20=ta.SMA(close,y1)
        sma9=ta.SMA(close,z1)            #FAILURE
        # plt.plot(close)
        # plt.plot(sma9)
        # plt.show()
        length=len(close)
        for i in range(0,length):
            if sma5[i] > sma20[i] and sma5[i-1] < sma20[i-1]:
                x=close[i]
                opening_price.append(x)
                temp.append(i)
        for j in range(temp[0],length-2):
            if  ((sma9[j-1])//1 > (sma9[j])//1) and ((sma9[j-2])//1 <= (sma9[j]//1)):
                b=close[j]
                closing_price.append(b)
                temp2.append(j)
                
        for i in range(len(closing_price)-5):
            z=closing_price[i]-opening_price[i]
            cap=((cap/opening_price[i])*z)+cap
            profit.append(z)  
        plt.plot(temp)
        plt.plot(temp2)
        plt.show()
        # print(profit)
        # mean1=sum(opening_price)/len(opening_price)
        # print(mean1)
        net_profit=sum(profit)
        lenm=len(profit)
        dict1={'ma combo':[[x1,y1,'*',z1]],
                'net_profit':[net_profit],
                'no.of.trades':[lenm],
                'capital appr':[cap],}  
        df=pd.DataFrame(dict1)
        print(df)
        # print(opening_price[:10],'\n',closing_price[:10],'\n',temp[:10],'\n',temp2[:10],'\n','ma combo',x1,y1,z1)
        # print("net profit=",net_profit,"/no.of trades",len(profit),'/MA comb=',x1,y1,z1,"/capital appriciation= ",cap)
# =============================================================================
    def p0(self,cl,op,hg,lw):
        import pandas as pd
        import matplotlib.pyplot as plt
        profit=[]
        trig=[]
        high=[]
        loss=[]
        count1=0
        count3=0 
        cl_len=len(cl)
        for i in range(3,cl_len):
            if(( cl[i-2] > cl[i-3]) and (cl[i-1] > cl[i-2]) and (op[i] > cl[i-1])):
                trig.append(cl[i])
                x=(hg[i])-op[i]
                high.append(hg[i])
                profit.append(x)
                if(x>2):
                    count1+=1
                elif(x==0):
                    x1=lw[i]-op[i]
                    loss.append(x1)
                    count3+=1
        dict={'op_price':trig,'hg_price':high,'profit':profit}
        df=pd.DataFrame(dict)
        plt.plot(profit)
        plt.plot(loss)
        plt.show()
        print(df,'\n','total trades',len(profit),
              '\n','profit count:',count1,
              '\n','loss count:',count3,'\n',
              'total profit:',sum(profit),'\n',
              'total loss:',sum(loss),'\n',
              'avg profit',(sum(profit)/1000000))
# =============================================================================
    def tfs2(self,close,vol,high,low):
        import talib as tl
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import ta
        bb=tl.BBANDS(close,20,2,2,0)
        # vwap=(np.cumsum(vol * close) / np.cumsum(vol))
        dict={"high":high,"low":low,"close":close,"volume":vol}
        df=pd.DataFrame(dict)
        vwap=ta.volume.VolumeWeightedAveragePrice(high=df['high'], 
        low=df['low'], close=df['close'], volume=df['volume'],
        window=20).volume_weighted_average_price()
        rsi=tl.RSI(close,14)
        # plt.plot(close)
        # plt.plot(bb)
        # plt.show()
        x=15
        m=x
        op_pr=[]
        cl_pr=[]
        op_len=[]
        cl_len=[]
        profit=[]
        temp1=[]
        temp=0
        kl=0
        while m!=len(close)-1:   
            flip=15
            for j in range(15):                                              #FAILURE
                if close[x] > vwap[x]:
                    flip=flip+0
                else:
                    flip=flip-1
                x=x-1
            if flip == 15 and (bb[2][m]*(1+0.005)) >= low[m]:
                op_pr.append(close[m])
                op_len.append(m)
            m=m+1
            x=m
        for l in range(op_len[0],len(close)-1):
            if rsi[l] >= 55 and bb[0][l] < high[l]:
                    cl_pr.append(close[l])
                    temp=l
                    cl_len.append(l)
                            
                
            
            
                
        dict1={'op':op_pr,'opl':op_len,'cll':cl_len,'cl_pr':cl_pr}
        # df1=pd.DataFrame(dict1)
        for i in range(10):
            
            print(op_len[i],cl_len[i],close[272],rsi[272],bb[0][272])
                    