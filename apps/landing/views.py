from django.shortcuts import redirect, render
from .forms import ContactForm

def main(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ContactForm()
    return render(request, 'landing/index.html', {'form':form})
