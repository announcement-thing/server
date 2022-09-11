from flask import Flask, jsonify, request
import announcements
import clients

app = Flask(__name__)
client_mgmt = clients.ClientMGMT()
announcement_mgmt = announcements.AnnouncementMGMT(client_mgmt)

@app.errorhandler(500)
def handle500(e):
    return jsonify({
        'code': 500,
        'data': 'Internal Server Error'
    })

@app.errorhandler(404)
def handle404(e):
    return jsonify({
        'code': 404,
        'data': 'Not found'
    })

@app.errorhandler(400)
def handle400(e):
    return jsonify({
        'code': 400,
        'data': 'Bad request'
    })

@app.errorhandler(405)
def handle400(e):
    return jsonify({
        'code': 405,
        'data': 'Method Not Allowed'
    })

@app.route('/announce', methods=['POST'])
def announce():
    data = request.form
    
    return jsonify({
        'code': 200,
        'data': 'Announced'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4861)
