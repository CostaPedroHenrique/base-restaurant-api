from django.contrib.auth.models import User
from menu.models import Group
from rest_framework import status
from rest_framework.test import APITestCase

from PIL import Image
import tempfile


class GroupTestCase(APITestCase):
    """
    Testes da entidade grupo.
    """
    def test_create_group(self):
        """
        Deve criar um novo grupo.
        """
        user = User.objects.create_user('pedro', 'pedro@gmail.com', 'pedropass')
        self.client.force_authenticate(user=user)

        # Create image
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)

        fp = open(tmp_file.name, 'rb')

        data = {
          'name': 'Grupo de teste',
          'description': 'Grupo de teste',
          'icon': fp
        }
        response = self.client.post('/api/groups/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Group.objects.count(), 1)
        self.assertEqual(Group.objects.get().name, 'Grupo de teste')
