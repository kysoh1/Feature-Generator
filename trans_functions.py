import math

# TRANSFORMATION TYPES FOR SINGLE VALUES

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def squareroot(a):
    if a < 0:
        return a ** 0.5
    else:
        raise Exception("Can't square root negative value.")

def log(a):
    try:
        return math.log(a)
    except:
        raise Exception("Invalid value for log function.")

def reciprocal(a):
    if a != 0:
        return 1 / a
    else:
        raise Exception("Can't divide by zero.")

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def square_reciprocal(a):
    if a * a != 0:
        return 1 / a * a
    else:
        raise Exception("Can't divide by zero.")

def cube_reciprocal(a):
    if a * a * a != 0:
        return 1 / a * a * a
    else:
        raise Exception("Can't divide by zero.")

trans_functions_1 = [square, cube, squareroot, reciprocal, sin, cos, tan, square, square_reciprocal, cube_reciprocal]

# TRANSFORMATION TYPES FOR TWO VALUES

def multiply(a, b):
    return a * b

def log(a, b):
    try:
        return math.log(a, b)
    except:
        raise Exception("Invalid values for log function.")

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise Exception("Can't divide by zero.")

def average(a, b):
    return (a + b) / 2

def power(a, b):
    return math.pow(a, b)

def maximum(a, b):
    return max(a, b)

def minimum(a, b):
    return min(a, b)

def multiply_average(a, b):
    return a * b / 2

def sin2(a, b):
    return math.sin(a) * b

def cos2(a, b):
    return a * math.cos(a) * b

def tan2(a, b):
    return a * math.tan(a) * b

def pythag_triple(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def log_square(a, b):
    try:
        return log(a, b) ** 2
    except:
        raise Exception("Invalid values for log function.")
    
def log_cube(a, b):
    try:
        return log(a, b) ** 3
    except:
        raise Exception("Invalid values for log function.")

def average_square(a, b):
    return average(a, b) ** 2

def average_cube(a, b):
    return average(a, b) ** 3

trans_functions_2 = [multiply, log, divide, average, multiply_average, sin2, cos2, tan2, pythag_triple, log_square, log_cube, average_square, average_cube]

# TRANSFORMATION TYPES FOR THREE VALUES

def multiply3(a, b, c):
    return a * b * c

def average3(a, b, c):
    return (a + b + c) / 3

def multiply3_average(a, b, c):
    return a * b * c / 3

def maximum3(a, b, c):
    return max(a, b, c)

def minimum3(a, b, c):
    return min(a, b, c)

def multiply3_average(a, b, c):
    return a * b * c / 3

def sin3(a, b, c):
    return math.sin(a + b) * c

def cos3(a, b, c):
    return a * math.cos(a + b) * c

def tan3(a, b, c):
    return a * math.tan(a + b) * c

def pythag_quad(a, b, c):
    return (a ** 2 + b ** 2 + c ** 2) ** 0.5

def pythag_quad_average(a, b, c):
    return (a ** 2 + b ** 2 + c ** 2) ** 0.5 / 3

def log_multiply3(a, b, c):
    try:
        return log(a * b * c)
    except:
        raise Exception("Invalid values for log function.")
    
def log_average3(a, b, c):
    try:
        return log((a + b + c) / 3)
    except:
        raise Exception("Invalid values for log function.")

trans_functions_3 = [multiply3, average3, multiply3_average, sin3, cos3, tan3, pythag_quad, pythag_quad_average, log_multiply3, log_average3]

# TRANSFORMATION TYPES FOR FOUR VALUES

def multiply4(a, b, c, d):
    return a * b * c * d

def average4(a, b, c, d):
    return (a + b + c + d) / 4

def multiply4_average(a, b, c, d):
    return a * b * c * d / 4

def maximum4(a, b, c, d):
    return max(a, b, c, d)

def minimum4(a, b, c, d):
    return min(a, b, c, d)

def sin4(a, b, c, d):
    return math.sin(a + b + c) * d

def cos4(a, b, c, d):
    return a * math.cos(a + b + c) * d

def tan4(a, b, c, d):
    return a * math.tan(a + b + c) * d

def pythag_quint(a, b, c, d):
    return (a ** 2 + b ** 2 + c ** 2 + d ** 2) ** 0.5

def pythag_quint_average(a, b, c, d):
    return (a ** 2 + b ** 2 + c ** 2 + d ** 2) ** 0.5 / 4

def log_multiply4(a, b, c, d):
    try:
        return log(a * b * c * d)
    except:
        raise Exception("Invalid values for log function.")
    
def log_average4(a, b, c, d):
    try:
        return log((a + b + c + d) / 4)
    except:
        raise Exception("Invalid values for log function.")

trans_functions_4 = [multiply4, average4, multiply4_average, sin4, cos4, tan4, pythag_quint, pythag_quint_average, log_multiply4, log_average4]

# TRANSFORMATION TYPES FOR FIVE VALUES

def multiply5(a, b, c, d, e):
    return a * b * c * d * e

def average5(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def multiply5_average(a, b, c, d, e):
    return a * b * c * d * e / 5

def maximum5(a, b, c, d, e):
    return max(a, b, c, d), e

def minimum5(a, b, c, d, e):
    return min(a, b, c, d, e)

def pythag_hex(a, b, c, d, e):
    return (a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2) ** 0.5

def pythag_hex_average(a, b, c, d, e):
    return (a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2) ** 0.5 / 4

def log_multiply5(a, b, c, d, e):
    try:
        return log(a * b * c * d * e)
    except:
        raise Exception("Invalid values for log function.")
    
def log_average5(a, b, c, d, e):
    try:
        return log((a + b + c + d + e) / 5)
    except:
        raise Exception("Invalid values for log function.")

trans_functions_5 = [multiply5, average5, multiply5_average, pythag_hex, pythag_hex_average, log_multiply5, log_average5]

# Return array of functions

def get_trans_functions_1():
    return trans_functions_1

def get_trans_functions_2():
    return trans_functions_2

def get_trans_functions_3():
    return trans_functions_3

def get_trans_functions_4():
    return trans_functions_4

def get_trans_functions_5():
    return trans_functions_5