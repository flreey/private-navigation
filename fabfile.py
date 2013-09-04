# -*- coding:utf-8 -*- 

from fabric.api import *
env.hosts = ['192.155.92.136']
env.user = 'root'

def d():
	with cd('/var/www/private-navigation'):
		run('git pull')
		run('pkill -9 uwsgi')
