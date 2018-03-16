#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Blueprint creation.
"""
from flask import Blueprint


main = Blueprint('main', __name__)

from . import views, errors
