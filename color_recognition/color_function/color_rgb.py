# -*- coding: utf-8 -*-
from haishoku.haishoku import Haishoku
import matplotlib.pyplot as plt

image='D:/py/测试图片2.png'
haishoku = Haishoku.loadHaishoku(image)
a=haishoku.palette  #palette函数输出配色色号
print(a)
rgb_list = [[i[1][0] / 255, i[1][1] / 255, i[1][2] / 255]
            for i in haishoku.palette] #色号简单转化为matplotlib可用的0～1之间RGB色号
plt.figure(dpi=120)
plt.style.use('bmh')
plt.bar(range(2, 10), range(2, 10), color=rgb_list)  #传入Haishoku提取的颜色号
plt.title('Colored with Haishoku', size=10)
plt.show()
#haishoku.showPalette(image)#showPalette函数预览上面提取出的配色
print("程序结束")