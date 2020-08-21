def pato():
    a=int(input(''))
    b=int(input(''))
    c=int(input(''))
    d=int(input(''))
    e=int(input(''))
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
    
