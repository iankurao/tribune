from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

#test our editor module
class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.ian= Editor(first_name = 'Ian', last_name ='Kurao', email ='kuraoian@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ian,Editor))
         # Testing Save Method
    def test_save_method(self):
        self.ian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.ian.delete_editor()
        editors = Editor.objects.filter(id = 2).delete()
        self.assertTrue(len(editors) > 0)  

    