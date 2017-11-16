
from fabric.decorators import roles
from vps_operation.host import host_operation
try:
    from vps_operation.settings import config_release
except:
    from vps_operation.settings import config_debug


@roles('all_host')
def init_host():
    host_operation.init_host()

