from flask import Flask, request, jsonify, send_file
import qrcode
import io
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "欢迎使用 LMBTFY API！\n- /api/lmbtfy?q=xxx 返回搜索链接\n- /api/qrcode?q=xxx 返回二维码"

@app.route('/api/lmbtfy')
def lmbtfy():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "请提供参数 q"}), 400

    url = f"https://lmbtfy.cn/?q={query}"
    return jsonify({"url": url})

@app.route('/api/qrcode')
def qrcode_api():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "请提供参数 q"}), 400

    url = f"https://lmbtfy.cn/?q={query}"
    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
