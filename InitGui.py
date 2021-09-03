class Basic1Workbench (Workbench):
    """Basic 1 workbench object"""
    # this is the icon in XPM format 16x16 pixels
    Icon = """
   /* XPM */
    static char * basic1_xpm[] = {
    "16 16 2 1",
" 	c None",
".	c #000000",
"     ..  ..     ",
"     ..  ..     ",
"     ..  ..     ",
"     ..  ..     ",
"    .      .    ",
"    ........    ",
"    .      .    ",
"    .      .    ",
"    .      .    ",
"     .    .     ",
"      ....      ",
"       .        ",
"      .         ",
"     .          ",
"                ",
"                "};


    """

    MenuText = "Plug&Produce"
    ToolTip = "Plug&Produce workbench"

    def Initialize(self) :
        "This function is executed when FreeCAD starts"
        from PySide import QtCore, QtGui
        # python file where the commands are:
        import Basic1Gui
        # list of commands, only one (it is in the imported Basic1Gui):
        cmdlist = [ "Basic1_MakeBox","Basic2_MakeBoxDialog","ScrewCMD","HoleCMD","JsonCmd"]
        self.appendToolbar(
            str(QtCore.QT_TRANSLATE_NOOP("Plug&Produce", "Plug&Produce")), cmdlist)
        self.appendMenu(
            str(QtCore.QT_TRANSLATE_NOOP("Plug&Produce", "Plug&Produce")), cmdlist)

        Log ('Loading Basic1 module... done\n')

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# The workbench is added:
Gui.addWorkbench(Basic1Workbench())