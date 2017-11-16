
from fabric.api import sudo
from fabric.decorators import roles


def init_host():
    sudo('apt-get update')
    sudo('apt-get -y install software-properties-common python-software-properties')
    sudo('add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"')
    sudo('apt-get update')

    # python3
    sudo('apt-get -y install python3-pip')
    sudo('ln -s -b /usr/bin/python3 /usr/bin/python')
    sudo('ln -s -b /usr/bin/pip3 /usr/bin/pip')
    sudo('export LC_ALL=C')
    sudo('pip install setuptools wheel')
    sudo('apt-get -y install gcc python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev')

    # docker
    sudo('apt-get -y install \
     linux-image-extra-virtual')
    # sudo('apt-get -y install \
    #  linux-image-extra-$(uname -r) \
    #  linux-image-extra-virtual')
    sudo('apt-get -y install \
     apt-transport-https \
     ca-certificates \
     curl \
     software-properties-common')
    sudo('apt-get -y --allow-unauthenticated install docker-ce')

    # docker-compose
    sudo('curl -L "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname -s)-$(uname -m)" '
        '-o /usr/local/bin/docker-compose')
    sudo('chmod +x /usr/local/bin/docker-compose')

    #utils
    sudo('apt-get -y install htop')
    sudo('echo "export C_FORCE_ROOT=true" >> ~/.bashrc')
    sudo('echo "export LC_ALL=C" >> ~/.bashrc')
    sudo('echo "alias g=\'ps aux|grep\'" >> ~/.bashrc')
    sudo('echo "alias f=\'tailf\'" >> ~/.bashrc')

def update_etc_hosts(content):
    sudo('printf "{}" >> /etc/hosts'.format(content))

def run_command(command, use_sudo=True):
    run(command, use_sudo=use_sudo)