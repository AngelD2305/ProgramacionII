from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    accept_header = request.headers.get('Accept')
    
    if accept_header == 'application/json':
        return jsonify(message='pong')
    else:
        return Response('debe ser un json'. status=406, mimeype='text/plain')
   
if __name__=='__main__':
    app.run(port=5000)
