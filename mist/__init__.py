#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from deis import ServiceFromApp, DeisProvider
from checks import ServiceCheck, RDSCheck, ECCheck, SQSCheck, ESCheck
from interfaces import IService, IProvider, ICheck
from mist import gsm

gsm.registerUtility(ServiceFromApp, IService, 'deis')
gsm.registerUtility(DeisProvider(), IProvider, 'deis')

gsm.registerUtility(ServiceCheck, ICheck, 'service')
gsm.registerUtility(RDSCheck, ICheck, 'rds')
gsm.registerUtility(ECCheck, ICheck, 'ec')
gsm.registerUtility(SQSCheck, ICheck, 'sqs')
gsm.registerUtility(ESCheck, ICheck, 'es')
