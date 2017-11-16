
from fabric.api import sudo, put, cd, env
from fabric.decorators import roles


def add_automation_agent():
    sudo('mkdir -p /opt/mongo')
    put('/opt/mongodb/mongodb-mms-automation-agent-manager.deb', '/opt/mongo', use_sudo=True)
    with cd('/opt/mongo'):
        sudo('dpkg -i mongodb-mms-automation-agent-manager.deb')

