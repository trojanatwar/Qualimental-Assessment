from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .model import DBSession, Base

from pyramid_heroku import expandvars_dict

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

def main(global_config, **settings):  # pylint: disable=unused-argument
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    
    settings = expandvars_dict(settings)
    config = Configurator(settings=settings,
                          root_factory='.model.Root')

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config.include("pyramid_openapi3")
    config.pyramid_openapi3_spec("openapi.yaml", route="/openapi.yaml")
    config.pyramid_openapi3_add_explorer(route="/docs")


    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('wiki_view', '/wiki_view/{uid}')
    

    config.scan()
    return config.make_wsgi_app()
