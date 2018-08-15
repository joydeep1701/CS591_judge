import json
from flask import Flask, request, render_template
from runner import ProgramEvaluator
import exceptions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ide.html')

@app.route('/api/evaluate', methods=["GET", "POST"])
def evaluate():
    if request.method == "POST":
        code_dir = request.form.get('code_dir')
        code_data = request.form.get('code_data')

        user_response = {}
        user_response['code_dir'] = code_dir

        with ProgramEvaluator("code/" + code_dir) as evaluator:
            evaluator.save_code(code_data)
            try:
                evaluator.compile()
            except exceptions.CompilationError as e:
                user_response['compilation_errors'] = True
                user_response['compiler_op'] = str(e)
                return json.dumps(user_response)

            try:
                output = evaluator.evaluate('sort')
            except Exception as e:
                user_response['runtime_errors'] = True
                return json.dumps(user_response)

            user_response['output'] = output

            return json.dumps(user_response)
                

        return "OK"
    else:
        return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)