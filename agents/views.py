from django.shortcuts import render, reverse
from django.views import generic
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        return Agent.objects.all()

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')