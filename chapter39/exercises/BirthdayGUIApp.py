import wx


class BirthdayFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None,
                         title='Happy Birthday App',
                         size=(300, 200))

        self.name = '<unknown'
        self.age = -1

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
        grid = wx.GridSizer(5, 1, 5, 5)

        # Create a Panel to hold the name label and input field widgets
        name_panel = wx.Panel(panel)
        horizontal_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        name_panel.SetSizer(horizontal_box_sizer)
        horizontal_box_sizer.Add(wx.StaticText(name_panel, label='Name: '))
        self.name_texttrl = wx.TextCtrl(name_panel, size=(150, -1))
        horizontal_box_sizer.Add(self.name_texttrl)

        # Create a panel for the age label and input field
        age_panel = wx.Panel(panel)
        horizontal_box_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        age_panel.SetSizer(horizontal_box_sizer2)
        horizontal_box_sizer2.Add(wx.StaticText(age_panel, label='Age: '))
        self.age_textctrl = wx.TextCtrl(age_panel, size=(150, -1))
        horizontal_box_sizer2.Add(self.age_textctrl)

        # Now configure the enter button
        enter_button = wx.Button(panel, label='Enter')
        enter_button.Bind(wx.EVT_BUTTON, self.set_name_and_age)

        # Next set up the text label
        self.label = wx.StaticText(panel,
                                   label='Welcome',
                                   style=wx.ALIGN_LEFT)

        # Now configure the Show Message button
        message_button = wx.Button(panel, label='Birthday')
        message_button.Bind(wx.EVT_BUTTON, self.show_birthday_message)

        # Add all the widgets to the grid sizer to handle layout
        grid.AddMany([name_panel, age_panel, enter_button, self.label, message_button])

        # Set the sizer on the panel
        panel.SetSizer(grid)

        # Centre the Frame on the Computer Screen
        self.Centre()

    def show_birthday_message(self, event):
        """ Event Handler for the birthdya button.
         Increments the age bt 1 and updates the age field.
         Then displays a birthday message. """
        self.age = self.age + 1
        self.age_textctrl.SetLabel(str(self.age))
        dialog = wx.MessageDialog(None,
                                  'Happy Birthday ' +
                                  self.name +
                                  ' you are now ' +
                                  str(self.age),
                                  'Birthday',
                                  wx.OK)
        dialog.ShowModal()

    def set_name_and_age(self, event):
        """ Event Handler for the Enter button.
            Retrieves the text entered into the name and age text control fields
            and sets the self.name attribute. It checks that the age is a number
            and uses that or displays a warning message. """
        self.name = self.name_texttrl.GetLineText(0)
        self.label.SetLabelText('Welcome ' + self.name)
        age_string = self.age_textctrl.GetLineText(0)
        if age_string.isnumeric():
            self.age = int(age_string)
        else:
            dialog = wx.MessageDialog(None, 'Age Must be an Integer', 'Error', wx.OK | wx.ICON_INFORMATION)
            dialog.ShowModal()


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the GUI display"""
        frame = BirthdayFrame()
        frame.Show()
        # Indicate whether processing should continue or not
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
