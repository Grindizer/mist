__author__ = 'Nassim Babaci'


from zope.interface import Interface, Attribute

class IService(Interface):
    name = Attribute("the name")
    endpoint = Attribute("url")
    configs = Attribute("dict of config")


class ICheck(Interface):
    name = Attribute("the name")
    all_services = Attribute("list of IService")

    def test(sec, host, port):
        """
        perform the test
        """

class IProvider(Interface):
    def get_client(configs):
        """
        Given a dict of configs, return the client
        to use to access services information
        :param configs:
        :return:
        """

    def get_services(client):
        """
        From client return all services in provider.
        :param client:
        :return:
        """
