from django import forms
from collections import OrderedDict


class BaseForm(forms.Form):
    ordered_field_names = []
    disabled_fields = []

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.rearrange_field_order()

    def rearrange_field_order(self):

        if len(self.ordered_field_names) == 0:
            return

        original_fields = self.fields
        new_fields = OrderedDict()

        for field_name in self.ordered_field_names:
            field = original_fields.get(field_name)
            if field:
                new_fields[field_name] = field

        self.fields = new_fields
    
    def disable_fields(self):
        for field in self.disabled_fields:
            self.fields[field].widget.attrs['disabled'] = True
