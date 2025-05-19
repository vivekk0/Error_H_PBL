import ply.yacc as yacc
from lex import tokens

symbol_table = {}

def p_statement_assign(p):
    'statement : ID EQUALS expression'
    symbol_table[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("[RUNTIME ERROR] Division by zero")
            p[0] = 0
        else:
            p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] in symbol_table:
        p[0] = symbol_table[p[1]]
    else:
        print(f"[ERROR] Undefined variable '{p[1]}'")
        p[0] = 0

def p_error(p):
    if p:
        print(f"[SYNTAX ERROR] Unexpected token '{p.value}' at line {p.lineno}")
        parser.errok()
    else:
        print("[SYNTAX ERROR] Unexpected end of input")

parser = yacc.yacc()
