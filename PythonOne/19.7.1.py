import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='分隔窗口', size=(350, 180))
        self.Center()

        splitter = wx.SplitterWindow(self, -1)
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)
        splitter.SplitVertically(leftpanel, rightpanel, 100)
        splitter.SetMinimumPaneSize(80)

        list = ['苹果', '橘子', '香蕉']
        lb = wx.ListBox(leftpanel, -1, choices=list, style=wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.on_listbox,lb)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(lb, 1, flag=wx.ALL | wx.EXPAND, border=5)
        leftpanel.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.content = wx.StaticText(rightpanel, label='右侧面板')
        vbox2.Add(self.content, 1, flag=wx.ALL | wx.EXPAND, border=5)
        rightpanel.SetSizer(vbox2)

    def on_listbox(self, event):
        s = '选择 {0}'.format(event.GetString())
        self.content.SetLabel(s)

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()