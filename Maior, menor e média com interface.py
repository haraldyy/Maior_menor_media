def pato():
    a=int(input('Digite o primeiro numero:'))
    b=int(input('Digite o segundo numero:'))
    c=int(input('Digite o terceiro numero:'))
    d=int(input('Digite o quarto numero:'))
    e=int(input('Digite o quinto numero:'))
    maior=max(a,b,c,d,e)
    menor=min(a,b,c,d,e)
    ma=(a+b+c+d+e)//5
    print(f'{maior}')
    print(f'{menor}')
    print(f'{ma}')
    return(f'{maior}{menor},{ma}')

def main():
    pato()

if __name__=='__main__':
       main()
    
