from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "欢迎使用 LMBTFY API！访问 /api/lmbtfy?q=XXX 生成搜索链接。"

@app.route('/api/lmbtfy')
def lmbtfy():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "请提供参数 q"}), 400

    url = f"https://lmbtfy.cn/?q={query}"
    return jsonify({"url": url})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
