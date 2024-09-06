from flask import Flask, request, jsonify, render_template
import translate_ast  # 确保 translate_ast.py 文件与 app.py 在同一目录下

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # 加载 templates/index.html 文件

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        csp_code = data.get('cspCode', '')
        translated_text = translate_ast.translate_csp_code(csp_code)
        return jsonify(result=translated_text)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(result="An error occurred"), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
