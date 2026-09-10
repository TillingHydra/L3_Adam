def calculer_mes_impots(mon_revenu : int) -> int :
#nono    

  if mon_revenu < 11497 :
   taux = 0 

  elif mon_revenu < 29315 and mon_revenu > 11497 : 
    taux = 0.11

  elif mon_revenu < 83823 and mon_revenu > 29316 : 
    taux = 0.30 

  elif mon_revenu < 180394 and mon_revenu > 83823 : 
    taux = 0.41

  elif mon_revenu > 180394 : 
    taux = 0.45



  return mon_revenu * taux

print(calculer_mes_impots(290000))


        
