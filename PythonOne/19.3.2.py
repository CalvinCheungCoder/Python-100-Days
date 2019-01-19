import wx

# 第一部分：简单实现 ---------------------------------------------------------------------------------------

# first
# app = wx.App()
# frm = wx.Frame(None, title = '第一个 GUI 程序', size = (400,300), pos = (100,100))
# frm.Show()
#
# app.MainLoop()


# 第二部分：自定义窗口类 MyFrame  ---------------------------------------------------------------------------

# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent = None, title = "第一个 GUI 程序", size = (400,300), pos = (100,100))
#
#
# class App(wx.App):
#     def OnInit(self):
#         # 创建对象窗口
#         frame = MyFrame()
#         frame.Show()
#         return True
#
#     def OnExit(self):
#         print('应用程序退出')
#         return 0
#
# if __name__ == '__main__':
#     app = App()
#     app.MainLoop() # 进入主事件循环


# 第三部分：显示静态文本  -----------------------------------------------------------------------------------

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None, title = "第一个 GUI 程序", size = (400,300))
        self.Center() # 设置窗口居中
        panel = wx.Panel(parent = self)
        statictext = wx.StaticText(parent = panel, label = 'Hello World!', pos = (10, 10))

class App(wx.App):

    def OnInit(self):
        # 创建对象窗口
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop() # 进入主事件循环