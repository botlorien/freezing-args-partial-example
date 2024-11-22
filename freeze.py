from operator import mul
from functools import partial
import unicodedata

def tag(name,*content,class_=None,**attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attrs_pairs = (f' {attr}="{value}"' for attr,value in sorted(attrs.items()))
    attrs_str = ''.join(attrs_pairs)
    if content:
        elements=(f'<{name}{attrs_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attrs_str} />'

if __name__=='__main__':
    # Encapsula a função mul congelando o primeiro argumento
    triple = partial(mul,3)

    # A nova função requer apenas o segundo argumento
    print(triple(7))
    print(list(map(triple,range(1,10))))

    # Congelando o primeiro argumento NFC
    nfc = partial(unicodedata.normalize,'NFC')

    # Testando antes e depois da normalização
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1,s2)
    print(s1==s2)
    print(nfc(s1),nfc(s2)) 

    # criando uma função para imagens usando partial congelando alguns argumentos caracteristicos de imagem
    picture = partial(tag,'img',class_='pic-frame')

    # Exibindo alguns resultados, objeto e parametros
    print(picture(src='wumpus.jpeg'))
    print(picture)
    print(picture.args)
    print(picture.keywords)