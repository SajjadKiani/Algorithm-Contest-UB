from django.views.generic import (
    ListView,
    CreateView,
)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Contact, Team
from blog.models import Post


# Create your views here.


class IndexView(ListView):
    model = Team
    template_name = "website/index.html"
    context_object_name = "teams"

    def get_queryset(self):
        # return all the Team objects
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-created_date")[:6]
        context.update(
            {
                "posts": posts,
            }
        )
        return context

class CreateTeam(SuccessMessageMixin, CreateView):
    model = Team
    template_name = "website/register.html"
    success_url = reverse_lazy("website:index")
    
    fields = [
        "team_name",
        "university",
        "language",
        # person 1
        "first_name1",
        "last_name1",
        "gender1",
        "phone1",
        "email1",
        "education1",
        "student_number1",
        # person 2
        "first_name2",
        "last_name2",
        "gender2",
        "phone2",
        "email2",
        "education2",
        "student_number2",
        # person 3
        "first_name3",
        "last_name3",
        "gender3",
        "phone3",
        "email3",
        "education3",
        "student_number3",
        "agree",
    ]
    success_message = ".تیم شما با موفقیت ثبت شد. لطفا برای پرداخت هزینه ورودی به اطلاعیه ها مراجعه کنید "
    def form_valid(self, form):
        return super().form_valid(form)


class ContactView(CreateView):
    model = Contact
    template_name = "website/contact.html"
    success_url = reverse_lazy("website:index")
    # form_class = CreateContactForm
    fields = [
        "name",
        "email",
        "subject",
        "message",
    ]

    def form_valid(self, form):
        return super().form_valid(form)

class TermsView(ListView):

    model = Team
    template_name = "website/terms.html"
    context_object_name = "teams"

    def get_queryset(self):
        # return all the Team objects
        return self.model.objects.all()
    
class CountdownView(ListView):

    model = Team
    template_name = "website/countdown.html"
    context_object_name = "teams"

    def get_queryset(self):
        # return all the Team objects
        return self.model.objects.all()
    