# import urllib = library for url
# use urllib.request to get the data from the url
# a function that takes a urls and returns a response

import urllib.request as urllib

def main(url):
    print('Checking connectivity ...')
    
    response = urllib.urlopen(url)
    print('Connected to', url, 'successfully')
    print('The responce code was', response.getcode())
    
     
print('This sis a site connectividty checker program (0_0)')
input_url = input('Input the url of dthe sote you want to check: ')
    
main(input_url)