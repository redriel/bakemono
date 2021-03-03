import wx
from lib import archive, npc

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Bakemono')
        self.my_archive = archive.Archive()
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_RICH|wx.TE_READONLY)
        my_sizer.Add(self.text_ctrl, 20, wx.ALL | wx.EXPAND, 25)
        my_btn = wx.Button(panel, label='Generate NPC')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        #self.cb1 = wx.CheckBox(panel, label = 'test') 
        #my_sizer.Add(self.cb1, 0, wx.ALL | wx.CENTER, 15)
        races = self.my_archive.races
        self.choice = wx.Choice(panel,choices = races)
        my_sizer.Add(self.choice, 0, wx.ALL | wx.CENTER, 15)
        lblList = ['Male', 'Female']     
        self.rbox = wx.RadioBox(panel,label = 'Gender', choices = lblList ,majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        my_sizer.Add(self.rbox, 0, wx.ALL | wx.CENTER, 15)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        self.npc = npc.NPC()
        #name = self.my_archive.shuffle(self.my_archive.names)
        if len(self.choice.GetString(self.choice.GetSelection())) > 0:
            self.npc.race = self.choice.GetString(self.choice.GetSelection()).strip()
        self.text_ctrl.SetValue(self.npc.stringify())
        print(self.npc.stringify())



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
