from django.shortcuts import render
from django.views import generic
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        return Agent.objects.all()