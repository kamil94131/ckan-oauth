import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.types import Context
from typing import Any

from ckanext.keycloak.views import get_blueprint
from ckanext.keycloak import helpers as h
import ckan.plugins as p
ignore_empty = p.toolkit.get_validator('ignore_empty')
unicode_safe = p.toolkit.get_validator('unicode_safe')


class KeycloakPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IResourceView, inherit=True)

    # IConfigurer

    def update_config(self, config_):
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
    
    def info(self) -> 'dict[str, Any]':
        return {'name': 'test1',
                'title': p.toolkit._('Website'),
                'schema': {'page_url': [ignore_empty, unicode_safe]},
                'iframed': False,
                'icon': 'link',
                'always_available': True,
                'default_title': p.toolkit._('Website'),
                }

    def view_template(self, context: Context, data_dict: 'dict[str, Any]'):
        return 'user/test1.html'

    def form_template(self, context: Context, data_dict: 'dict[str, Any]'):
        return 'user/test1.html'
