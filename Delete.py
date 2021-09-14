from tkinter import * 
form tkinter.messagebox import  *

class DeleteFrame(Frame): #继承Frame类
	def __init__(self,master = None):
		Frame.__init__(self,master) #初始化一个Frame，这是后续creatPage的基础
		self.E1 = Entry(self)
		self.E2 = Entry(self)
		self.createPage()
    
		# createPage()的功能：创建用户交互界面
	def createPage(self): #在Frame的基础上创建widget
		Label(self).grid(row = 0 , stick = W,pady = 20) # row为排，column为列，此处为0排0列，pady向y轴填充20，用以调整组件和顶部框的距离。
		Label(self,text = "学号").grid(row = 1,column = 0,pady = 10)
		self.E1.grid(row = 1,column = 1,pady = 10)
		Label(self,text = "科目").grid(row = 2 ,column = 0,pady = 10)
		self.E2.grid(row = 2,column = 1,pady = 10)
		Button(self,text = "删除",command =self.click ).grid(row = 4,column = 1) # 这是一个按钮，执行表单的提交
	
    #表单提交
  def click(self):
			num = self.E1.get() # get()是Tkinter中的方法，用来取出Entry中的内容
			course = self.E2.get()
		if Isspace(num) or Isspace(course): #如果文本框为空则执行以下操作
			messagebox.showinfo(title = "Warning",message = "Can'not input nothing")
		else:
			self.delete(num ,course)
	
   #检查文本框是否为空，
  def Isspace(self,text):
		for i in text:
			if not i.isspace():
				return False
			else:
				return True
	
	def delete(self,num,course):
		temp = 0
		with open('成绩.csv','r',encoding = "utf-8") as f:
			lines = f.readlines()
		with open('成绩.csv','w',encoding = "utf-8") as f:
			for line in lines:
				info = line[:-1].split(',')
				if len(info) < 4 :
					break
				if num = infop[1] and course = info[2]:
					temp = 1
					continue
				f.write(line) #你想要删除的内容在continue中被返回了没有被f.write(line)写入，所谓删除使用覆盖的方式实现的。
		if temp == 0:
			messagebox.showinfo(title = "Warning",message = "你想要删除的信息不存在")
		else:
			messagebox.showinfo(title = "Warning",message = num +' '+"已经被删除")
