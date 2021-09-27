from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('tonnikala.pyramid')
        config.include('.routes')
        config.include('.models')
        config.include('.auth')
        config.add_tonnikala_extensions('tk')
        config.scan()

    return config.make_wsgi_app()
