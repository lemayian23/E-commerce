import warnings
import ecommerce.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "ecommerce.service.wsgi_server.application to ecommerce.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return ecommerce.http.root(environ, start_response)
