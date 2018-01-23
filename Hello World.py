import matplotlib.pyplot as plt


print("Hello World!")
myfile=open("screenlog.0","r")





plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


text=myfile.read()
rcv1=text.find("rcv")+4      # This will give you the start position of the word (if it exists, otherwise -1)
rcv2=text.find("miss")-1

miss1=text.find("miss")+5      # This will give you the start position of the word (if it exists, otherwise -1)
miss2=text.find("boot")-1



rcv=text[rcv1:rcv2]
miss=text[miss1:miss2]



print(rcv+" "+miss)











