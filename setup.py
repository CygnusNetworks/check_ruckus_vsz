#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='check_ruckus_vsz',
	version='0.13',
	description='Nagios Check for Ruckus SCG',
	author='Lukas Schauer',
	author_email='l.schauer@cygnusnetworks.de',
	license='Apache 2.0',
	packages=['ruckus_vsz_snmp'],
	scripts=['check_ruckus_vsz', 'check_ruckus_ap'],
	zip_safe=False,
	install_requires=['configparser', 'nagiosplugin', 'pysnmp', 'pysnmp-mibs', 'ipaddress'])
