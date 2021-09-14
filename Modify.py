class ModifyFrame(Frame):
	def creatPage(self):
		Label(self).grid(row = 0 ,pady = 10)
		Label(self,text = "姓名").grid(row = 1 ,column = 0,pady=10)
		self.E1.grid(row = 1,column = 1,pady=10)
		Label(self,text = "学号").grid(row = 2,column = 0,pady=10)
		self.E2.grid(row = 2,column = 1,pady=10)
		Label(self,text = "科目").grid(row = 3 , column = 0,pady=10)
		self.E3.grid(row = 3 ,column = 1,pady=10)
		Label(self,text = "成绩").grid(row = 4 ,column =0,pady=10)
		self.E4.grid(row = 4 ,column =1,pady=10)
		Button(self,text = "Modify",command= self.click).grid(row = 8,column = 1,pady=10)
	def Isspace(self,text):
		temp = 0
		for i in text:
			if not i.isspace():
				return False
			else:
				return True
	def modify(self,name,num,course,score):
		temp = 0
		f = open('成绩.csv','r',encoding = 'utf-8')
		lines = f.readlines()
		print(lines)
		f = open('成绩.csv','w',encoding = 'utf-8')
		for line in lines :
			info = line[：-1].split(',') #报错：-1前没有:，导致info为空，现已修正
			print(info)
			if info[0] == name and info[1] == num:
				print(info)
				print(info[0],info[1])
				temp = 1
				f.write('{},{},{},{}\n'.format(name,num,course,score))#此处报错，原因为format前面用的是,而不是.
				#报错TypeError: format() takes at most 2 arguments (4 given)
				continue
			f.write(line)
		if temp == 0 :
			messagebox.showinfo(title = "Warning",message = "Fail writing"+' '+name)
		else:
			messagebox.showinfo(title = "Congratulation !",message = "Succee!")

	def click(self):
		name = self.E1.get()
		num = self.E2.get()
		course = self.E3.get()
		score = self.E4.get()
		if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score):
			messagebox.showinfo(title="Warning", message="Can't input space")
		else:
			self.modify(name, num, course, score)

	def __init__(self, master=None):
			Frame.__init__(self, master)
			self.E1 = Entry(self)
			self.E2 = Entry(self)
			self.E3 = Entry(self)
			self.E4 = Entry(self)
			self.creatPage()
