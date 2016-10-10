#!/usr/bin/env python
# coding: utf8
# author: youdi



###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class XbFrame1
###########################################################################

class XbFrame1(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"我的窗口", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"友弟", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(15, 75, 90, 90, False, "黑体"))
        self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    app = wx.App()
    f1 = XbFrame1(None)
    f1.Show()
    app.MainLoop()
