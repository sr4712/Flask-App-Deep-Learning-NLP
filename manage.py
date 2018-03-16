#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module to start the application.
"""
import os
from flask_script import Server, Manager
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("runserver", Server())


if __name__ == "__main__":
    #python manage.py runserver
    manager.run()
