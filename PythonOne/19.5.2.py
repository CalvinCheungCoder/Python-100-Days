import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='StaticBox 布局', size=(300, 120))
        self.Center()
        panel = wx.Panel(parent=self)
        # 创建垂直方向的 Box 布局管理器对象
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='Default text')
        # 添加静态文本到 Box 布局管理器
        vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)

        b1 = wx.Button(parent=panel, id=10, label='Button1')
        b2 = wx.Button(parent=panel, id=11, label='Button2')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)

        sb = wx.StaticBox(panel, label='按钮框')
        hsbox = wx.StaticBoxSizer(sb, wx.HORIZONTAL)

        hsbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        hsbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

        vbox.Add(hsbox, proportion=1, flag=wx.CENTER)

        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('点击了 Button1')
        else:
            self.statictext.SetLabelText('点击了 Button2')


class App(wx.App):

    def OnInit(self):
        # 创建对象窗口
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop() # 进入主事件循环