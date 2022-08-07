import wx
import wx.xrc
import wx.aui
import wx.stc
import wx.propgrid as pg
import wx.py as py

###########################################################################
## Class wxStudio-Main
###########################################################################

class wxStudio-Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxStudio - ", pos = wx.DefaultPosition, size = wx.Size( 921,689 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.FRAME_SHAPED|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL, name = u"wxstudiomain" )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( wx.MB_DOCKABLE )
		self.m_FileMenu = wx.Menu()
		self.m_NewProjecItem = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"New Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_FileMenu.Append( self.m_NewProjecItem )

		self.m_NewMenu = wx.Menu()
		self.m_NewFrameMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Frame", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewFrameMenuItem )

		self.m_NewDialogMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Dialog", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewDialogMenuItem )

		self.m_NewPamelMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Panel", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewPamelMenuItem )

		self.m_NewMenu.AppendSeparator()

		self.m_NewConsoleAppMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Console Application", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewConsoleAppMenuItem )

		self.m_NewModuleMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Module", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewModuleMenuItem )

		self.m_NewRCMenuItem = wx.MenuItem( self.m_NewMenu, wx.ID_ANY, u"New Resource File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_NewMenu.Append( self.m_NewRCMenuItem )

		self.m_FileMenu.AppendSubMenu( self.m_NewMenu, u"&New" )

		self.m_OpenFIle = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"Open File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_OpenFIle.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_MENU ) )
		self.m_FileMenu.Append( self.m_OpenFIle )

		self.m_Save = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Save.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
		self.m_FileMenu.Append( self.m_Save )

		self.m_SaveAs = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"Save As", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_SaveAs.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE_AS, wx.ART_MENU ) )
		self.m_FileMenu.Append( self.m_SaveAs )

		self.m_Close = wx.Menu()
		self.m_FileMenu.AppendSubMenu( self.m_Close, u"Close" )

		self.m_Import = wx.Menu()
		self.m_FileMenu.AppendSubMenu( self.m_Import, u"Import" )

		self.m_Export = wx.Menu()
		self.m_FileMenu.AppendSubMenu( self.m_Export, u"Export" )

		self.m_ExitSave = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"Exit && Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_ExitSave.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
		self.m_FileMenu.Append( self.m_ExitSave )

		self.m_Exit = wx.MenuItem( self.m_FileMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Exit.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
		self.m_FileMenu.Append( self.m_Exit )

		self.m_menubar1.Append( self.m_FileMenu, u"&File" )

		self.m_EditMenu = wx.Menu()
		self.m_Undo = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Undo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Undo.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_UNDO, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Undo )

		self.m_Redo = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Redo", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Redo.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REDO, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Redo )

		self.m_EditMenu.AppendSeparator()

		self.m_Find = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Find", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Find.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FIND, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Find )

		self.m_EditMenu.AppendSeparator()

		self.m_Copy = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Copy", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Copy.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_COPY, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Copy )

		self.m_Cut = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Cut", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Cut.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_CUT, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Cut )

		self.m_Paste = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Paste", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Paste.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PASTE, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Paste )

		self.m_Delete = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_Delete.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_DELETE, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_Delete )

		self.m_EditMenu.AppendSeparator()

		self.m_CopyObject = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Copy Object to Clipboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_CopyObject.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_COPY, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_CopyObject )

		self.m_PasteObject = wx.MenuItem( self.m_EditMenu, wx.ID_ANY, u"Paste Object From Clipboard", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_PasteObject.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PASTE, wx.ART_MENU ) )
		self.m_EditMenu.Append( self.m_PasteObject )

		self.m_menubar1.Append( self.m_EditMenu, u"&Edit" )

		self.m_ViewMenu = wx.Menu()
		self.m_WidgetsToolVisable = wx.MenuItem( self.m_ViewMenu, wx.ID_ANY, u"Widgets Tool Bar", wx.EmptyString, wx.ITEM_CHECK )
		self.m_ViewMenu.Append( self.m_WidgetsToolVisable )
		self.m_WidgetsToolVisable.Check( True )

		self.m_ObjectInspectorVisable = wx.MenuItem( self.m_ViewMenu, wx.ID_ANY, u"Object Inspector", wx.EmptyString, wx.ITEM_CHECK )
		self.m_ViewMenu.Append( self.m_ObjectInspectorVisable )
		self.m_ObjectInspectorVisable.Check( True )

		self.m_PropertiesEventsVisable = wx.MenuItem( self.m_ViewMenu, wx.ID_ANY, u"Properties/Events Editor", wx.EmptyString, wx.ITEM_CHECK )
		self.m_ViewMenu.Append( self.m_PropertiesEventsVisable )
		self.m_PropertiesEventsVisable.Check( True )

		self.m_ProjectInformation = wx.MenuItem( self.m_ViewMenu, wx.ID_ANY, u"Project Information", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_ProjectInformation.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_REPORT_VIEW, wx.ART_MENU ) )
		self.m_ViewMenu.Append( self.m_ProjectInformation )

		self.m_PreferencesSettings = wx.MenuItem( self.m_ViewMenu, wx.ID_ANY, u"Preferences & Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_PreferencesSettings.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_MENU ) )
		self.m_ViewMenu.Append( self.m_PreferencesSettings )

		self.m_menubar1.Append( self.m_ViewMenu, u"V&iew" )

		self.m_ToolsMenu = wx.Menu()
		self.m_menubar1.Append( self.m_ToolsMenu, u"&Tools" )

		self.m_DesignMenu = wx.Menu()
		self.m_FormsSubMenu = wx.Menu()
		self.m_DesignMenu.AppendSubMenu( self.m_FormsSubMenu, u"Forms" )

		self.m_SizersSubMenu = wx.Menu()
		self.m_DesignMenu.AppendSubMenu( self.m_SizersSubMenu, u"Sizers" )

		self.m_menubar1.Append( self.m_DesignMenu, u"Design" )

		self.m_ProjectMenu = wx.Menu()
		self.m_menubar1.Append( self.m_ProjectMenu, u"Project" )

		self.m_HelpMenu = wx.Menu()
		self.m_ReadHelpFile = wx.MenuItem( self.m_HelpMenu, wx.ID_ANY, u"Read Help File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_ReadHelpFile.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP, wx.ART_MENU ) )
		self.m_HelpMenu.Append( self.m_ReadHelpFile )

		self.m_AboutBox = wx.MenuItem( self.m_HelpMenu, wx.ID_ANY, u"About wxStudio...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_AboutBox.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK, wx.ART_MENU ) )
		self.m_HelpMenu.Append( self.m_AboutBox )

		self.m_menubar1.Append( self.m_HelpMenu, u"&Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.tb_FileOperationsToolBar = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_GRIPPER|wx.aui.AUI_TB_HORZ_LAYOUT )
		self.tb_FileOperationsToolBar.Realize()
		self.m_mgr.AddPane( self.tb_FileOperationsToolBar, wx.aui.AuiPaneInfo().Name( u"aui_FileOperationsToolBar" ).Top().CaptionVisible( False ).CloseButton( False ).PinButton( True ).Gripper().Dock().Fixed().DockFixed( True ).BottomDockable( False ).LeftDockable( False ).RightDockable( False ).Floatable( False ).CentrePane().ToolbarPane() )

		self.g_WidgetsBook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_RIGHT )
		self.m_mgr.AddPane( self.g_WidgetsBook, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).BestSize( wx.Size( 150,-1 ) ) )

		self.t_Common = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Common, u"Common", False )
		self.t_Additional = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Additional, u"Additional", False )
		self.t_Data = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Data, u"Data", False )
		self.t_Containers = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Containers, u"Containers", False )
		self.t_MenuToolBar = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_MenuToolBar, u"Menu/Toolbar", False )
		self.t_Layout = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Layout, u"Layout", False )
		self.t_Forms = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Forms, u"Forms", False )
		self.t_Ribbon = wx.Panel( self.g_WidgetsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_WidgetsBook.AddPage( self.t_Ribbon, u"Ribbon", False )

		self.g_EditorBook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_TOP|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		self.m_mgr.AddPane( self.g_EditorBook, wx.aui.AuiPaneInfo() .Name( u"AUI_EditWindow" ).Center() .Caption( u"Editor" ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( -1,-1 ) ).DockFixed( True ).Floatable( False ).CentrePane().DefaultPane() )

		self.p_UIDesigner = wx.Panel( self.g_EditorBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_UIDesignerSizer = wx.BoxSizer( wx.VERTICAL )


		self.p_UIDesigner.SetSizer( s_UIDesignerSizer )
		self.p_UIDesigner.Layout()
		s_UIDesignerSizer.Fit( self.p_UIDesigner )
		self.g_EditorBook.AddPage( self.p_UIDesigner, u"Form Designer", True, wx.NullBitmap )
		self.p_SourceEditor = wx.Panel( self.g_EditorBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_SourceEditorSizer = wx.GridBagSizer( 0, 0 )
		s_SourceEditorSizer.SetFlexibleDirection( wx.BOTH )
		s_SourceEditorSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.p_SourceNavigation = wx.Panel( self.p_SourceEditor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.p_SourceNavigation.SetMinSize( wx.Size( -1,20 ) )

		s_SourceEditorSizer.Add( self.p_SourceNavigation, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.w_SourceCodeEditor = wx.stc.StyledTextCtrl( self.p_SourceEditor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.w_SourceCodeEditor.SetUseTabs ( True )
		self.w_SourceCodeEditor.SetTabWidth ( 4 )
		self.w_SourceCodeEditor.SetIndent ( 4 )
		self.w_SourceCodeEditor.SetTabIndents( True )
		self.w_SourceCodeEditor.SetBackSpaceUnIndents( True )
		self.w_SourceCodeEditor.SetViewEOL( False )
		self.w_SourceCodeEditor.SetViewWhiteSpace( False )
		self.w_SourceCodeEditor.SetMarginWidth( 2, 0 )
		self.w_SourceCodeEditor.SetIndentationGuides( True )
		self.w_SourceCodeEditor.SetReadOnly( False );
		self.w_SourceCodeEditor.SetMarginType ( 1, wx.stc.STC_MARGIN_SYMBOL )
		self.w_SourceCodeEditor.SetMarginMask ( 1, wx.stc.STC_MASK_FOLDERS )
		self.w_SourceCodeEditor.SetMarginWidth ( 1, 16)
		self.w_SourceCodeEditor.SetMarginSensitive( 1, True )
		self.w_SourceCodeEditor.SetProperty ( "fold", "1" )
		self.w_SourceCodeEditor.SetFoldFlags ( wx.stc.STC_FOLDFLAG_LINEBEFORE_CONTRACTED | wx.stc.STC_FOLDFLAG_LINEAFTER_CONTRACTED );
		self.w_SourceCodeEditor.SetMarginType( 0, wx.stc.STC_MARGIN_NUMBER );
		self.w_SourceCodeEditor.SetMarginWidth( 0, self.w_SourceCodeEditor.TextWidth( wx.stc.STC_STYLE_LINENUMBER, "_99999" ) )
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
		self.w_SourceCodeEditor.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
		self.w_SourceCodeEditor.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
		self.w_SourceCodeEditor.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
		self.w_SourceCodeEditor.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
		self.w_SourceCodeEditor.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
		self.w_SourceCodeEditor.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
		self.w_SourceCodeEditor.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
		self.w_SourceCodeEditor.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
		self.w_SourceCodeEditor.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
		self.w_SourceCodeEditor.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		self.w_SourceCodeEditor.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.w_SourceCodeEditor.SetMinSize( wx.Size( 668,655 ) )

		s_SourceEditorSizer.Add( self.w_SourceCodeEditor, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		self.p_SourceEditor.SetSizer( s_SourceEditorSizer )
		self.p_SourceEditor.Layout()
		s_SourceEditorSizer.Fit( self.p_SourceEditor )
		self.g_EditorBook.AddPage( self.p_SourceEditor, u"Source Code", False, wx.NullBitmap )

		self.g_ObjectBook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.g_ObjectBook, wx.aui.AuiPaneInfo() .Name( u"AUI_ObjectList" ).Right() .Caption( u"Object Inspector" ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 200,-1 ) ).BottomDockable( False ).BestSize( wx.Size( 250,-1 ) ).MaxSize( wx.Size( 200,-1 ) ) )

		self.p_ObjectTree = wx.Panel( self.g_ObjectBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.g_ObjectBook.AddPage( self.p_ObjectTree, u"Object Tree", False, wx.NullBitmap )
		self.p_ProjectFilesTree = wx.Panel( self.g_ObjectBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_ProjectFilesTabSizer = wx.GridBagSizer( 0, 0 )
		s_ProjectFilesTabSizer.SetFlexibleDirection( wx.BOTH )
		s_ProjectFilesTabSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_ProjectFilesTree = wx.TreeCtrl( self.p_ProjectFilesTree, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225,300 ), wx.TR_DEFAULT_STYLE )
		s_ProjectFilesTabSizer.Add( self.w_ProjectFilesTree, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.p_ProjectFilesTree.SetSizer( s_ProjectFilesTabSizer )
		self.p_ProjectFilesTree.Layout()
		s_ProjectFilesTabSizer.Fit( self.p_ProjectFilesTree )
		self.g_ObjectBook.AddPage( self.p_ProjectFilesTree, u"Project Files", True, wx.NullBitmap )
		self.p_ClassesTree = wx.Panel( self.g_ObjectBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_ClassesTabSizer = wx.GridBagSizer( 0, 0 )
		s_ClassesTabSizer.SetFlexibleDirection( wx.BOTH )
		s_ClassesTabSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_ClassesTree = wx.TreeCtrl( self.p_ClassesTree, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225,300 ), wx.TR_DEFAULT_STYLE )
		s_ClassesTabSizer.Add( self.w_ClassesTree, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.p_ClassesTree.SetSizer( s_ClassesTabSizer )
		self.p_ClassesTree.Layout()
		s_ClassesTabSizer.Fit( self.p_ClassesTree )
		self.g_ObjectBook.AddPage( self.p_ClassesTree, u"Classes", False, wx.NullBitmap )
		self.p_ResourcesTree = wx.Panel( self.g_ObjectBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_ResourcesSizer = wx.GridBagSizer( 0, 0 )
		s_ResourcesSizer.SetFlexibleDirection( wx.BOTH )
		s_ResourcesSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_ResourcesTree = wx.TreeCtrl( self.p_ResourcesTree, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225,300 ), wx.TR_DEFAULT_STYLE )
		s_ResourcesSizer.Add( self.w_ResourcesTree, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.p_ResourcesTree.SetSizer( s_ResourcesSizer )
		self.p_ResourcesTree.Layout()
		s_ResourcesSizer.Fit( self.p_ResourcesTree )
		self.g_ObjectBook.AddPage( self.p_ResourcesTree, u"Resources", False, wx.NullBitmap )

		self.g_PropertiesList = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.g_PropertiesList, wx.aui.AuiPaneInfo() .Name( u"AUI_PROPEVENT" ).Right() .Caption( u"Properties/Events" ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 250,-1 ) ).BestSize( wx.Size( 250,-1 ) ).MinSize( wx.Size( 250,-1 ) ).MaxSize( wx.Size( 250,-1 ) ) )

		self.p_PropertiesDataGrid = wx.Panel( self.g_PropertiesList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		s_PropertiesSizer = wx.GridBagSizer( 0, 0 )
		s_PropertiesSizer.SetFlexibleDirection( wx.BOTH )
		s_PropertiesSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_PropertiesGrid = pg.PropertyGrid(self.p_PropertiesDataGrid, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,300 ), wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.TAB_TRAVERSAL)
		s_PropertiesSizer.Add( self.w_PropertiesGrid, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		self.p_PropertiesDataGrid.SetSizer( s_PropertiesSizer )
		self.p_PropertiesDataGrid.Layout()
		s_PropertiesSizer.Fit( self.p_PropertiesDataGrid )
		self.g_PropertiesList.AddPage( self.p_PropertiesDataGrid, u"Properties", False, wx.NullBitmap )
		self. = wx.Panel( self.g_PropertiesList, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_propertyGridManager2 = pg.PropertyGridManager(self., wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PGMAN_DEFAULT_STYLE)
		self.m_propertyGridManager2.SetExtraStyle( wx.propgrid.PG_EX_MODE_BUTTONS )

		self.m_propertyGridPage1 = self.m_propertyGridManager2.AddPage( u"Page", wx.NullBitmap );
		self.m_propertyGridItem5 = self.m_propertyGridPage1.Append( pg.EnumProperty( u"Name", u"Name" ) )
		gbSizer2.Add( self.m_propertyGridManager2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		gbSizer2.AddGrowableCol( 0 )
		gbSizer2.AddGrowableRow( 0 )

		self..SetSizer( gbSizer2 )
		self..Layout()
		gbSizer2.Fit( self. )
		self.g_PropertiesList.AddPage( self., u"Events", True, wx.NullBitmap )

		self.p_Console = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.p_Console, wx.aui.AuiPaneInfo() .Name( u"AUI_Console" ).Bottom() .Caption( u"Console" ).PinButton( True ).Hide().Dock().Resizable().FloatingSize( wx.DefaultSize ).LeftDockable( False ).RightDockable( False ).BestSize( wx.Size( -1,300 ) ) )

		s_ConsoleSizer = wx.BoxSizer( wx.VERTICAL )

		p_PyShell = wx.py.shell.Shell(self.m_Console,  introtext = intro)
		s_ConsoleSizer.Add( self.w_Console, 0, wx.ALL, 5 )


		self.p_Console.SetSizer( s_ConsoleSizer )
		self.p_Console.Layout()
		s_ConsoleSizer.Fit( self.p_Console )
		self.p_Inspector = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.p_Inspector, wx.aui.AuiPaneInfo() .Name( u"AUI_Inspector" ).Bottom() .Caption( u"Inspector" ).PinButton( True ).Hide().Dock().Resizable().FloatingSize( wx.DefaultSize ).LeftDockable( False ).RightDockable( False ).Row( 1 ).Position( 0 ).BestSize( wx.Size( -1,300 ) ) )

		s_InspectorSizer = wx.BoxSizer( wx.VERTICAL )


		p_Filling = wx.py.filling.FillingTree(self.m_Inspector, -1)
		s_InspectorSizer.Add( self.w_Inspector, 0, wx.ALL, 5 )


		self.p_Inspector.SetSizer( s_InspectorSizer )
		self.p_Inspector.Layout()
		s_InspectorSizer.Fit( self.p_Inspector )

		self.m_mgr.Update()
		self.Centre( wx.BOTH )

	def __del__( self ):
		self.m_mgr.UnInit()



