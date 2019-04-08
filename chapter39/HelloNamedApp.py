import wx


class HelloFrame(wx.Frame):

    def __init__(self, parent, title):
        super(HelloFrame, self).__init__(parent,
                                         title=title,
                                         size=(300, 200))

        self.name = '<unknown'

        vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vertical_box_sizer)

        panel = wx.Panel(self)
        grid = wx.GridSizer(4, 1, 5, 5)

        enter_button = wx.Button(panel, label='Enter')
        enter_button.Bind(wx.EVT_BUTTON, self.set_name)

        self.label = wx.StaticText(panel,
                                   label='Welcome',
                                   style=wx.ALIGN_LEFT)
        self.text = wx.TextCtrl(panel, size=(150, -1))

        message_button = wx.Button(panel, label='Show Message')
        message_button.Bind(wx.EVT_BUTTON, self.show_message)

        grid.AddMany([self.text, enter_button, self.label, message_button])
        panel.SetSizer(grid)
        vertical_box_sizer.Add(panel,
                               wx.ID_ANY,
                               wx.EXPAND | wx.ALL,
                               20)

        self.Centre()

    def on_quit(self, e):
        self.Close()

    def show_message(self, event):
        dialog = wx.MessageDialog(None, 'Welcome To Python ' + self.name, 'Hello', wx.OK)
        dialog.ShowModal()

    def set_name(self, event):
        self.name = self.text.GetLineText(0)
        self.label.SetLabelText('Welcome ' + self.name)


def main():
    app = wx.App()
    ex = HelloFrame(None, title='Sample App')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
