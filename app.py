from flask import Flask, render_template

app =  Flask(__name__)

@app.route('/')
def home():
    try:
        serverID = '1234567'
        return render_template("index.html", value=serverID)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
