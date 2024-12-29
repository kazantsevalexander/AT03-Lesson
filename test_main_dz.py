import pytest
from main_dz import get_random_cat_image

def test_get_random_cat_image_success(mocker):
   mock_get = mocker.patch('main_dz.requests.get')
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = [{
       "id": "72t",
       "url": "https://cdn2.thecatapi.com/images/72t.jpg",
       "width": 500,
       "height": 375
   }]

   user_data = get_random_cat_image()
   assert user_data == "https://cdn2.thecatapi.com/images/72t.jpg"

def test_get_random_cat_image_with_error(mocker):
   mock_get = mocker.patch('main_dz.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_random_cat_image()
   assert user_data == None