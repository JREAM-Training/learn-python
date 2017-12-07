from fabric.api import *

env.user = 'root'
env.host_string = '162.243.26.53'

# Local DB Settings
dev = dict(
   host='localhost',
   port=3306,
   user='root',
   passwd='',
   dbname='jrbug'
)
production = dict(
   path='/var/www/',
   host='localhost',
   port=3306,
   user='root',
   passwd='',
   dbname='jrbug'
)

def deploy(branch = 'master'):
    with cd(production['path']):
        run('git pull origin {0}'.format(branch))

def deploydb(filename = 'schema.sql'):
    with cd(production['path']):
        run('mysql -h {0} -P {1} -u {2} {3} < {4}'.format(
            production['host'],
            production['port'],
            production['user'],
            production['dbname'],
            filename
        ))

# $ fab commit
# $ fab commit:dev
def commit(branch = 'master'):
    local('git add -u')
    local('git add .')
    msg = prompt('Commit Message: ')
    local('git commit -m "{0}"'.format(msg))
    local('git push origin {0}'.format(branch))

def pull(branch = 'master'):
    local('git pull origin {0}'.format(branch))

# $ fab dumpdb
# $ fab dumpdb:filename.sql
def dumpdb(filename = 'schema.sql'):
    local('mysqldump -h {0} -P {1} -u {2} {3} > {4}'.format(
        dev['host'],
        dev['port'],
        dev['user'],
        dev['dbname'],
        filename
    ))

# $ fab import
# $ fab import:filename.sql
def importdb(filename = 'schema.sql'):
    local('mysql -h {0} -P {1} -u {2} {3} < {4}'.format(
        dev['host'],
        dev['port'],
        dev['user'],
        dev['dbname'],
        filename
    ))

