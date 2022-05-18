
from  flask_migrate import Migrate, MigrateCommand

from flask_script import Manager
import app
from app.models import Blog, User, Comment
app = create_app('production')

from app import create_app,db
migrate = Migrate(app,db)
manager =  Manager(app)
manager.add_command('run',)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


manager.add_command('db',MigrateCommand)
@Manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Blog=Blog, Comment=Comment)

if __name__ == '__main__':
    manager.run()