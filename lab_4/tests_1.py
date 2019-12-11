from django.urls import reverse
from django.urls import reverse_lazy
##from django.core.urlresolvers import reverse_lazy
from django.test import TestCase
from djangoapp import models

class TestCalls(TestCase):
    def setUp(self):
        self.create_url = 'create_measurement'
        self.list_url = 'measurement_list'
    def test_call_view_loads(self):
        for url in [self.create_url, self.list_url]:
            path = str(reverse_lazy(url))
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)   ## proverka na poluchenyi status cod, proverka otveta na zapros, proverka po usloviyu 
            self.assertTemplateUsed(response, '{}.html'.format(url))## proverka shablona pri rendere otveta 
            
    def test_call_view_fails_blank(self):
        path = str(reverse_lazy(self.create_url))
        response = self.client.post(path, {})
        self.assertFormError(response, 'form', 'value',
                             u'This field is required.') ## proverka na otpravku pustih poley, dogen vernut` oshibku
        
    def test_call_view_fails_incorrect(self):
        path = str(reverse_lazy(self.create_url))
        value = '1'*51
        measurement_params = {
            'value': value,
        }
        response = self.client.post(path, measurement_params)
        self.assertFormError(response, 'form', 'value', u'Ensure this value has at most 50 characters (it has 51).') ##proverka povedenie formy pri nekorectnyh dannih,
                                                                                                                     ##dogen vernut` oshibku, menee 50 symvolov
