data1="Publicado em: Segunda-feira, 30 de Maio de 2022 16h39min18s BRT"
data2="Publicado em: Quarta-feira, 25 de Maio de 2022 23h39min03s BRT"
a=f'3408#{data1}\n3245#{data2}'
a=a.splitlines()

materia = {}
for x in a: 
    print(x.split("#"))
    
    
    
#    x=x.split()
#    materia[x[0]]=x[1]
#print(materia["3408"])
