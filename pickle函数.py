#用于存储历史记录， 把数据存储到本地文件
import pickle

q = [1,2,4,5]
pickle.dump(q,open('his','wb'))        #数据存储到本地his文件
print(pickle.load(open('his','rb')))   #调用his文件显示数据
