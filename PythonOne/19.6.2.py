import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(400, 200))
        self.Center()
        panel = wx.Panel(parent=self)

        fgs = wx.FlexGridSizer(3, 2, 10, 10)

        userid = wx.StaticText(panel, label='用户ID：')
        pwd = wx.StaticText(panel, label='密码：')
        content = wx.StaticText(panel, label='多行文本：')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel, style = wx.TE_PASSWORD)
        tc3 = wx.TextCtrl(panel, style = wx.TE_MULTILINE)

        tc1.SetValue('tony')
        print('读取用户ID：{0}'.format(tc1.GetValue()))

        fgs.AddMany([userid, (tc1, 1, wx.EXPAND),
                     pwd, (tc2, 1, wx.EXPAND),
                     content, (tc3, 1, wx.EXPAND)])

        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableRow(2, 3)
        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        panel.SetSizer(hbox)

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()