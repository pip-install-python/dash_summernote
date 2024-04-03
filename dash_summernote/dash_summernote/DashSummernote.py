# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSummernote(Component):
    """A DashSummernote component.


Keyword arguments:

- id (string; optional)

- height (number; optional)

- toolbar (list; optional)

- value (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_summernote'
    _type = 'DashSummernote'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, toolbar=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'height', 'toolbar', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'height', 'toolbar', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashSummernote, self).__init__(**args)
