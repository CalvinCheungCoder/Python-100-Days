import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='静态文本和按钮', size=(300, 200))
        self.Center()
        panel = wx.Panel(parent=self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.statictext = wx.StaticText(parent=panel, label='Statictext 1', style=wx.ALIGN_CENTER_HORIZONTAL)

        b1 = wx.Button(parent=panel, label='OK')
        self.Bind(wx.EVT_BUTTON, self.on_click, b1)

        b2 = wx.ToggleButton(panel, -1, 'ToggleButton')
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)

        bmp = wx.Bitmap('icon/1.png', wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel, -1, bmp)
        self.Bind(wx.EVT_BUTTON, self.on_click, b3)

        vbox.Add(100, 10, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND)

        panel.SetSizer(vbox)

    def on_click(self, event):
        self.statictext.SetLabelText('Hello World')


class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()