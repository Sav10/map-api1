import sys, os
INTERP = "/var/www/myappfalcon1/code/flaskproject27/local/bin/python"
#INTERP is present twice so that the new python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)
from app import api as application