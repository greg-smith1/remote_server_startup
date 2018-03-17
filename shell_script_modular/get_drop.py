import os

def create_droplet(name):
    os.system(curl -X POST "https://api.digitalocean.com/v2/droplets" -d'{"name":"{name}","region":"nyc1","size":"s-1vcpu-1gb","image":"ubuntu-16-04-x64", "ssh_keys":["30:7a:78:55:04:99:f6:a2:2d:b2:08:6f:79:cd:99:06"]}' -H "Authorization: Bearer a7bcb6921f712c20e0641c9b408d31af3de4c8be255e3868576c2d86ab272e1e" -H "Content-Type: application/json")
    return 'All done'


create_droplet(input('Please name your server: '))