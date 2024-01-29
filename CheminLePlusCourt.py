import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/zoero/Downloads/TP2_DONNEES_NOEUDS - Feuille1.csv")
data.head()

G=nx.MultiDiGraph()
G=nx.from_pandas_edgelist(data,source="De",target="À",edge_attr="Distance")

#Création du tableau des choix des communes possibles
communes=["Abymes","Anse-Bertrand","Baie-Mahault","Baillif","Bouillante","Capesterre","Deshaies","Gosier","Gourbeyre","Goyave","Lamentin","Morne à l eau","Moule","Petit Bourg","Petit Canal","Port-Louis","Pointe-Noire","Pointe-à-Pitre","Sainte-Anne","Saint-Claude","Saint-François","Sainte-Rose","Trois-Rivières","Vieux-Fort","Vieux-Habitants"]
print("Listes des communes :\n 0-Abymes \n 1-Anse-Bertrand \n 2-Baie-Mahault \n 3-Baillif \n 4-Bouillante \n 5-Capesterre \n 6-Deshaies \n 7-Gosier \n 8-Gourbeyre \n 9-Goyave \n 10-Lamentin \n 11-Morne à l'eau \n 12- Moule \n 13-Petit  Bourg \n 14-Petit Canal \n 15-Port-Louis \n 16-Pointe-Noire \n 17-Pointe à Pitre \n 18-Sainte-Anne \n 19-Saint-Claude \n 20-Saint-François\n 21-Saint-Rose\n 22-Trois-Rivières \n 23-Vieux-Fort \n 24-Vieux-Habitants")

#On complète le point de départs et les différents points de livraison
depart=int(input("Saissisez la commune de départ en choisissant le numéro correspondant :"))
pointsLivraison=[]
valid1=False
while valid1==False:
    if depart>=0 and depart<=24:
        pointsLivraison.append(communes[depart])
        valid1=True
    else:
        depart=int(input("La commune saisie n'est pas répertoriée, veuillez rentrer le départ de nouveau :"))

valid2=False
unPointLivraison=int(input("Saissisez un point de livraison en choisissant le numéro correspondant :"))
while valid2==False:
    if unPointLivraison>=0 and unPointLivraison<=24:
        pointsLivraison.append(communes[unPointLivraison])
        valid2=True
    else:
        unPointLivraison=int(input("La commune saisie n'est pas répertoriée, veuillez rentrer le point de livraison de nouveau :"))

response=True
i=0
while response==True and i<5:
    choix=str(input("Voulez-vous choisir un autre point de livraison (oui/non):"))
    if choix=="oui":
        unPointLivraison=int(input("Saissisez un point de livraison en choisissant le numéro correspondant :"))
        if unPointLivraison>=0 and unPointLivraison<=24:
            pointsLivraison.append(communes[unPointLivraison])
            i=i+1
        else:
            unPointLivraison=int(input("La commune saisie n'est pas répertoriée, veuillez rentrer le point de livraison de nouveau :"))
    else:
        response=False

#On cherche le cycle qui contient tous les points de livraison et commencant au point de depart
trajet=nx.approximation.traveling_salesman_problem(G,weight="Distance",nodes=pointsLivraison,cycle=True)

print("Le trajet le plus court est ",trajet,"avec un poid de",nx.path_weight(G,trajet,"Distance"))

#Affichage du Graphe complet de la guadeloupe
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
plt.show()
    
          
             
        
            

