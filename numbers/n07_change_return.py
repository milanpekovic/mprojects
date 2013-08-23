def vracanje_kusura():
  cena = int(raw_input('Unesite cenu:'))
  depozit = int(raw_input('Unesite iznos kojim biste platili:'))
  kusur = depozit - cena
  
  
  pethilj = kusur / 5000
  kusur -= pethilj * 5000
  
  dvehilj = kusur / 2000
  kusur -= dvehilj * 2000
  
  hiljade = kusur / 1000
  kusur -= hiljade * 1000
  
  petsto = kusur / 500
  kusur -= petsto * 500
  
  dvesta = kusur / 2000
  kusur -= dvesta * 200
  
  sto = kusur / 100
  kusur -= sto * 100
  
  pedeset = kusur / 50
  kusur -= pedeset * 50
  
  dvadeset = kusur / 20
  kusur -= dvadeset * 20
  
  deset = kusur / 10
  kusur -= deset * 10
  
  pet = kusur / 5
  kusur -= pet * 5
  
  dva = kusur / 2
  kusur -= dva * 2
  
  jedan = kusur
  
  
  print (''' {} po pet hiljada\n {} po dve hiljade
 {} po hiljadu\n {} po petsto\n {} po dvesta
 {} po sto\n {} po pedeset\n {} po dvadeset
 {} po deset\n {} po pet\n {} po dva
 {} po dinar''').format(pethilj , dvehilj, hiljade, petsto, dvesta, sto, pedeset, dvadeset, deset, pet, dva, jedan)
  
vracanje_kusura()
  
  