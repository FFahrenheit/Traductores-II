import re

def main():
    validate_regex = re.compile(r'^print\("[^"]*"\)$')
    phrase = "-"

    while phrase != "":
        phrase = input("Ingrese la frase print a validar: ")

        if validate_regex.fullmatch(phrase) is not None:
            print("✅ Frase print válida")
        else:
            print("❌ Frase print inválida")

if __name__ == "__main__":
    main()
