# cython: language_level=3, boundscheck=False, wraparound=False, cdivision=True

cdef:
    char* __version__
    tuple __all__
    char* default_cipher_key
    object cipher


cdef object init_cookie_session(object cookie, object response_headers)
    # pass
