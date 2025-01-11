def verificar_secuencia(a, b, c, mod=10000):
    # Verificación de los primeros números conocidos
    primeros_conocidos = [
        (1, 2023),
        (2, 2024),
        (3, 2025),
        (4, 6072),
        (50, 3360)  # Ejemplo conocido del problema
    ]
    
    sequence = [(a % mod), (b % mod), (c % mod)]
    
    # Verificamos los números conocidos
    for pos, expected in primeros_conocidos:
        if pos <= 3:
            actual = sequence[pos-1]
        else:
            while len(sequence) < pos:
                next_num = (sequence[-3] + sequence[-2] + sequence[-1]) % mod
                sequence.append(next_num)
            actual = sequence[pos-1]
        
        if actual != (expected % mod):
            print(f"Error: En posición {pos}, se esperaba {expected % mod} pero se obtuvo {actual}")
            return None
    
    # Una vez verificados los números conocidos, buscamos el ciclo
    seen = {}
    state = tuple(sequence[-3:])
    seen[state] = len(sequence)
    
    # Generamos más números hasta encontrar un ciclo
    for _ in range(200000):  # Aumentamos el límite para asegurar encontrar el ciclo correcto
        next_num = (state[0] + state[1] + state[2]) % mod
        state = (state[1], state[2], next_num)
        sequence.append(next_num)
        
        if state in seen:
            start_cycle = seen[state]
            cycle_length = len(sequence) - start_cycle
            
            # Verificación rigurosa del ciclo
            temp_state = state
            is_valid_cycle = True
            for _ in range(cycle_length):
                next_temp = (temp_state[0] + temp_state[1] + temp_state[2]) % mod
                temp_state = (temp_state[1], temp_state[2], next_temp)
                if temp_state == state:
                    break
            
            if temp_state != state:
                seen[state] = len(sequence)
                continue
            
            # Si el ciclo es válido, calculamos la posición
            pos = 2023202320232023
            pos_within_cycle = (pos - start_cycle) % cycle_length
            result = sequence[start_cycle + pos_within_cycle]
            
            print("\n=== Resultados Verificados ===")
            print(f"✓ Primeros números correctos")
            print(f"✓ Posición 50 correcta (3360)")
            print(f"✓ Ciclo encontrado: inicio={start_cycle}, longitud={cycle_length}")
            print(f"✓ Posición {pos} cae en índice {pos_within_cycle} del ciclo")
            print(f"\nResultado final: {result}")
            print("✓ Ciclo verificado correctamente")
            
            return result
        
        seen[state] = len(sequence)
    
    print("⚠️ No se encontró un ciclo válido después de muchas iteraciones")
    return None

# Ejecutamos con los valores iniciales
resultado = verificar_secuencia(2023, 2024, 2025)
if resultado is not None:
    print(f"\nLos últimos 4 dígitos en la posición 2023202320232023 son: {resultado}")
