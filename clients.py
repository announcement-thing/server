import uuid
import requests

class ClientMGMT:
    def __init__(self):
        self.clients = {}
    def add_client(self, ip, name):
        id = str(uuid.uuid4())
        self.clients[id] = {'ip': ip, 'name': name}
        return id
    def remove_client(self, id):
        del self.clients[id]
    def ping_client(self, id):
        try:
            requests.get('http://{}:4860/ping'.format(self.clients[id]['ip']))
        except:
            print('Client {} is offline, so it was removed from the list'.format(id))
            return False
        else:
            return True
    def call_client(self, id, path, method, data=None):
        if self.ping_client(id):
            if method == 'GET':
                requests.get('http://{}:4860{}'.format(self.clients[id]['ip'], path))
            elif method == 'POST':
                request.post('http://{}:4860{}'.format(self.clients[id]['ip'], path), data=data)
