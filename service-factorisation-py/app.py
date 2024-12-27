from flask import Flask, request, jsonify
from factorisation_solver import advanced_factorization

app = Flask(__name__)

@app.route('/factoriser', methods=['POST'])
def factorize_advanced():

    try:
        # Lecture des données JSON envoyées par le client
        data = request.json
        equation = data.get('equation')
        variable = data.get('variable', 'x')

        if not equation:
            return jsonify({"success": False, "error": "L'équation est obligatoire."}), 400

        # Appel à la fonction de factorisation
        factorized_result = advanced_factorization(equation, variable)

        # La réponse
        return jsonify({
            "success": True,
            "original_equation": equation,
            "factorized_result": factorized_result
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
    equation = equation.replace('^', '**')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
