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
from .models import RecurringBill


# def index(request):
#     expenses = RecurringBill.objects.all()
#     return render(request, 'finance/index.html', {'expenses': expenses})

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
    
    paginate_by=5

    def get_queryset(self) -> QuerySet[Any]:
        return RecurringBill.objects.all()

class RecurringBillDetailsView(DetailView):
    model = RecurringBill
    template_name = "finance/recurring_bill_detail.html"

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

# ...
# def vote(request, question_id):
#     bill = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = bill.choice_set.get(pk=request.POST["choice"])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(
#             request,
#             "polls/detail.html",
#             {
#                 "question": bill,
#                 "error_message": "You didn't select a choice.",
#             },
#         )
#     else:
#         selected_choice.votes = F("votes") + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse("polls:results", args=(bill.id,)))