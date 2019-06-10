import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Grid 布局', size=(300, 300))
        self.Center()
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, label='1')
        btn2 = wx.Button(panel, label='2')
        btn3 = wx.Button(panel, label='3')
        btn4 = wx.Button(panel, label='4')
        btn5 = wx.Button(panel, label='5')
        btn6 = wx.Button(panel, label='6')
        btn7 = wx.Button(panel, label='7')
        btn8 = wx.Button(panel, label='8')
        btn9 = wx.Button(panel, label='9')

        grid = wx.GridSizer(cols=3, rows=3, vgap=0, hgap=0)

        grid.AddMany([
            (btn1, 0, wx.EXPAND),
            (btn2, 0, wx.EXPAND),
            (btn3, 0, wx.EXPAND),
            (btn4, 0, wx.EXPAND),
            (btn5, 0, wx.EXPAND),
            (btn6, 0, wx.EXPAND),
            (btn7, 0, wx.EXPAND),
            (btn8, 0, wx.EXPAND),
            (btn9, 0, wx.EXPAND)
        ])

        panel.SetSizer(grid)

class App(wx.App):

    def OnInit(self):
        # 创建对象窗口
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop() # 进入主事件循环