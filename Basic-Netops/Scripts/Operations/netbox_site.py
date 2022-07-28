
import pynetbox
import json

nb = pynetbox.api('https://demo.netbox.dev',token='4fb4bf0e9d3b937aec9037ecb8022ca77c9f19b2')
sites = nb.dcim.sites.all()
site_list = list(sites)
print(site_list)