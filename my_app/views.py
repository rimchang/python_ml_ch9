from django.shortcuts import render
from django.views.generic.base import View
from forms import ReviewForm
# Create your views here.
from .movieclassfier.movie_model import classify,train
from .models import result

class review(View):
    
    def get(self,request):
        form=ReviewForm()
        return render(request,'review_form.html',{'form':form})
        
    def post(self,request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.data['review']
            y,prob = classify(review)
            return render(request,'result.html',{'review': review,'y':y,'prob':prob})

from django.views.decorators.csrf import csrf_exempt


class feedback(View):
    
    @csrf_exempt
    def post(self,request):
        feedback=request.POST['feedback_button']
        review=request.POST['review']
        prediction=request.POST['prediction']
        
        inv_label={'negative':0,'positive':1}
        y=inv_label[prediction]
        if feedback == 'Incorrcet':
            y=int(not(y))
        train(review,y)
        
        result1=result()
        result1.review = review
        result1.prediction = int(inv_label[prediction])
        result1.sentiment = int(y)
        result1.save()
        
        return render(request,'thanks.html')
    