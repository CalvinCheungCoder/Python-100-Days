import wx
import wx.grid

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='使用菜单', size=(550, 500))
        self.Center()

        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.text, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
        self.SetSizer(vbox)

        menubar = wx.MenuBar()

        file_menu = wx.Menu()
        new_item = wx.MenuItem(file_menu, wx.ID_NEW, text='新建', kind=wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU, self.on_newitem_click, id=wx.ID_NEW)
        file_menu.Append(new_item)
        file_menu.AppendSeparator()

        edit_menu = wx.Menu()
        copy_item = wx.MenuItem(edit_menu, 100, text='复制', kind=wx.ITEM_NORMAL)
        edit_menu.Append(copy_item)

        cut_item = wx.MenuItem(edit_menu, 101, text='剪切', kind=wx.ITEM_NORMAL)
        edit_menu.Append(cut_item)

        paste_item = wx.MenuItem(edit_menu, 102, text='粘贴', kind=wx.ITEM_NORMAL)
        edit_menu.Append(paste_item)

        self.Bind(wx.EVT_MENU, self.on_editmenu_click, id=100, id2=102)

        file_menu.Append(wx.ID_ANY, "编辑", edit_menu)
        menubar.Append(file_menu, '文件')
        self.SetMenuBar(menubar)


        tb = wx.ToolBar(self, -1)
        self.ToolBar = tb
        tsize = (24, 24)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp =  wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY,wx.ART_TOOLBAR,tsize)
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE,wx.ART_TOOLBAR,tsize)

        tb.AddTool(10,'New',new_bmp,kind=wx.ITEM_NORMAL,shortHelp='New')
        tb.AddTool(20,'Open',open_bmp,kind=wx.ITEM_NORMAL,shortHelp='Open')
        tb.AddTool(30,'Copy',copy_bmp,kind=wx.ITEM_NORMAL,shortHelp='Copy')
        tb.AddTool(40,'Paste',paste_bmp,kind=wx.ITEM_NORMAL,shortHelp='Paste')

        tb.AddTool(201,'back',wx.Bitmap("menu_icon/back.png"),kind=wx.ITEM_NORMAL,shortHelp='Back')
        tb.AddTool(202,'forward',wx.Bitmap("menu_icon/forward.png"),kind=wx.ITEM_NORMAL,shortHelp='forward')
        self.Bind(wx.EVT_MENU, self.on_click, id=201, id2=202)
        tb.AddSeparator()

        tb.Realize()

    def on_click(self, event):
        event_id = event.GetId()
        if event_id == 201:
            self.text.SetLabel('点击「Back」按钮')
            print('点击「Back」按钮')
        else:
            self.text.SetLabel('点击「Forward」按钮')
            print('点击「Forward」按钮')

    def on_newitem_click(self, evnet):
        self.text.SetLabel('点击「新建」菜单')
        print('点击「新建」菜单')

    def on_editmenu_click(self, event):
        event_id = event.GetId()
        if event_id == 100 :
            self.text.SetLabel('点击「复制」菜单')
            print('点击「复制」菜单')
        elif event_id == 101:
            self.text.SetLabel('点击「剪切」菜单')
            print('点击「剪切」菜单')
        else:
            self.text.SetLabel('点击「粘贴」菜单')
            print('点击「粘贴」菜单')

class App(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()