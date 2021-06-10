from flask import *

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時
@app.route("/")
def root():
    # HTMLでWebフォームを記述
    return """
    <html><body>
    <form action="/tashizan" method="post">
      <input type="text" name="a"> +
      <input type="text" name="b">
      <input type="submit" value="計算">
    </form>
    <form action="/hikizan" method="post">
      <input type="text" name="c"> -
      <input type="text" name="d">
      <input type="submit" value="計算">
    </form>
    <form action="/kakezan" method="post">
      <input type="text" name="e"> ×
      <input type="text" name="f">
      <input type="submit" value="計算">
    </form>
    <form action="/warizan" method="post">
      <input type="text" name="g"> ÷
      <input type="text" name="h">
      <input type="submit" value="計算">
    </form>
    """

# フォームの値を受け取って結果を表示
@app.route("/tashizan", methods=["post"])
def tashizan():
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    r = a + b
    return "<h1>答えは..." + str(r) + "</h1>"

@app.route("/hikizan", methods=["post"])
def hikizan():
    a = int(request.form.get("c"))
    b = int(request.form.get("d"))
    r = a - b
    return "<h1>答えは..." + str(r) + "</h1>"

@app.route("/kakezan", methods=["post"])
def kakezan():
    a = int(request.form.get("e"))
    b = int(request.form.get("f"))
    r = a * b
    return "<h1>答えは..." + str(r) + "</h1>"

@app.route("/warizan", methods=["post"])
def warizan():
    a = int(request.form.get("g"))
    b = int(request.form.get("h"))
    r = a / b
    return "<h1>答えは..." + str(r) + "</h1>"

# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True, port=8888)