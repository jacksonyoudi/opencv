#!/usr/bin/env python
# coding: utf8
# author: youdi

import wx


# app = wx.App()
# frame = wx.Frame(None, -1, u'GUI学习')
# frame.Show()
# app.MainLoop()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=-1, title=u'GUI学习', size=(600, 600))
        panel = wx.Panel(self, -1)
        self.Centre()

        button = wx.Button(panel, id=-1, label=u'这是按钮', pos=(50, 50))
        statictext = wx.StaticText(parent=panel, id=-1, label=u'这是静态文本框', pos=(20, 100))
        text = wx.TextCtrl(panel, -1, u'这是文本', pos=(200, 210))
        password = wx.TextCtrl(panel, -1, u'输入密码', style=wx.TE_PASSWORD, pos=(200, 250))
        mutiText = wx.TextCtrl(panel, -1, u'请输入多行内容', style=wx.TE_MULTILINE, pos=(100, 300))
        checkBox1 = wx.CheckBox(panel, -1, u'这是复选框1', pos=(150, 20))
        checkBox2 = wx.CheckBox(panel, -1, u'这是复选框1', pos=(150, 40))

        radio1 = wx.RadioButton(panel, -1, u'这是单选框1', pos=(150, 60), style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, u'这是单选框2', pos=(150, 60))
        radio3 = wx.RadioButton(panel, -1, u'这是单选框3', pos=(150, 60))

        radiolist = [u'一组单选按钮1', u'一组单选按钮2', u'一组单选按钮3']
        wx.RadioBox(panel, -1, u'一组单选按钮', (10, 120), wx.DefaultSize, radiolist, 2, wx.RA_SPECIFY_COLS)

        tuxinghua = [u'图', u'形', u'化', u'篇', '1', '2', '3', '4', '5', '6']
        listbox = wx.ListBox(panel, -1, pos=(300, 20), size=(100, 100), choices=tuxinghua, style=wx.LB_SINGLE)

        img = wx.Image(r'../img/5.jpg', wx.BITMAP_TYPE_ANY).Scale(200, 200)
        sb1 = wx.StaticBitmap(panel, -1, wx.BitmapFromImage(img), pos=(300, 300))

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
