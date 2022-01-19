def add (a, b):
    S = a+b
    return S

def mul (a, b):
    S = a*b
    return S    
    
def sous (a, b):
    S = a-b
    return S
    
def div (a, b):
    S = a/b
    return S    
    
print('ce programme permet d effectuer des calcul: addition, multiplication, division et soustraction \n')
#ici l'utilisateur effectue le choix du calcule a faire 
choix= int(input ('CHOIX DE L OPERATION A EFFECTUER \n \n1-Additionner \n2-Soustraction \n3-Multiplication \n4-Division \n'))

if choix==1:
    # Trouver la somme de deux nombres entiers
    a = int(input('Entrez le premier nombre: '))
    b = int(input('Entrez le deuxième nombre: '))
    ResultatAdd = add(a, b)
    print('RESULTAT: ', ResultatAdd)
    
elif choix==3:
    #trouver la multiplication de deux nombres 
    
    a = int(input('Entrez le premier nombre: '))
    b = int(input('Entrez le deuxième nombre: '))
    ResultatMul = mul(a, b)
    print('RESULTAT: ', ResultatMul)

elif choix==2:
    #trouver la soustraction de deux nombres 
    
    a = int(input('Entrez le premier nombre: '))
    b = int(input('Entrez le deuxième nombre: '))
    ResultatSous = sous(a, b)
    print('RESULTAT: ', ResultatSous)

elif choix==4:
    #trouver la division de deux nombres 
    
    a = int(input('Entrez le premier nombre: '))
    b = int(input('Entrez le deuxième nombre: '))
    ResultatDiv = div(a, b)
    print('RESULTAT: ', ResultatDiv)
else:
    print('VOTRE CHOIX N EXISTE PAS VEILLE')
    choix= int(input ('CHOIX DE L OPERATION A EFFECTUER \n \n1-Additionner \n2-Soustraction \n3-Multiplication \n4-Division \n'))
input('ROMEO JUNIOR  CALCULATRICE ')