from hashlib import sha256
import pickle
import os

def shorten(url:str, shortened_url_dict:dict)-> str:
    '''A function to hash the url to 6 digit hash. If the url is already in the dictionary, 
    return the next hash.

    Args:
        url: the original long url to be shortned (hashed)
        shortened_url_dict: a dictionary containing mapping of long urls to their short urls
    
    Returns:
        the hashed shortened url in hexadecimal of length 6
    '''
    shortened_url = None
    
    #TODO: if url already in the dictionary, return the shortened url
    
    
    #salt is to add randomization to the string before hashing
    salt = str(os.urandom(16))
    
    #TODO: create new shortened url in hexadecimal if the url is not in the dictionary
    #shortened_url = ???
    
    
    #TODO: if the url is already in shortened_url_dict then add 1 to generated shortened url and continue rechecking till a shortened url is found
    #that is not in shortened_url_dict
    
    
    #TODO: save the shortened url in the dictionary
    #shortened_url_dict[url] = ???
    
    
    return shortened_url
 

def restore(shortened_url, shortened_url_dict):
    '''A function to restore the long url from the short url

    Args:
        shortened_url: the short url
        shortened_url_dict: a dictionary containing mapping of long urls to their short urls
    
    Returns:
        the original long url
    '''
    
    # TODO: if the short url is not present in shortened_url_dict then return None
    

    # TODO: if the short url is present in shortened_url_dict then return the corresponding long url
    
    
    # TODO: Delete next line
    pass
