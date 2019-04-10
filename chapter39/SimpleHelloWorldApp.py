import wx

# Create the Application Object
app = wx.App()

# Now create a Frame (representing the window)
frame = wx.Frame(None, title="Simple Hello World")
# And add a text label to it
text = wx.StaticText(frame, label='Hello Python')

# Display the window (frame)
frame.Show()

# Start the event loop
app.MainLoop()