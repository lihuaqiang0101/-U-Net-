# import os
#
# count = 0
#
# datasets = os.listdir('整理的数据集')
# datasets.sort(key=lambda x:int(x))
# with open('yingyang.txt','r') as f:
#     lables = f.read()
# for i in range(len(datasets)):
#     dirs = os.listdir('整理的数据集/'+datasets[i])
#     for dir in dirs:
#         imgs = os.listdir('整理的数据集/'+datasets[i]+'/'+dir)
#         # imgs.sort(key=lambda x:int(x[:5]))
#         for img in imgs:
#             if len(img) == 9:
#                 if lables[i] == '-':
#                     os.system("mv '整理的数据集/{}/{}/{}' tumour/0_{}.png".format(datasets[i],dir,img,count))#阴性记为0
#                     count += 1
#                 elif lables[i] == '+':
#                     os.system("mv '整理的数据集/{}/{}/{}' tumour/1_{}.png".format(datasets[i], dir, img, count))  # 阳性记为1
#                     count += 1
# #     for img in imgs:
# #         if img.split('.')[1] == 'png':
# #             os.system("mv '../B题-全部数据/数据集1/{}/{}/{}' train/GT/{}.png".format(dataset, dirs[1], img,str(count1)))
# #             count1 += 1
# #         elif img.split('.')[1] == 'dcm':
# #             os.system("mv '../B题-全部数据/数据集1/{}/{}/{}' train/image/{}.dcm".format(dataset, dirs[1], img,str(count2)))
# #             count2 += 1

import matplotlib.pyplot as plt
with open('F1','r') as f:
    F = f.readlines()
x = []
y = []
for fs in F:
    datas = fs.strip()
    datas = datas.split(',')
    x.append(int(datas[0][5:]))
    y.append(float(datas[1][8:]))
plt.plot(x,y)
plt.title('F1')
plt.xlabel("x")
plt.ylabel("y") # 步骤一    （宋体）
plt.show()
# plt.waitforbuttonpress(0)
# for i in range(len(x)):
#     print(x[i]20,y[i])
