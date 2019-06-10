import wx

# 一对一事件处理

# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent = None, title = '一对一事件处理', size = (300, 180))
#         self.Center()
#         panel = wx.Panel(parent = self)
#         self.statictext = wx.StaticText(parent = panel, pos = (110, 20))
#         b = wx.Button(parent = panel, label = 'OK', pos = (100, 50))
#         self.Bind(wx.EVT_BUTTON, self.on_click, b)
#
#     def on_click(self, event):
#         print(type(event)) # <class 'wx._core.CommandEvent'>
#         self.statictext.SetLabelText('Hello World')
#
# class App(wx.App):
#     def OnInit(self):
#         frame = MyFrame()
#         frame.Show()
#         return True
#
# if __name__ == '__main__':
#     app = App()
#     app.MainLoop()


# 一对多事件处理

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='一对多事件处理', size=(300, 180))
        self.Center()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(110, 15))
        b1 = wx.Button(parent=panel, id=10, label='button1', pos=(100, 45))
        b2 = wx.Button(parent=panel, id=11, label='button2', pos=(100, 85))
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)
        self.Bind(wx.EVT_BUTTON, self.on_click, id=11)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1 点击')
        else:
            self.statictext.SetLabelText('Button2 点击')

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()