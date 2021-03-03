import wx
from lib import archive, npc

class BakemonoFrame(wx.Frame):
    def __init__(self):
        # Setting the main frame and data lists
        style = ( wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.BORDER_THEME)
        super().__init__(parent = None, title = "Bakemono", style = style)
        inst_archive = archive.Archive()
        races = inst_archive.races
        races.insert(0, "Random race")
        genderList = ["Random", "Male", "Female"]
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        x_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Setting frame widgets
        self.textbox = wx.TextCtrl(panel, style = wx.TE_MULTILINE | wx.TE_RICH | wx.TE_READONLY)
        self.font = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.textbox.SetFont(self.font)
        self.generate_btn = wx.Button(panel, label = "Generate NPC")
        self.generate_btn.Bind(wx.EVT_BUTTON, self.on_press)
        self.select_races = wx.Choice(panel, choices = races)
        self.select_races.SetSelection(0)
        self.genderBox = wx.RadioBox(panel, label = "Gender", choices = genderList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        
        # Setting widgets position inside the frame
        x_sizer.Add(self.select_races, 5,  wx.ALL | wx.LEFT | wx.ALIGN_CENTER, 5)
        x_sizer.Add(self.genderBox, 5,  wx.ALL | wx.RIGHT | wx.ALIGN_CENTER,5)
        sizer.Add(x_sizer, 0, wx.ALL |wx.LEFT|wx.RIGHT|wx.TOP, 0)
        sizer.Add(self.textbox, 15, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.generate_btn, 5, wx.ALL | wx.CENTER, 5)
        
        # Displaying the frame and the widgets
        panel.SetSizer(sizer)
        self.SetSize(wx.Size(400, 375))
        self.Centre()
        self.SetTransparent(240)
        self.Show()

    def on_press(self, event):
        self.npc = npc.NPC()
        if self.select_races.GetSelection() > 0:
            self.npc.race = self.select_races.GetString(self.select_races.GetSelection()).strip()
        self.textbox.SetValue(self.npc.stringify())
        print(self.npc.stringify())

if __name__ == '__main__':
    app = wx.App()
    frame = BakemonoFrame()
    app.MainLoop()
