
cdef:
    char* __version__
    tuple __all__
    char* default_cipher_key
    object cipher


cdef object init_cookie_session(object cookie, object response_headers)
    # pass
