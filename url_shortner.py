from hashlib import sha256
import pickle
import os

def shorten(url:str, shortened_url_dict:dict):
    '''A function to hash the url to 6 digit hash. If the url is already in the dictionary, 
    return the next hash.

    Args:
        url: the url to be hashed
    
    Returns:
        the hashed shortened url
    '''
    #if url already in the dictionary, return the shorted url
    if url in shortened_url_dict.keys():
        return shortened_url_dict[url]

    #create new shortened url if the url is not in the dictionary
    salt = str(os.urandom(16))
    shortened_url = sha256((url+salt).encode()).hexdigest()[:6]
    while shortened_url in shortened_url_dict.values():
        shortened_url = hex(int(shortened_url,16)+1)[:6]
    
    #save the shortened url in the dictionary
    shortened_url_dict[url] = shortened_url
    return shortened_url
    

def restore(shortened_url, shortened_url_dict):
    '''A function to restore the url from the short url

    Args:
        shortened_url: the short url
    
    Returns:
        the original url
    '''
    if shortened_url not in shortened_url_dict.values():
        return None

    for k, v in shortened_url_dict.items():
        if v == shortened_url:
            return k


#Do not change the main function
def main():
    '''The main function
    '''

    try:
        with open('shortened_url_dict.pkl', 'rb') as f:
            shortened_url_dict = pickle.load(f)
    except FileNotFoundError as e:
        shortened_url_dict = {}

    print(shorten("www.google.com", shortened_url_dict))
    print(shorten("www.msn.com", shortened_url_dict))
    print(shorten("www.yahoo.com", shortened_url_dict))
    #if the user enters same long url multiple times then same short url must be generated
    print(shorten("www.googlemail.com", shortened_url_dict))
    print(shorten("www.googlemail.com", shortened_url_dict))
    print(restore("zLg6wl", shortened_url_dict)) #this should return None
    
    with open('shortened_url_dict.pkl', 'wb') as f:
        pickle.dump(shortened_url_dict, f)


if __name__ == "__main__":
    main()