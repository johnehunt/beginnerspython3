import wx


class HelloFrame(wx.Frame):

    def __init__(self, title):
        super(HelloFrame, self).__init__(None,
                                         title=title,
                                         size=(300, 200))

        self.name = '<unknown'

        # Create the BoxSizer to use for the Frame
        vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vertical_box_sizer)

        # Create the panel to contain the widgets
        panel = wx.Panel(self)
        # Add the Panel to the Frames Sizer
        vertical_box_sizer.Add(panel,
                               wx.ID_ANY,
                               wx.EXPAND | wx.ALL,
                               20)

        # Create the GridSizer to use with the Panel
        grid = wx.GridSizer(4, 1, 5, 5)

        # Set up the input field
        self.text = wx.TextCtrl(panel, size=(150, -1))

        # Now configure the enter button
        enter_button = wx.Button(panel, label='Enter')
        enter_button.Bind(wx.EVT_BUTTON, self.set_name)

        # Next set up the text label
        self.label = wx.StaticText(panel,
                                   label='Welcome',
                                   style=wx.ALIGN_LEFT)

        # Now configure the Show Message button
        message_button = wx.Button(panel, label='Show Message')
        message_button.Bind(wx.EVT_BUTTON, self.show_message)

        # Add all the widgets to the grid sizer to handle layout
        grid.AddMany([self.text, enter_button, self.label, message_button])

        # Set the sizer on the panel
        panel.SetSizer(grid)

        # Centre the Frame on the Computer Screen
        self.Centre()

    def show_message(self, event):
        """ Event Handler to display the Message Dialog
        using the current value of the name attribute. """
        dialog = wx.MessageDialog(None, 'Welcome To Python ' + self.name, 'Hello', wx.OK)
        dialog.ShowModal()

    def set_name(self, event):
        """ Event Handler for the Enter button.
            Retrieves the text entered into the input field
            and sets the self.name attribute. This is then
            used to set the text label """
        self.name = self.text.GetLineText(0)
        self.label.SetLabelText('Welcome ' + self.name)


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = HelloFrame(title='Sample App')
        frame.Show()
        # Indicate whether processing should continue or not
        return True

    def OnExit(self):
        """ Executes when the GUI application shuts down"""
        print('Goodbye')
        # Need to indicate success or failure
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
