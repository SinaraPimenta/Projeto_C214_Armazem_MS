#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.requests")
use_plugin("python.beautifulsoup4")
use_plugin("python.flask")

name = "Armazem_MS"
default_task = "publish"


@init
def set_properties(project):
    pass
