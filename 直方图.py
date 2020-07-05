# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:59:25 2020

@author: dell
"""

# 直方图
plt.figure(figsize=(22, 7))  # 设置图片初始化大小
p1 = plt.bar(x=contrast_province, height=today_add) # x轴，y轴
plt.xticks(contrast_province,fontproperties=my_font, fontsize=10) # 设置字体
plt.title('%s各省份每日增长数据' % today, fontproperties=my_font, fontsize=30) 
plt.xlabel('省份', fontproperties=my_font, fontsize=10) # 小标签：提示信息
plt.ylabel('日增(人)', fontproperties=my_font,fontsize=10)
plt.savefig('各省份每日增长数据-直方图.png',dpi=400) # 保存图片：格式、分辨率
plt.legend()# 图例
plt.show() # 展示出来