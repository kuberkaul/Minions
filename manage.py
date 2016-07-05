#!/usr/bin/env python

import os

from flask.ext.script import Manager, Server, prompt_bool
from flask.ext.script.commands import ShowUrls, Clean
from minions import create_app
from minions.models import db, User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('minions.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db, User=User)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()


@manager.command
def dropdb():
    """Drop all DB tables and start afresh. Lose all data.
    """
    """
    :return:
    """
    if prompt_bool(
            "Are you sure you want to lose all your data"):
        db.drop_all()


if __name__ == "__main__":
    manager.run()
