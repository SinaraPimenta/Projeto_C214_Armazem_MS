#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")
#use_plugin("python.requests")
#use_plugin("python.beautifulsoup4")
#use_plugin("python.flask")
#use_plugin("python.pymongo")
#use_plugin("python.dnspython")

name = "Armazem_MS"
#default_task = "publish"
default_task = ['install_dependencies', 'publish']


#@init
#def set_properties(project):
 #  pass

@init
def initialize(project):
    project.build_depends_on('requests')
    project.build_depends_on('flask')
    project.build_depends_on('pymongo')
    project.build_depends_on('dnspython')
    project.build_depends_on('beautifulsoup4')

@init
def set_properties(project):
    pass