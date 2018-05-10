#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import random 

print "1: Pierre"
print "2: Feuille"
print "3: Ciseau"
print "4: Puits"

noms_des_choix=["Pierre","Feuille","Ciseau","Puits"]

perd="L'ordinateur gagne"
gagne="Vous gagnez"
nul="Match nul"

regle={
	"11":nul,
	"12":perd,
	"13":gagne,
	"14":perd,
	
	"21":gagne,
	"22":nul,
	"23":perd,
	"24":gagne,
	
	"31":perd,
	"32":gagne,
	"33":nul,
	"34":perd,
	
	"41":gagne,
	"42":perd,
	"43":gagne,
	"44":nul
	}
	
	
	
def Comparer(deux_choix):
	return regle[deux_choix]

for nombre_de_jeu in range(12):
	je_joue=raw_input("entrez un chiffre de 1 à 4: ")
	Ordinateur_joue=1+int(random.random()*4)
	if Ordinateur_joue>4:
		Ordinateur_joue=4
	print "Vous jouez:",noms_des_choix[int(je_joue)-1]
	print "l'ordinateur joue:",Ordinateur_joue,noms_des_choix[Ordinateur_joue-1]
	resultat=Comparer(je_joue+str(Ordinateur_joue))
	print resultat
	print "----------------------------"
