# Ismael Iván López Murillo - 220975903
# Actividad Diagnósitca
# Traductores de Lenguajes II - Luis Felipe Muñoz Mendoza

def insert_sorted(elements: list, data):
    elements.append(data)
    # Insertar al final de la lista
    i = len(elements) - 2
    
    # Dependiendo de su ubicación, se recorrerán los elementos al inicio o al final
    while i >= 0 and elements[i] > data:
        elements[i+1], elements[i] = elements[i], elements[i+1]
        i -= 1

def main():
    rows = 4
    columns = 5
    elements = []
    final_matrix = [[None for _ in range(columns)] for _ in range(rows)]

    for i in range(rows*columns):
        try:
            data = int(input(f"Ingrese el dato {i + 1}: "))
            insert_sorted(elements, data)
        except:
            print('Por favor, inserte solo valores numéricos')

    for index, data in enumerate(elements):
        row = index // columns
        column = index % columns
        final_matrix[row][column] = data

    print(final_matrix)

if __name__ == '__main__':
    main()