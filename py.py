#Saisie de la date
year1 = int(input('Veuillez entrer une annee: '))
month1 = int(input('Veuillez entrer le mois: '))
day1 = int(input('Veuillez entrer le jour: '))
#Fonctions nécessaires au programme
#question 7

def isBissextile(year):
	if(year%4==0):
		sub=1
	else:
		sub=0
	return sub
#question 6

def SiecleNumber(year):
	if(1600<=year<1700):
		number=6
	elif(1700<=year<1800):
		number=4
	elif(1800<=year<1900):
		number=2
	elif(1900<=year<2000):
		number=0
	elif(2000<=year<2100):
		number=6
	elif(2100<=year<2200):
		number=4
	return number

#question 4

def MonthNumber(month):
	if(month==1) or (month==10):
		nb=0
	elif(month==2) or (month==3) or (month==11):
		nb=3
	elif(month==4) or (month==7):
		nb=6
	elif(month==9) or (month==12):
		nb=5
	elif(month==5):
		nb=1
	elif(month==6):
		nb=4
	elif(month==8):
		nb=2
	return nb

#question 1

def AnneeDizaine(year):
	a=year%100
	return a

#question 8

def Jour(reste):
	if(reste==0):
		day="Dimanche"
	elif(reste==1):
		day="Lundi"
	elif(reste==2):
		day="Mardi"
	elif(reste==3):
		day="Mercredi"
	elif(reste==4):
		day="Jeudi"
	elif(reste==5):
		day="Vendredi"
	elif(reste==6):
		day="Samedi"
	return day
#utilisation des fonctions en les affectant dans une variable
#programme

nombre=AnneeDizaine(year1)
nombre+=nombre//4
nombre+=day1
nombre+=MonthNumber(month1)
nombre-=isBissextile(year1)
nombre+=SiecleNumber(year1)
nombre=nombre%7
resultat=Jour(nombre)

print(resultat)


