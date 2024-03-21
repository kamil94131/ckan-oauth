import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.keycloak.views import get_blueprint
from ckanext.keycloak import helpers as h
import ckan.plugins as p
import logging
from flask import Flask

app = Flask(__name__)

ignore_empty = p.toolkit.get_validator('ignore_empty')
unicode_safe = p.toolkit.get_validator('unicode_safe')


class KeycloakPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):

        app.logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(stream_handler)

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'keycloak')

    def get_blueprint(self):
        return get_blueprint()
  
    # ITemplateHelpers

    def get_helpers(self):
        return {
            'button_style': h.button_style,
            'enable_internal_login': h.enable_internal_login,
        }