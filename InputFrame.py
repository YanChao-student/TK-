class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master) #继承了Frame的init方法，意为把当前类定义为Frame
        self.root = master
        self.E1 = Entry(self)#定义文本输入框
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.creatpage() #启动页面

    def creatpage(self): #此处的布局很简陋无任何装饰，如想要漂亮的页面建议采用Figma
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text="姓名").grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text="学号").grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self, text="科目").grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E)
        Label(self, text="成绩").grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)
        Button(self, text="提交", command=self.click).grid(row=6, stick=E, column=1, pady=10)

    def Isspace(self, text): #检查Entry中是否为空
       
        for i in text:
            if not i.isspace():
                return False
            else:
                return True

    def click(self): #和Button绑定的事件，点击左键触发
        name = self.E1.get() #get()时Tkinter中定义的方法，取出Entry中的值。
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score):
            print("输入项不能为空")
            messagebox.showinfo(title="提示", message="输入项不能为空")
        else:
            print("调用write()")
            self.write(name, num, course, score)

    def write(self, name, num, course, score):
        f = open('成绩.csv', 'r', encoding='utf-8')
        for line in f.readlines(): #readlines()一次性读取全部文本，并生成一个列表，这个列表中的元素是按行分割的。
            info = line[:-1].split(',') #去除行末换行符
            if len(info) < 4: #检查信息是否齐全
                break
            if name == info[0] and num == info[1]:
                messagebox.showinfo(title="提示", message="信息已经存在")
                f.close()
                return
        f = open('成绩.csv', 'a', encoding='utf-8')
        f.write('{},{},{},{}\n'.format(name, num, course, score))
        f.close()
        messagebox.showinfo(title="提示", message="信息写入成功")
