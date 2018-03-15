#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from app import create_app
from flask_script import Server, Manager


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command("runserver", Server())


if __name__ == "__main__":
    #python manage.py runserver
    manager.run()
