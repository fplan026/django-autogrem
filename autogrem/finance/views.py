from typing import Any
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView

from .forms import NewBill
from .models import Bill

class IndexView(ListView):    
    """Extend the generic ListView view to take advantage of django's
    abstraction of the concept of “display a list of objects.”

    This means we can skip the overhead of writing a million methods like
    this:
    
    def index(request):
    try:
        objects = MyObject.objects.all()
    except Exception:
        raise Http404("MyObject does not exist")
    return render(request, "myapp/index.html", {"objects": objects})
    """
    
    # let django know what to render
    template_name = "finance/index.html"
    
    # the ListView superclass will call get_queryset() automatically
    # this variable is what we will name the variable we pass to our template
    # see autogrem/finance/templates/finance/index.html to see how we use it
    context_object_name = "expenses"
    
    paginate_by=10

    def get_queryset(self) -> QuerySet[Any]:
        return Bill.objects.all().order_by("name")

class RecurringBillDetailsView(DetailView):
    model = Bill
    template_name = "finance/bill_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

def new_bill(request):
    user = User.objects.first() # TODO: get the logged in user!
    
    if request.method == 'POST':
        form = NewBill(request.POST)
        if form.is_valid():
            bill = form.save()
            # go back to the finance home page
            return HttpResponseRedirect(reverse('finance:index'))
    else:
        form = NewBill()
    return render(request, 'finance/new_bill.html', {'form': form})