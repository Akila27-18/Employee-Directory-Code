from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm

class HRPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='HR').exists()

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'directory/employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        department = self.request.GET.get('department')
        if department:
            return Employee.objects.filter(department__name=department)
        return Employee.objects.all()

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'directory/employee_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = [
            {'name': 'Home', 'url': reverse_lazy('employee_list')},
            {'name': self.object.name, 'url': ''}
        ]
        return context

class EmployeeCreateView(LoginRequiredMixin, HRPermissionMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'directory/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(LoginRequiredMixin, HRPermissionMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'directory/employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(LoginRequiredMixin, HRPermissionMixin, DeleteView):
    model = Employee
    template_name = 'directory/employee_form.html'
    success_url = reverse_lazy('employee_list')
