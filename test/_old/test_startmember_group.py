#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#  Copyright (C) 2009-2014:
#     Jean Gabes, naparuba@gmail.com
#     Hartmut Goebel, h.goebel@goebel-consult.de
#     Grégory Starck, g.starck@gmail.com
#     Sebastien Coavoux, s.coavoux@free.fr

#  This file is part of Shinken.
#
#  Shinken is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Shinken is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

#
# This file is used to test reading and processing of config files
#

from alignak_test import *


class TestStarMemberGroup(AlignakTest):
    def setUp(self):
        self.setup_with_file(['etc/alignak_startmember_group.cfg'])

    # Check if service apply on a hostgroup * is good or not
    def test_starmembergroupdef(self):
        hg = self.sched.conf.hostgroups.find_by_name('ping-servers')
        self.assertIsNot(hg, None)
        print hg.members
        h = self.sched.conf.hosts.find_by_name('test_host_0')
        r = self.sched.conf.hosts.find_by_name('test_router_0')
        self.assertIn(h.uuid, hg.members)
        self.assertIn(r.uuid, hg.members)

        s = self.sched.conf.services.find_srv_by_name_and_hostname('test_host_0', 'PING')
        self.assertIsNot(s, None)


if __name__ == '__main__':
    unittest.main()
