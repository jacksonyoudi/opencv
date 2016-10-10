#!/usr/bin/env python
# coding: utf8
# author: youdi


import wx
from math import *


class CalcFrame(wx.Frame):
    def __init__(self, title):
        super(CalcFrame, self).__init__(self, None, -1, title, size=())
