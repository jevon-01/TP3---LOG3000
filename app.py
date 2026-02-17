"""
Calculatrice web simple basée sur Flask.
Gère les routes HTTP, l'affichage de l'interface et délègue les opérations arithmétiques au module operators.py.
"""
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule le résultat d’une expression mathématique simple composée de deux nombres et d’un seul opérateur (+,-,*,/).

    Paramètres:
        expr (str): Expression mathématique fournie sous forme de chaîne de caractères.

    Sortie:
        float: Résultat du calcul.

    Raises:
        ValueError: Si l’expression est vide, mal formée, contient plus d’un opérateur ou des valeurs non numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS and i > 0:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.

    GET  : affiche l'interface de la calculatrice.
    POST : évalue l'expression soumise et retourne le résultat.

    Sortie:
        Page HTML de la calculatrice avec le résultat.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)