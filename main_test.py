import functions
obj=functions.funcs()
import pandas as pd
file=pd.read_csv('/Users/punisher/Desktop/x/0-1/data/nifty/AXISBANK-2.csv')
df=pd.DataFrame(file)
close_data=df['close']
tmst=df['date']
vol=df['volume']
op_data=df['open']
high_data=df['high']
low_data=df['low']
# =============================================================================
fast=[5,9,20,50]
slow=[9,20,50,100,200]
exit_ma=[5,9,20,50,100]
temp_var=0 
temp_var2=0 
choice=input("input choice ")

elif choice == '2':
    for i in fast:
        for j in slow:
            if i!=j and i<j:
                obj.mul_final(close_data,i,j)
    

elif choice =='3':
    obj.mul_sma_final(close_data,tmst)

    
elif choice == '5':
    temp_var = int(input("enter fast sma "))
    temp_var2= int(input("enter slow sma "))
    obj.mul_final(close_data,temp_var,temp_var2)
    

elif choice == '6':
    obj.tfs2(close_data,vol,high_data,low_data)
