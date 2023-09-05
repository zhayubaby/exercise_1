f = open(r'file_to_read.txt','r')
#str = f.read()
lines = f.readlines()
count = {'terrible':0}
for line in lines:
    line1 = line.split(' ')
    for word in line1:
        if word in count:
            count[word]+=1
 
count = sorted(count.items(),key=lambda item:item[1],reverse=True)
print(count)