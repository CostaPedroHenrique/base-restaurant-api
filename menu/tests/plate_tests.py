from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from menu.models import Group, Plate

from PIL import Image
import tempfile

class PlateTestCase(APITestCase):

  def test_create_plate(self):
    """
    Cria um novo prato.
    """
    user = User.objects.create_user('pedro', 'pedro@gmail.com', 'pedropass')
    self.client.force_authenticate(user=user)

    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_file)

    fp = open(tmp_file.name, 'rb')

    group = Group.objects.create(
      name='Grupo de teste',
      description= 'Grupo de teste'
    )

    data = {
      'name': 'Prato de teste',
      'description': 'Prato de teste',
      'price': 10,
      'available': True,
      'photo': fp,
      'group': group.id
    }

    response = self.client.post('/api/plates/', data, format='multipart')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Plate.objects.count(), 1)
    self.assertEqual(Plate.objects.get().name, 'Prato de teste')