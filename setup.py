#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='check_ruckus_vsz',
	version='0.14',
	description='Nagios Check for Ruckus SCG',
	author='Lukas Schauer, Dr. Torge Szczepanek',
	author_email='info@cygnusnetworks.de',
	license='Apache 2.0',
	packages=['ruckus_vsz_snmp'],
	scripts=['check_ruckus_vsz', 'check_ruckus_ap'],
	zip_safe=False,
	install_requires=['configparser', 'nagiosplugin', 'pysnmp', 'pysnmp-mibs', 'ipaddress'])
