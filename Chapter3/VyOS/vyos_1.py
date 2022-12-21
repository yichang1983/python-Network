#!/usr/bin/env python

import vymgmt

vyos = vymgmt.Router('192.168.17.24', 'test', password='test')
vyos.login()
vyos.configure()
vyos.set("hostname R1")
vyos.commit()
vyos.save()
vyos.exit()
vyos.logout()
exit()