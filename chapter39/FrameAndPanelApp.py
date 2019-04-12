import wx


class SampleFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None,
                         title='Sample App',
                         size=(300, 300))

        # Set up the first Panel to be at position 1, 1
        # and of size 300 by 100 with a blue background
        self.panel1 = wx.Panel(self)
        self.panel1.SetSize(300, 100)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 255))

        # Set up the second Panel to be at position 1, 110
        # and of size 300 by 100 with a red background
        self.panel2 = wx.Panel(self)
        self.panel2.SetSize(1, 110, 300, 100)
        self.panel2.SetBackgroundColour(wx.Colour(255, 0, 0))


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the main GUI Application"""
        frame = SampleFrame()
        frame.Show()
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
