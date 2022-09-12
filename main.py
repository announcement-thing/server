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
    data = request.form['id']
    return jsonify({
        'code': 200,
        'data': 'Announced'
    })

@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.form
    id = client_mgmt.add_client(request.remote_addr, data['name'])
    print('Client {} added'.format(id))
    return jsonify({
        'code': 200,
        'id': id
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4861)
