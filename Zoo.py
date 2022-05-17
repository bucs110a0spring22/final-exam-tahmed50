import requests

class ZooAPI:
  def __init__(self):
    self.api_url = "https://zoo-animal-api.herokuapp.com/animals/rand"

  def get(self):
    response = requests.get(self.api_url)
    return response.json()

  def __str__(self):
    response = self.get()
    
    return f"Name of the animal is {response['name']}, minimum length is {response['length_min']} ft, maximum length is {response['length_max']} ft, minimum weight is {response['weight_min']} pounds, maximum weight is {response['weight_max']} pounds, average life span is {response['lifespan']} years, click this link to see an image of the {response['name']}, {response['image_link']}"
