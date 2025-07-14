from flask import Flask, request

app = Flask(__name__)

@app.route("/ig", methods=["POST"])
def ig_webhook():
    data = request.json
    print("📩 Received IG message:", data)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run()
