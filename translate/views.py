from django.http import HttpResponse
from django.shortcuts import render
from transformers import AutoTokenizer
from transformers import TFAutoModelForSeq2SeqLM
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
model = TFAutoModelForSeq2SeqLM.from_pretrained("./tf_model/")


# Create your views here.
def index(request):
    return render(request, "index.html", {})

def getResponse(request):
    message = request.GET.get("userMessage")
    try:
        tokenized = tokenizer([message], return_tensors='np')
        out = model.generate(**tokenized, max_length=128)

        with tokenizer.as_target_tokenizer():
            message = tokenizer.decode(out[0], skip_special_tokens=True)
    except Exception as e:
        print(e) 
    return HttpResponse(message)