#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import wx

class Produit:
	def __init__(self, nom,num_id, prix):
		self.nom=nom
		self.num_id=num_id
		self.prix=prix

Produits_liste=[Produit("Balle",1,3),
	Produit("Nounours",2,10),
	Produit("Livre",3,21),
	Produit("Puzzle",4,12),
	]
	
	
	
class myForm(wx.Frame):
	
	
	def __init__(self, parent, title):
		self.addition=[]
		super(myForm, self).__init__(parent,title=title, size=(150, 200))
		
		
		#wxFlexGridSizer (int rows, int cols, int vgap(px), int hgap(px))
		tableau = wx.FlexGridSizer(4, 1, 9, 25)
		panel = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		title = wx.StaticText(panel, label="Produit")
		self.Combo = wx.ComboBox(panel,
			size=wx.DefaultSize)
		for i in range(len(Produits_liste)):
			self.Combo.Append(Produits_liste[i].nom)
       
		self.button1 = wx.Button(panel, label="Ajouter")
		self.button2 = wx.Button(panel, label="Terminer")
		self.Bind(wx.EVT_BUTTON, self.on_Add, self.button1)
		self.Bind(wx.EVT_BUTTON, self.on_Finish, self.button2)
		
		tableau.AddMany([(title), (self.Combo),(self.button1,1,wx.EXPAND),(self.button2,1,wx.EXPAND)])

		hbox.Add(tableau, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
		panel.SetSizer(hbox)
		
		self.Centre()
		self.Show()  
           
	
	def on_Add(self, event):
		def trouver_produit(chaine_de_caracteres):
			for produit in Produits_liste:
				if produit.nom==chaine_de_caracteres:
					return produit
		#print myForm.text.GetValue()
		objet_produit=trouver_produit(self.Combo.GetStringSelection());
		if objet_produit:
			print 'Nous ajoutons',self.Combo.GetStringSelection()
			self.addition.append(objet_produit)
		#event.Skip()
				
		
	def on_Finish(self, event):
		total_a_payer=0
		print '---------------------------------'
		print "Addition:"
		for produit in self.addition:
			print produit.nom, " ---- ",produit.prix
			total_a_payer+=produit.prix
		print ""
		print "Total à payer:",total_a_payer
		#print myForm.text.GetValue()
		#event.Skip()
	
# Run the program
if __name__ == "__main__":
	app = wx.App()
	frame = myForm(None,"Caisse")
	app.SetTopWindow(frame)
	frame.Show()
	app.MainLoop()

