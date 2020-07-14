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
    
    return resto_x, resto_y

def completar_2_bloques(vertical, horizontal):
    
    """ Implementar binary search en recursividad """
    catch_y = sum(vertical)
    if catch_y <= 45:
        resto_y = 45 - catch_y
        resto_y_1 = resto_y // 2
        resto_y_2 = resto_y - resto_y_1 
        print(f'Numeros {resto_y_1} y {resto_y_2} agregados')
        vertical.append(resto_y_1)
        vertical.append(resto_y_1)
        
        vertical.sort()
    else:
        print('El vector está completo')
    
    catch_x = sum(horizontal)
    if catch_x <= 45:
        resto_x = 45 - catch_x
        resto_x_1 = resto_x // 2
        resto_x_2 = resto_x - resto_x_1 
        print(f'Numeros {resto_x_1} y {resto_x_2} agregados')
        horizontal.append(resto_x_1)
        horizontal.append(resto_x_2)
        
        horizontal.sort()
    else:
        print('El vector está completo')
    
    return resto_y_1, resto_y_2, resto_x_1, resto_x_2

def busqueda_binaria():
    pass   



    
    


if __name__ == '__main__':
    horizontal = [1,2,4,5,6,8,9]
    vertical = [1,2,3,4,6,8,9]

    print(f'Valores iniciales: {vertical}')
    print(f'Valores iniciales: {horizontal}')


    final = completar_2_bloques(vertical, horizontal)

    
    
    
    
