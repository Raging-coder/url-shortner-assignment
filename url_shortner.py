from hashlib import sha256
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
    print(shorten("www.googlemail.com", shortened_url_dict))
    print(restore("zLg6wl", shortened_url_dict)) #this should return None
    
    with open('shortened_url_dict.pkl', 'wb') as f:
        pickle.dump(shortened_url_dict, f)


if __name__ == "__main__":
    main()
