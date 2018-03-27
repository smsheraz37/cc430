import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('serial.csv',usecols=[0,1,2,3,4])      # Reads the file only column 0 to column 4


df = df.sort_values('node_id')                           # Sort data by node_id
df.to_csv('serial_sorted.csv', index=False)             # outputs sorted csv file


nodes = []
counter = 0

for x in range (1,34):                                                     # Separate Each Node Data
    current_node = df['node_id'] == x
    current_node = df[current_node]
    current_node = current_node.sort_values('# timestamp',ascending=False) # Sort data by timestamp
    nodes.append(current_node)
    nodes[counter].to_csv('node%d.csv'%x, index=False)
    counter = counter +1

received = []
missed = []
node_id = []

total_received = 0.0
total_missed = 0.0

for x in range(1,34):
    current_file = open("node%d.csv"%x,"r")
    current_text = current_file.read()

    rcv1 = current_text.find("rcv")  # gives start position of quoted word +4 for rcv= in rcv=47
    if rcv1 != -1:
        node_id.append(x)
        rcv1 = rcv1 + 4
        rcv2 = current_text.find("miss") - 1
        rcv = current_text[rcv1:rcv2]
        total_received = total_received + float(rcv)
        received.append(float(rcv))

    miss1 = current_text.find("miss")   # This will give the start position of the word (if it exists, otherwise -1)
    if miss1 != -1:
        miss1 = miss1 + 5
        miss2 = current_text.find("boot") - 1
        miss = current_text[miss1:miss2]
        total_missed = total_missed + float(miss)
        missed.append(float(miss))

print(received)
print(missed)
print(node_id)
print(total_received,"R  M",total_missed,total_received*100/(total_missed+total_received))



A=0.0

B=0.0
C=0.0
reliability_success = []
reliability_failure = []
for x in range(0,23):                   # for conversion to percentage
    A = received[x]
    B = missed[x]
    C = A + B
    A = 100.0 * A / C
    B = 100.0 * B / C
    reliability_success.append(A)
    reliability_failure.append(B)
print(reliability_success)
print(reliability_failure)              # ////////////////////////////

A = reliability_success
B = reliability_failure

X = range(23)

# bar(x, height, width, bottom, *, align='center', **kwargs)
plt.figure(1)
p1=plt.bar(X, A, 0.4, color = 'g')
p2=plt.bar(X, B, 0.4,  color = 'r', bottom = A)

plt.ylabel('Reliability (in Percentage %)')
plt.xlabel('Node ID')
plt.title('Reliability of Different Nodes')
plt.xticks(X, node_id)
plt.legend((p1,p2),('Received Packets','Missed Packets'),loc='upper right', bbox_to_anchor=(1,1.15))



plt.figure(2)

labels = 'Received', 'Missed'
sizes = [total_received*100/(total_missed+total_received),100.0-(total_received*100/(total_missed+total_received))]
colors = ['green', 'red']
explode = (0.1, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Overall Reliability')
plt.legend((p1,p2),('Received Packets','Missed Packets'),loc='upper right', bbox_to_anchor=(1,1.15))
plt.axis('equal')



plt.show()
































#node3 = df['node_id'] == 3
#node3 = df[node3]
#nodes.append(node3)
#nodes[1].to_csv('node%d.csv'%x[1], index=False)





#print "We're on time %d" % (x)



#print(node1)




"""

rcv1 = text.find("rcv")+4       # gives start position of quoted word +4 for rcv= in rcv=47
rcv2 = text.find("miss")-1
rcv = text [rcv1:rcv2]          # prints characters from rcv1 to rcv2 in text

miss1 = text.find("miss") + 5
miss2 = text.find("boot") - 1
miss  = text [miss1:miss2]
#print (rcv)
#print (miss)


A = int(rcv)
B = int(miss)
C = A + B
A = [(100 * A)/C,40,70]
B = [(100 * B)/C,60,30]


X = range(3)

#bar(x, height, width, bottom, *, align='center', **kwargs)
plt.bar(X, A, 0.3, color = 'g')
plt.bar(X, B, 0.3,  color = 'r', bottom = A)

plt.ylabel('Reliability (in Percentage %')
plt.title('Reliability Vs Different Payloads')
plt.xticks(X, ('P1', 'P2', 'P3'))
#plt.show()



#df = pd.DataFrame(df, columns = ['# timestamp', 'observer_id', 'node_id', 'direction','output'])


#rcv2=text.find("miss")-1

"""


"""
myFile = open("screenlog.0","r")


#myCSVFile = pd.read_csv('serial.csv', header = None)


#df = csv.reader(open("example.csv",'r'))

#sortedlist = sorted(df, key=operator.itemgetter(3), reverse=True)
#myCSVFile = open("serial.csv","r")


plt.plot([1,2,3,4],[5,2,7,2])
plt.ylabel("yaxis")
plt.show()

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")pip
plt.show()

 myFile = open("screenlog.0", "r")

plt.plot([1, 2, 3, 4])
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
"""











