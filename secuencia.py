import math

def completar_1_bloque(vertical, horizontal):
    
    resultado_y = sum(vertical)
    print(f'Sumatoria del eje vertical es {resultado_y}') 
    if resultado_y <= 45:
        resto_y = 45 - resultado_y
        print(f'Numero {resto_y} agregado.')
        vertical.append(resto_y)
        vertical.sort()
    else:
        print('El vector está completo')
    
    resultado_x = sum(horizontal)
    print(f'Sumatoria del eje vertical es {resultado_x}')
    if resultado_x <= 45:
        resto_x = 45 -resultado_x
        print(f'Numero {resto_x} agregado.')
        horizontal.append(resto_x)
        horizontal.sort()
    else:
        print('El vector está completo')
    
    return f'Vertical: {vertical} / Horizontal {horizontal}'
    
    


if __name__ == '__main__':
    horizontal = [1,2,3,4,5,6,8,9]
    vertical = [1,3,4,5,6,7,8,9]

    final = completar_1_bloque(vertical, horizontal)

    
    
    
    
