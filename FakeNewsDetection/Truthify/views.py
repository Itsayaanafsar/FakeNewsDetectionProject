from django.shortcuts import render
from django.http import HttpResponse
import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Create your views here.

def home(request):
    if request.method == "POST":
        news = request.POST.get("news")

        transformed = vectorizer.transform([news])
        prediction = model.predict(transformed)[0]

        result = "Real" if prediction == 0 else "Fake"

        return render(request, "index.html", {"result": result})

    return render(request, "index.html")

