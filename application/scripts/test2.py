
###############################################################################
## Script description
## By: your name here

import pn
import scintilla
from pypn.decorators import script

@script("Test2 Script", "Test Scripts")
def SayHello():
	""" Say Hello """
	newDoc = pn.NewDocument(None)
	editor = scintilla.Scintilla(newDoc)
	message = "Hello world!"
	editor.BeginUndoAction()
	editor.AppendText(len(message), message)
	editor.EndUndoAction()
	pass


