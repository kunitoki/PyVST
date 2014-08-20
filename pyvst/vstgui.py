import threading

try:
    import PyQt4.QtCore as QtCore
    import PyQt4.QtGui as QtGui
    HAVE_PYQT = True
except ImportError:
    HAVE_PYQT = False

try:
    import wx
    HAVE_WX = True
except ImportError:
    HAVE_WX = False
    

#===============================================================================
if HAVE_PYQT:
    def raise_gui(plugin):
        class HostWindow(QtGui.QMainWindow):
            def __init__(self, app, plugin, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.app = app
                self.plugin = plugin
                QtCore.QMetaObject.connectSlotsByName(self)
            
        app = QtGui.QApplication([])
        frame = HostWindow(app, plugin)
        plugin.open_edit(frame.winId())
        rect = plugin.get_erect()
        frame.resize(rect.right, rect.bottom)
        frame.show()
        app.exec_()
        plugin.close_edit()

#===============================================================================
elif HAVE_WX:
    def raise_gui(plugin):
        class HostWindow(wx.Frame):
            def __init__(self, app, plugin):
                wx.Frame.__init__(self, None, -1, "Plugin editor")
                self.app = app
                self.plugin = plugin

        app = wx.App()
        frame = HostWindow(app, plugin)
        plugin.open_edit(frame.GetHandle())
        rect = plugin.get_erect()
        frame.SetClientSize((rect.right, rect.bottom))
        frame.Show()
        app.MainLoop()
        plugin.close_edit()

#===============================================================================
else:
    raise Exception("Must have at least wxPython or PyQT to use a vstgui")


#===============================================================================
class PluginWindowThread(threading.Thread):
    def __init__(self, plugin):
        threading.Thread.__init__(self)
        self.plugin = plugin

    def run(self):
        raise_gui(self.plugin)
