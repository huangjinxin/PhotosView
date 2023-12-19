from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        # 设置图片保存路径，比如 "uploads/"
        uploaded_file.save(uploaded_file.filename)
        return jsonify({"message": "File uploaded successfully"})
    return jsonify({"message": "No file uploaded"})

if __name__ == '__main__':
    app.run(debug=True)
