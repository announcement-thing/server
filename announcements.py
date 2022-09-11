import requests

class AnnouncementMGMT:
    def __init__(self, client_mgmt):
        self.client_mgmt = client_mgmt
    def announce(self, message, from_id):
        from_name = self.client_mgmt.clients[from_id]['name']
        for client in self.client_mgmt.clients:
            self.client_mgmt.call_client(client, '/announcement', 'POST', {'from': from_name, 'data': message})
