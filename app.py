from flask import Flask
from flask import render_template, Response
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/automate')
def automate():
    return render_template('automate.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/data_stream')
def data_stream():
    def gen():
        for c in 'Hello world!':
            yield c
            time.sleep(0.5)
    return Response(gen())


if __name__ == "__main__":
    app.run()
