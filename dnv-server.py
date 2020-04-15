from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/status')
def hello():
    return jsonify({'status': 'API OK'})

if __name__ == '__main__':
    app.run()
