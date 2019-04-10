import wx

class WelcomeFrame(wx.Frame):
    """ The Main Window / Frame fo the application """
    def __init__(self, *args, **kw):
        super(WelcomeFrame, self).__init__(*args, **kw)

        # Set up panel within the frame and text label
        self.panel = wx.Panel(self)
        self.text = wx.StaticText(self.panel, label='Hello')

        # Bind the on_mouse_click method to the Mouse Event via the
        # left mouse click binder
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)

    def on_mouse_click(self, mouse_event):
        """ When the left mouse button is clicked this
            method is called. It will obtain the current
            mouse coordinates, and reposition the text label
            to this position. """
        x, y = mouse_event.GetPosition()
        print(x, y)
        self.text.SetPosition(wx.Point(x, y))


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the main GUI Application"""
        frame = WelcomeFrame(None, title='Sample App')
        frame.Show()
        # Indicate whether processing should continue or not
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
