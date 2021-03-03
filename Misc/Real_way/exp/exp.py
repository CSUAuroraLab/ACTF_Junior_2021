import os
import random

m=[]
for i in range(7):
    m.append(chr(ord('a')+i))

print("数据量："+str(m))
strmap=[]
flag_map=[]
for i1 in m:
    for i2 in m:
        for i3 in m:
            for i4 in m:
                for i5 in m:
                    temp=i1+'\\'+i2+'\\'+i3+'\\'+i4+'\\'+i5
                    strmap.append(temp)
                    temp=i1+i2+i3+i4+i5
                    flag_map.append(temp)
#print(strmap)

def makemap(level,list_map):
    if level>0:
        level-=1
        makemap


def makedir():
    for p in strmap:
        this='C:\\Users\\mxy\\Downloads\\Real_way'
        #path=os.path.abspath('.')+'\\misc_test\\'+p
        path=this+'\\misc_test\\'+p
        os.makedirs(path)
        temp=open(path+'\\flag.txt','w')
        temp.write('actf{'+flag_map[random.randint(0, len(strmap)-1)]+'}')
    
def checkflag():
    basepath='C:\\Users\\mxy\\Downloads\\Real_way'
    #basepath=os.path.abspath('.')
    ans=[]
    for i in range(len(strmap)):
        path=basepath+'\\misc_test\\'+strmap[i]+'\\flag.txt'
        file=open(path,'r')
        flag=file.readline()
        if flag_map[i]==flag[5:flag.find('}')]:
            #print(flag)
            ans.append(flag)
        #else:
            
            #print('error ' +flag_map[i]+' : '+flag[5:flag.find('}')])
            #print(flag[5:flag.find('}')])
        file.close()
    return ans
        
        
    

if __name__=='__main__':
    #makedir()
    print('目录扫描ing')
    ans=checkflag()
    print(ans)