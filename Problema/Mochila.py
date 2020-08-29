#Para cada item n, teremos um peso p e um valor v que será colocado dentro da mochila com uma capacidade.

def mochila(capacidade,p,v,n):
    #se o numero de itens e capacidade for igual a 0, retornaremos 0
    if n==0 or capacidade ==0 :
        return 0

    #Se o peso do enésimo item for mais que a capaciade da mochila, então esse item não pode ser add.

    if (p[n-1]>capacidade):
        return mochila(capacidade,p,v,n-1)

    else:
        #retorna o enésimo item incluido ou não
        return max(v[n-1] + mochila(capacidade - v[n-1],p,v,n-1),
                   mochila(capacidade,p,v,n-1))

#teste da função

v = [80, 100, 140]
p = [12, 20, 25]
capacidade= 60
n = len(v)
print (mochila(capacidade,p,v,n))

olar
