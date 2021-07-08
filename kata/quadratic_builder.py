import re
def quadratic_builder(expression):
    #Good Luck!!
        
    # get separate expression enclosed in ()
    sub_equation_1, sub_equation_2 = re.findall('\(.*?\)', expression)
    
    unknown_variable = re.findall('[a-zA-z]', sub_equation_1)[0]
    m, n = get_values(sub_equation_1, unknown_variable)
    p, q = get_values(sub_equation_2, unknown_variable)

    # formatting the result in form of ix^2 + hx + j
    i = m * p
    if i == 1:
        ix = '{}^2'.format(unknown_variable[0])
    elif i == -1:
        ix = '-{}^2'.format(unknown_variable[0])
    else:
        ix = '{}{}^2'.format(i, unknown_variable[0])

    h = (m * q) + (n * p)
    if h > 1:
        hx = '+{}{}'.format(h, unknown_variable[0])
    elif h == 1:
        hx = '+{}'.format(unknown_variable[0])
    elif h == -1:
        hx = '-{}'.format(unknown_variable[0])
    elif h == 0:
        hx = ''
    else:
        hx = '{}{}'.format(h, unknown_variable[0])
    
    j = n * q
    if j > 0:
        j = '+{}'.format(j)
    elif j == 0:
        j = ''

    return '{}{}{}'.format(ix, hx, j)

def get_values(sub_equation, variable):
    formated_equation = re.sub('-[a-zA-z]', '-1{}'.format(variable), sub_equation)
    values = re.findall('-?\d+', formated_equation)
    
    if len(values) == 2:
        slope = int(values[0])
        intercept = int(values[1])
    else:
        slope = 1
        intercept = int(values[0])

    return (slope, intercept)

#5x^2-6x+8
equa = '(-h-7)(4h+3)'
print(quadratic_builder(equa))