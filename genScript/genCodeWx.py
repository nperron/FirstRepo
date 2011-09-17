#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import genCode as generator

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.lbPrefix = wx.StaticText(self,-1, "Préfixe :")
        self.tbPrefix = wx.TextCtrl(self, -1, "")
        self.lbNbCode = wx.StaticText(self, -1, "Nombre de codes :")
        self.tbNbCode = wx.TextCtrl(self, -1, "")
        self.lbNbChar = wx.StaticText(self, -1, "Nombre de caractères :")
        self.cbNbChar = wx.ComboBox(
                                self,
                                -1,
                                choices=["4", "5", "6", "7", "8", "9", "10", "11", "12"],
                                style=wx.CB_DROPDOWN|wx.CB_READONLY
                                )
        self.btSend = wx.Button(self, -1, "Generer")
        self.lbCodes = wx.ListBox(
                                self,
                                -1,
                                choices=[],
                                style=wx.LB_MULTIPLE|wx.LB_EXTENDED
                                )
        #Events
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.btSend.Bind(wx.EVT_BUTTON, self.OnClick)
        
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Code Generator")
        self.cbNbChar.SetMinSize((60, 29))
        self.cbNbChar.SetSelection(0)
        self.lbCodes.SetMinSize((250, 400))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(3, 2, 0, 0)
        grid_sizer_1.Add(self.lbPrefix, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.tbPrefix, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.lbNbCode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.tbNbCode, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.lbNbChar, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.cbNbChar, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        sizer_1.Add(grid_sizer_1, 1, wx.ALL|wx.EXPAND, 1)        
        sizer_1.Add(self.btSend, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.lbCodes, 0, wx.ALL|wx.EXPAND, 1)

        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade
        
    def OnClose(self, event):
        dlg = wx.MessageDialog(self, 
            "Voulez vous vraiment quitter ?",
            "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()
    
    def OnClick(self, event):
        import pdb;pdb.set_trace()
        gen = generator.genCode(
                            self.tbNbCode.GetValue(),
                            self.cbNbChar.GetValue(),
                            self.tbPrefix.GetValue()
                            )
        result = sorted(gen.main())
        result2 = sorted(list(set(result)))
        print "%d codes generated" % len(result2)
        self.lbCodes.InsertItems(result2, 0)
        


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    mainFrame = MyFrame(None, -1, "")
    app.SetTopWindow(mainFrame)
    mainFrame.Show()
    app.MainLoop()
