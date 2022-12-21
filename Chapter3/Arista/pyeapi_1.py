import pyeapi
import pprint
#show command
arista1 = pyeapi.connect_to('Arista1')
pprint.pprint(arista1.enable('show hostname'))

#config command, change hostname
arista1.config('hostname arista1-new')
pprint.pprint(arista1.enable('show hostname'))
