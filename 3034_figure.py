import matplotlib.pyplot as plt
import twstock

stock_3034=twstock.Stock('3034')
stocklist=stock_3034.fetch_31()
high_3034=[]
low_3034=[]
close_3034=[]
listy=[]
for i in stocklist:
    high_3034.append(i.high)
    low_3034.append(i.low)
    close_3034.append(i.close)
    listy.append(i.date.strftime('%m-%d'))

plt.figure(figsize=[20,10])
plt.plot(listy,high_3034,'r-.*',lw=2,ms=10,label='High')
plt.plot(listy,low_3034,'g-.p',lw=2,ms=10,label='low')
plt.plot(listy,close_3034,'y-.o',lw=2,ms=10,label='close')
plt.legend(fontsize=16)
# plt.ylim(300,600)
plt.title('3034 Stock',fontsize=28)
plt.xlabel('Date',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.grid(color='k',ls=':',lw=1,alpha=0.5)
plt.show()
