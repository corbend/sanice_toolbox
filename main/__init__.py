import os
import anyconfig


PROJECT_DIR = os.path.dirname(__file__)

base_conf = anyconfig.open(
	os.path.join(PROJECT_DIR, 'config', 'base.yml'), ac_parser='yaml')
local_conf = anyconfig.load(
	[base_conf, os.path.join(PROJECT_DIR, 'config', 'local.yml')], 
	ac_parser='yaml', ignore_missing=True)

conf = local_conf
