import wx
import wx.xrc
import wx.adv

###########################################################################
## Class d_NewProjectWiz
###########################################################################

class d_NewProjectWiz ( wx.adv.Wizard ):

	def __init__( self, parent ):
		wx.adv.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Project Wizard", bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE|wx.DIALOG_NO_PARENT )

		self.SetExtraStyle( wx.adv.WIZARD_EX_HELPBUTTON )
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []

		self.d_NewProjectWizPg1 = wx.adv.WizardPageSimple( self  )
		self.add_page( self.d_NewProjectWizPg1 )

		s_NewProjectWizPg1Sizer = wx.GridBagSizer( 0, 0 )
		s_NewProjectWizPg1Sizer.SetFlexibleDirection( wx.BOTH )
		s_NewProjectWizPg1Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_Bitmap1 = wx.StaticBitmap( self.d_NewProjectWizPg1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		s_NewProjectWizPg1Sizer.Add( self.w_Bitmap1, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 1 ), wx.ALL, 5 )


		s_NewProjectWizPg1Sizer.Add( ( 275, 0 ), wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		self.w_IntroText = wx.StaticText( self.d_NewProjectWizPg1, wx.ID_ANY, u"Welcome to the New Project Wizard. \nThis tool will guide you through the process of setting up all of the necessary details \nfor your project.\n\nIf you don't understand any of the fields you can click the \"Help\" \nbutton for an explanation. You can change any of your projects configuration settings\n through the \"Project\" menu under \"Project Configuration\".", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_IntroText.Wrap( -1 )

		s_NewProjectWizPg1Sizer.Add( self.w_IntroText, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_ProjectNameLabel = wx.StaticText( self.d_NewProjectWizPg1, wx.ID_ANY, u"Project Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_ProjectNameLabel.Wrap( -1 )

		self.w_ProjectNameLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		s_NewProjectWizPg1Sizer.Add( self.w_ProjectNameLabel, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_ProjectNameEdit = wx.TextCtrl( self.d_NewProjectWizPg1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_ProjectNameEdit.SetMinSize( wx.Size( 300,-1 ) )

		s_NewProjectWizPg1Sizer.Add( self.w_ProjectNameEdit, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.w_ProjectPathLabel = wx.StaticText( self.d_NewProjectWizPg1, wx.ID_ANY, u"Project Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_ProjectPathLabel.Wrap( -1 )

		self.w_ProjectPathLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		s_NewProjectWizPg1Sizer.Add( self.w_ProjectPathLabel, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_ProjectPathEdit = wx.TextCtrl( self.d_NewProjectWizPg1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_ProjectPathEdit.SetMinSize( wx.Size( 475,-1 ) )

		s_NewProjectWizPg1Sizer.Add( self.w_ProjectPathEdit, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.w_DirSelectButton = wx.Button( self.d_NewProjectWizPg1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_DirSelectButton.SetMinSize( wx.Size( 40,-1 ) )

		s_NewProjectWizPg1Sizer.Add( self.w_DirSelectButton, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_HeaderTextLabel = wx.StaticText( self.d_NewProjectWizPg1, wx.ID_ANY, u"New Project Wizard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.w_HeaderTextLabel.Wrap( -1 )

		self.w_HeaderTextLabel.SetFont( wx.Font( 30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		s_NewProjectWizPg1Sizer.Add( self.w_HeaderTextLabel, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.d_NewProjectWizPg1.SetSizer( s_NewProjectWizPg1Sizer )
		self.d_NewProjectWizPg1.Layout()
		s_NewProjectWizPg1Sizer.Fit( self.d_NewProjectWizPg1 )
		self.Centre( wx.BOTH )

	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)

	def __del__( self ):
		pass


###########################################################################
## Class d_NewProjWizHelp
###########################################################################

class d_NewProjWizHelp ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"New Project Wizard Help", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class d_UnsavedChangesDlg
###########################################################################

class d_UnsavedChangesDlg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Unsaved Changes", pos = wx.DefaultPosition, size = wx.Size( 646,220 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		s_UnsavedChangesSizer = wx.GridBagSizer( 0, 0 )
		s_UnsavedChangesSizer.SetFlexibleDirection( wx.BOTH )
		s_UnsavedChangesSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_CancelButton = wx.Button( self, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_UnsavedChangesSizer.Add( self.w_CancelButton, wx.GBPosition( 7, 45 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_OkButton = wx.Button( self, wx.ID_ANY, u"&Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_UnsavedChangesSizer.Add( self.w_OkButton, wx.GBPosition( 7, 46 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.w_StaticText1 = wx.StaticText( self, wx.ID_ANY, u"You have unsaved changes in your project.\nWould you like to save now?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.w_StaticText1.Wrap( -1 )

		self.w_StaticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		s_UnsavedChangesSizer.Add( self.w_StaticText1, wx.GBPosition( 3, 15 ), wx.GBSpan( 2, 40 ), wx.ALL, 5 )


		self.SetSizer( s_UnsavedChangesSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class d_StartNewDialog
###########################################################################

class d_StartNewDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Start New...", pos = wx.DefaultPosition, size = wx.Size( 701,506 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		s_StartNewSizer = wx.GridBagSizer( 0, 0 )
		s_StartNewSizer.SetFlexibleDirection( wx.BOTH )
		s_StartNewSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.w_CancelButton = wx.Button( self, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_StartNewSizer.Add( self.w_CancelButton, wx.GBPosition( 21, 50 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.TEMPORARYSPACEHOLDER = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 660,400 ), 0 )
		s_StartNewSizer.Add( self.TEMPORARYSPACEHOLDER, wx.GBPosition( 1, 1 ), wx.GBSpan( 20, 70 ), wx.ALL, 5 )

		self.w_OkButton = wx.Button( self, wx.ID_ANY, u"&Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		s_StartNewSizer.Add( self.w_OkButton, wx.GBPosition( 21, 52 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( s_StartNewSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


