from flask import Flask, jsonify, request, make_response
import announcements
import clients

app = Flask(__name__)
client_mgmt = clients.ClientMGMT()
announcement_mgmt = announcements.AnnouncementMGMT(client_mgmt)

@app.errorhandler(500)
def handle500(e):
    return make_response(jsonify({
        'code': 500,
        'data': 'Internal Server Error'
    }), 500)

@app.errorhandler(404)
def handle404(e):
    return make_response(jsonify({
        'code': 404,
        'data': 'Not found'
    }), 404)

@app.errorhandler(400)
def handle400(e):
    return make_response(jsonify({
        'code': 400,
        'data': 'Bad request'
    }), 400)

@app.errorhandler(405)
def handle400(e):
    return make_response(jsonify({
        'code': 405,
        'data': 'Method Not Allowed'
    }), 405)

@app.route('/announce', methods=['POST'])
def announce():
    data = request.form
    announcement_mgmt.announce(data['message'], data['id'])
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
