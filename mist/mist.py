#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Here go you application specific code.

from interfaces import IProvider, ICheck
from zope.component import getGlobalSiteManager
from graphviz import Digraph
from utils import urlparsing

gsm = getGlobalSiteManager()


def get_graph_from_services(all_services):
    checks = [c(all_services) for c in gsm.getAllUtilitiesRegisteredFor(ICheck)]
    dot = Digraph()
    for service in all_services:
        dot.node(service.name, service.name,
                 color="lightblue2",
                 style="filled",
                 shape="doublecircle",
                 fixedsize="shape")
        for key, value in service.configs.items():
            for check in checks:
                sec, host, port = urlparsing(value)
                node, edge = check.test(sec, host, port)
                if node and node['name'] != service.name:
                    dot.node(**node)
                    dot.edge(service.name, node['name'], tooltip=key, **edge)

    return dot


def adapt_to_provider(provider, configs):
    prov = gsm.getUtility(IProvider, provider)
    all_services = prov.get_services(prov.get_client(configs))
    graph = get_graph_from_services(all_services)
    return graph
