
import pandas as pd
import matplotlib.pyplot as plt

path="C:/Users/picheeng/Desktop/python/matplotlib/"
df = pd.read_excel(r"C:\Users\picheeng\Desktop\Tool SPC.xlsx")
#print (df)
date_list=df['date'].tolist()
tool_list=df['tool'].tolist()
recess_list=df['recess'].tolist()
UCL_list=df['UCL'].tolist()
LCL_list=df['LCL'].tolist()
target_list=df['target'].tolist()
plt.plot(date_list,recess_list,linestyle='-',color='blue')
plt.plot(date_list,UCL_list, linestyle=':',color='red')
plt.plot(date_list,LCL_list, linestyle=':',color='red')
plt.plot(date_list,target_list, linestyle=':',color='green')
my_dpi=200
#plt.figure(figsize=(800/my_dpi, 800/my_dpi), dpi=my_dpi)
#plt.suptitle('test title', fontsize=25)
plt.title("Test 2", fontsize=25)

#plt.axis([0, 10, 0, 10])
plt.text(date_list[0], ((UCL_list[0]-LCL_list[0])*1.1+LCL_list[0]) , "TEST",color='red')
plt.savefig(path+"filename.png", dpi=my_dpi)
