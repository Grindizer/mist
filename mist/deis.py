__author__ = 'nacim'


from hapydeis import Client
from mist import gsm
from interfaces import IService

class ServiceFromApp(object):
    def __init__(self, app):
        self.endpoint = app['url']
        self.name = app['id']
        self.configs = app['values']


class DeisProvider(object):
    def get_client(self, configs):
        endpoint = configs.get('endpoint')
        username = configs.get('username')
        password = configs.get('password')
        client = Client(endpoint)
        client.authenticate(username, password)
        return client

    def get_services(self, client):
        s = []
        for app in client.apps.get()['results']:
            deis_app = getattr(client.apps, app['id'])
            app['values'] = deis_app.configs.get()['values']
            adapter = gsm.getUtility(IService, 'deis')
            s.append(adapter(app))
        return s
