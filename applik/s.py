#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: s.py
@time: 2018/2/16 15:20
"""

from flask import Flask
from applik import *
app = Flask(__name__)


@app.route("/hello")
def ihello():
    return "Hello OpenShift World!"
