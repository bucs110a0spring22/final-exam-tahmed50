import requests

class FoxAPI:
  def __init__(self):
    self.api_url = "https://randomfox.ca/floof/"

  def get(self):
    response = requests.get(self.api_url)
    return response.json()

  def __str__(self):
    response = self.get()

    return f"Hope this image of a fox makes your day 10 times better :){response['link']} click the link please." 
    
