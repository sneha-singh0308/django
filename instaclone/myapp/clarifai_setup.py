from clarifai.rest import ClarifaiApp
from myapp.models import PostModel

def get_keywords():

    app = ClarifaiApp(api_key="a1924afdfb1b45c0b04f1217c9183f0f")

    model = app.models.get("general-v1.3")
    response = model.predict_by_url(url=PostModel.image_url)
    return response