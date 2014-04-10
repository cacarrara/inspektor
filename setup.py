# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat 2013-2014
# Author: Lucas Meneghel Rodrigues <lmr@redhat.com>

from distutils.core import setup

import inspektor.version

setup(name='inspektor',
      version=inspektor.version.VERSION,
      description='Inspektor code checker',
      author='Lucas Meneghel Rodrigues',
      author_email='lmr@redhat.com',
      url='http://autotest.github.com',
      packages=['inspektor',
                'inspektor.cli',
                'inspektor.utils'
                ],
      scripts=['scripts/inspekt'],
      data_files=[('/usr/share/inspektor/data', ['data/LICENSE_SNIPPET_GPLV2']),
                  ('/usr/share/inspektor/data', ['data/LICENSE_SNIPPET_GPLV2_STRICT'])],
      )
