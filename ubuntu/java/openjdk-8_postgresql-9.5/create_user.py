#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import os

user = os.environ['USER'] 
child = pexpect.spawnu("su - postgres -c 'createuser -dilPrS {}'".format(user))

child.expect('(?i)Enter password for new role:')
child.sendline(user)
child.expect('(?i)Enter it again:')
child.sendline(user)
