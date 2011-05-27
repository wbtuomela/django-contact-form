class OrderableFormMixin(object):
    """
    Form mixin class which allows for reordering and hiding fields for normal
    forms, similar to the way this is possible with ModelForms::
    
        class MyFunkyForm(OrderableFormMixin, Form):
            class Meta:
                fields = ('my_field1', 'my_field2')

    """

    def __init__(self, *args, **kwargs):
        super(OrderableFormMixin, self).__init__(*args, **kwargs)
        
        # Get the Meta class, if available
        meta_class = getattr(self, 'Meta', None)
        if meta_class:
            fields_list = getattr(meta_class, 'fields', None)
            
            if fields_list:
                self.fields.keyOrder = fields_list
