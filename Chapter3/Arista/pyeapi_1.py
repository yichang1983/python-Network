import pyeapi
import pprint

arista1 = pyeapi.connect_to('Arista1')
pprint.pprint(arista1.enable('show hostname'))
