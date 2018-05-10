from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://ec2-54-149-169-53.us-west-2.compute.amazonaws.com/get_data.php' # Set destination URL here
post_fields = {'gate_open': '1', 'vehicle_pass' : '0'}     # Set POST fields here

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()
print(json)
