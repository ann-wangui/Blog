from flask_script import Manager,Server

from app.models import Blog, User, Comment
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from config import config_options

app = create_app('production')

manager =  Manager(app)
manager.add_command('run',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Blog=Blog, Comment=Comment)

    
@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)

if __name__ == '__main__':
    manager.run()
