#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'tao_bip32utils',
    version = '0.3-3',
    author = 'Bryce Weiner',
    author_email = 'bryce@tao.network',
    url = 'http://github.com/taoblockchain/tao_bip32utils',
    description = 'Utilities for generating and using Bitcoin Hierarchical Deterministic wallets (BIP0032), modified for Tao',
    license = 'MIT',
    install_requires = ['ecdsa'],
    packages = ['bip32utils'],
    scripts = ['tao_bip32gen']
)
