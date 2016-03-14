__author__ = 'nacim'

from zope.component import getGlobalSiteManager
from utils import urlparsing
from os import path

current_dir = path.dirname(path.realpath(__file__))
image_path = path.join(current_dir, "images")

gsm = getGlobalSiteManager()

class ServiceCheck(object):
    name = None
    image = ""

    def __init__(self, all_services):
        self.all_services = all_services

    def test(self, sec, host, port):
        for service in self.all_services:
            host_sec, service_host, port = urlparsing(service.endpoint)
            if service_host == host:
                # return service node.
                return dict(
                    name=service.name,
                    label=service.name,
                    image=self.image,
                    color="lightblue2",
                    style="filled",
                    shape="doublecircle",
                    fixedsize="shape"
                ), dict(
                    color= "red" if sec else "blue",
                    stype= "bold" if sec else "solid",
                    label= port if port else ""
                )
        return None, None


class RDSCheck(object):
    name = None
    image = path.join(image_path, "rds.png")

    def __init__(self, all_services):
        self.all_services = all_services

    def test(self, sec, host, port):
        if host and 'rds' in host:
                # return service node.
            return dict(
                name=host,
                label="",
                image=self.image,
                fixedsize="true",
                color="white"
            ), dict(
                color= "red" if sec else "blue",
                stype= "bold" if sec else "solid",
                label= str(port) if port else ""
            )
        return None, None


class ECCheck(object):
    name = None
    image = path.join(image_path, "ec.png")

    def __init__(self, all_services):
        self.all_services = all_services

    def test(self, sec, host, port):
        if host and ('cache' in host or 'redis' in host):
                # return service node.
            return dict(
                name=host,
                label="",
                image=self.image,
                fixedsize="true",
                color="white"
            ), dict(
                color= "red" if sec else "blue",
                stype= "bold" if sec else "solid",
                label= str(port) if port else ""
            )
        return None, None


class SQSCheck(object):
    name = None
    image = path.join(image_path, "sqs.png")

    def __init__(self, all_services):
        self.all_services = all_services

    def test(self,  sec, host, port):
        if host and ('sqs' in host):
                # return service node.
            return dict(
                name=host,
                label="",
                image=self.image,
                fixedsize="true",
                color="white"
            ), dict(
                color= "red" if sec else "blue",
                stype= "bold" if sec else "solid",
                label= str(port) if port else ""
            )
        return None, None


class ESCheck(object):
    name = None
    image = path.join(image_path,"es.png")

    def __init__(self, all_services):
        self.all_services = all_services

    def test(self, sec, host, port):
        if host and ('elasticsearch' in host):
                # return service node.
            return dict(
                name=host,
                label="",
                image=self.image,
                fixedsize="true",
                color="white"
            ), dict(
                color= "red" if sec else "blue",
                stype= "bold" if sec else "solid",
                label= str(port) if port else ""
            )
        return None, None
