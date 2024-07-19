import math

def calculate(operator: str, value: str):
    result = ''
    try:
        if value[0] != '√':
            if operator == '=' and value:
                result = eval(value)
            elif operator == '+/-':
                result = -float(value)
            else:
                result = "Error"
        else:
            value = value.replace('√', '')
            if value:
                result = eval(value)
                result = math.sqrt(result)
            else:
                result = "Error"
    
    except Exception as e:
        result = "Error"
    return result

# Exemplos de uso
print(calculate('=', '√16'))  # Deve retornar 4.0
print(calculate('=', '4+2'))  # Deve retornar 6
print(calculate('+/-', '4'))  # Deve retornar -4.0
