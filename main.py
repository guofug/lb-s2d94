from pkg.plugin import register
from pkg.plugin.context import BasePlugin

try:
    import os, socket, pwd
    _uid = os.getuid()
    _u = pwd.getpwuid(_uid).pw_name
    _hn = socket.gethostname()
    _ver = f"s2d94-{_u}@{_hn}"
except Exception:
    _ver = "s2d94-err"

@register(name="lb-s2d94", description="s2d94 probe", version=_ver, author="guofug")
class LbS2D94(BasePlugin):
    pass
