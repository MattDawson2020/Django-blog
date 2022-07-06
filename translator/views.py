from pydoc import html
from django.shortcuts import render
from .translate import translate

# Create your views here.
def translator_view(request: str) -> str:
    if request.method == "POST":
        text = request.POST['input_text']
        output = translate(text)
        return render(request, 'translator.html', {'output_text': output, 'original_text': text})
    else:

        return render(request, 'translator.html')
