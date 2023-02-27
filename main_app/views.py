from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, TemplateView
from main_app.models import *
from main_app.forms import *
class Index(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		return context


class BASIC_STRUCTURE_CREATEVIEW(CreateView):
	template_name = 'BASIC_STRUCTURE_create.html'
	model = BASIC_STRUCTURE
	
	form_class = BASIC_STRUCTURE_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_STRUCTURE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class FULL_CODE_CREATEVIEW(CreateView):
	template_name = 'FULL_CODE_create.html'
	model = FULL_CODE
	
	form_class = FULL_CODE_MF
	
	def get_context_data(self, **kwargs):
		context = super(FULL_CODE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_CATEGO_CREATEVIEW(CreateView):
	template_name = 'RB_CATEGO_create.html'
	model = RB_CATEGO
	
	form_class = RB_CATEGO_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_CATEGO_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_SUBC_CREATEVIEW(CreateView):
	template_name = 'RB_SUBC_create.html'
	model = RB_SUBC
	
	form_class = RB_SUBC_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_SUBC_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_TYPE_CREATEVIEW(CreateView):
	template_name = 'RB_TYPE_create.html'
	model = RB_TYPE
	
	form_class = RB_TYPE_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_TYPE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class C_CATEGO_CREATEVIEW(CreateView):
	template_name = 'C_CATEGO_create.html'
	model = C_CATEGO
	
	form_class = C_CATEGO_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_CATEGO_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class C_SUBC_CREATEVIEW(CreateView):
	template_name = 'C_SUBC_create.html'
	model = C_SUBC
	
	form_class = C_SUBC_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_SUBC_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class C_TYPE_CREATEVIEW(CreateView):
	template_name = 'C_TYPE_create.html'
	model = C_TYPE
	
	form_class = C_TYPE_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_TYPE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class COMPONENT_CREATEVIEW(CreateView):
	template_name = 'COMPONENT_create.html'
	model = COMPONENT
	
	form_class = COMPONENT_MF
	
	def get_context_data(self, **kwargs):
		context = super(COMPONENT_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class ROBOT_CREATEVIEW(CreateView):
	template_name = 'ROBOT_create.html'
	model = ROBOT
	
	form_class = ROBOT_MF
	
	def get_context_data(self, **kwargs):
		context = super(ROBOT_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class CODE_CREATEVIEW(CreateView):
	template_name = 'CODE_create.html'
	model = CODE
	
	form_class = CODE_MF
	
	def get_context_data(self, **kwargs):
		context = super(CODE_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_LIBRARY_CREATEVIEW(CreateView):
	template_name = 'BASIC_LIBRARY_create.html'
	model = BASIC_LIBRARY
	
	form_class = BASIC_LIBRARY_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_LIBRARY_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_COMP_CREATEVIEW(CreateView):
	template_name = 'BASIC_COMP_create.html'
	model = BASIC_COMP
	
	form_class = BASIC_COMP_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_COMP_CREATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_STRUCTURE_LISTVIEW(ListView):
	template_name = 'BASIC_STRUCTURE_list.html'
	model = BASIC_STRUCTURE
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_STRUCTURE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class FULL_CODE_LISTVIEW(ListView):
	template_name = 'FULL_CODE_list.html'
	model = FULL_CODE
	
	def get_context_data(self, **kwargs):
		context = super(FULL_CODE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class RB_CATEGO_LISTVIEW(ListView):
	template_name = 'RB_CATEGO_list.html'
	model = RB_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(RB_CATEGO_LISTVIEW, self).get_context_data(**kwargs)
		return context

class RB_SUBC_LISTVIEW(ListView):
	template_name = 'RB_SUBC_list.html'
	model = RB_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(RB_SUBC_LISTVIEW, self).get_context_data(**kwargs)
		return context

class RB_TYPE_LISTVIEW(ListView):
	template_name = 'RB_TYPE_list.html'
	model = RB_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(RB_TYPE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class C_CATEGO_LISTVIEW(ListView):
	template_name = 'C_CATEGO_list.html'
	model = C_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(C_CATEGO_LISTVIEW, self).get_context_data(**kwargs)
		return context

class C_SUBC_LISTVIEW(ListView):
	template_name = 'C_SUBC_list.html'
	model = C_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(C_SUBC_LISTVIEW, self).get_context_data(**kwargs)
		return context

class C_TYPE_LISTVIEW(ListView):
	template_name = 'C_TYPE_list.html'
	model = C_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(C_TYPE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class COMPONENT_LISTVIEW(ListView):
	template_name = 'COMPONENT_list.html'
	model = COMPONENT
	
	def get_context_data(self, **kwargs):
		context = super(COMPONENT_LISTVIEW, self).get_context_data(**kwargs)
		return context

class ROBOT_LISTVIEW(ListView):
	template_name = 'ROBOT_list.html'
	model = ROBOT
	
	def get_context_data(self, **kwargs):
		context = super(ROBOT_LISTVIEW, self).get_context_data(**kwargs)
		return context

class CODE_LISTVIEW(ListView):
	template_name = 'CODE_list.html'
	model = CODE
	
	def get_context_data(self, **kwargs):
		context = super(CODE_LISTVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_LIBRARY_LISTVIEW(ListView):
	template_name = 'BASIC_LIBRARY_list.html'
	model = BASIC_LIBRARY
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_LIBRARY_LISTVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_COMP_LISTVIEW(ListView):
	template_name = 'BASIC_COMP_list.html'
	model = BASIC_COMP
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_COMP_LISTVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_STRUCTURE_UPDATEVIEW(UpdateView):
	template_name = 'BASIC_STRUCTURE_update.html'
	model = BASIC_STRUCTURE
	
	form_class = BASIC_STRUCTURE_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_STRUCTURE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class FULL_CODE_UPDATEVIEW(UpdateView):
	template_name = 'FULL_CODE_update.html'
	model = FULL_CODE
	
	form_class = FULL_CODE_MF
	
	def get_context_data(self, **kwargs):
		context = super(FULL_CODE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_CATEGO_UPDATEVIEW(UpdateView):
	template_name = 'RB_CATEGO_update.html'
	model = RB_CATEGO
	
	form_class = RB_CATEGO_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_CATEGO_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_SUBC_UPDATEVIEW(UpdateView):
	template_name = 'RB_SUBC_update.html'
	model = RB_SUBC
	
	form_class = RB_SUBC_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_SUBC_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class RB_TYPE_UPDATEVIEW(UpdateView):
	template_name = 'RB_TYPE_update.html'
	model = RB_TYPE
	
	form_class = RB_TYPE_MF
	
	def get_context_data(self, **kwargs):
		context = super(RB_TYPE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class C_CATEGO_UPDATEVIEW(UpdateView):
	template_name = 'C_CATEGO_update.html'
	model = C_CATEGO
	
	form_class = C_CATEGO_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_CATEGO_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class C_SUBC_UPDATEVIEW(UpdateView):
	template_name = 'C_SUBC_update.html'
	model = C_SUBC
	
	form_class = C_SUBC_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_SUBC_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class C_TYPE_UPDATEVIEW(UpdateView):
	template_name = 'C_TYPE_update.html'
	model = C_TYPE
	
	form_class = C_TYPE_MF
	
	def get_context_data(self, **kwargs):
		context = super(C_TYPE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class COMPONENT_UPDATEVIEW(UpdateView):
	template_name = 'COMPONENT_update.html'
	model = COMPONENT
	
	form_class = COMPONENT_MF
	
	def get_context_data(self, **kwargs):
		context = super(COMPONENT_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class ROBOT_UPDATEVIEW(UpdateView):
	template_name = 'ROBOT_update.html'
	model = ROBOT
	
	form_class = ROBOT_MF
	
	def get_context_data(self, **kwargs):
		context = super(ROBOT_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class CODE_UPDATEVIEW(UpdateView):
	template_name = 'CODE_update.html'
	model = CODE
	
	form_class = CODE_MF
	
	def get_context_data(self, **kwargs):
		context = super(CODE_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_LIBRARY_UPDATEVIEW(UpdateView):
	template_name = 'BASIC_LIBRARY_update.html'
	model = BASIC_LIBRARY
	
	form_class = BASIC_LIBRARY_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_LIBRARY_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_COMP_UPDATEVIEW(UpdateView):
	template_name = 'BASIC_COMP_update.html'
	model = BASIC_COMP
	
	form_class = BASIC_COMP_MF
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_COMP_UPDATEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_STRUCTURE_DETAILVIEW(DetailView):
	template_name = 'BASIC_STRUCTURE_detail.html'
	model = BASIC_STRUCTURE
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_STRUCTURE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class FULL_CODE_DETAILVIEW(DetailView):
	template_name = 'FULL_CODE_detail.html'
	model = FULL_CODE
	
	def get_context_data(self, **kwargs):
		context = super(FULL_CODE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class RB_CATEGO_DETAILVIEW(DetailView):
	template_name = 'RB_CATEGO_detail.html'
	model = RB_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(RB_CATEGO_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class RB_SUBC_DETAILVIEW(DetailView):
	template_name = 'RB_SUBC_detail.html'
	model = RB_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(RB_SUBC_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class RB_TYPE_DETAILVIEW(DetailView):
	template_name = 'RB_TYPE_detail.html'
	model = RB_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(RB_TYPE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class C_CATEGO_DETAILVIEW(DetailView):
	template_name = 'C_CATEGO_detail.html'
	model = C_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(C_CATEGO_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class C_SUBC_DETAILVIEW(DetailView):
	template_name = 'C_SUBC_detail.html'
	model = C_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(C_SUBC_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class C_TYPE_DETAILVIEW(DetailView):
	template_name = 'C_TYPE_detail.html'
	model = C_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(C_TYPE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class COMPONENT_DETAILVIEW(DetailView):
	template_name = 'COMPONENT_detail.html'
	model = COMPONENT
	
	def get_context_data(self, **kwargs):
		context = super(COMPONENT_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class ROBOT_DETAILVIEW(DetailView):
	template_name = 'ROBOT_detail.html'
	model = ROBOT
	
	def get_context_data(self, **kwargs):
		context = super(ROBOT_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class CODE_DETAILVIEW(DetailView):
	template_name = 'CODE_detail.html'
	model = CODE
	
	def get_context_data(self, **kwargs):
		context = super(CODE_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_LIBRARY_DETAILVIEW(DetailView):
	template_name = 'BASIC_LIBRARY_detail.html'
	model = BASIC_LIBRARY
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_LIBRARY_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_COMP_DETAILVIEW(DetailView):
	template_name = 'BASIC_COMP_detail.html'
	model = BASIC_COMP
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_COMP_DETAILVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_STRUCTURE_DELETEVIEW(DeleteView):
	template_name = 'BASIC_STRUCTURE_direct-delete.html'
	model = BASIC_STRUCTURE
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_STRUCTURE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class FULL_CODE_DELETEVIEW(DeleteView):
	template_name = 'FULL_CODE_direct-delete.html'
	model = FULL_CODE
	
	def get_context_data(self, **kwargs):
		context = super(FULL_CODE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class RB_CATEGO_DELETEVIEW(DeleteView):
	template_name = 'RB_CATEGO_direct-delete.html'
	model = RB_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(RB_CATEGO_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class RB_SUBC_DELETEVIEW(DeleteView):
	template_name = 'RB_SUBC_direct-delete.html'
	model = RB_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(RB_SUBC_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class RB_TYPE_DELETEVIEW(DeleteView):
	template_name = 'RB_TYPE_direct-delete.html'
	model = RB_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(RB_TYPE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class C_CATEGO_DELETEVIEW(DeleteView):
	template_name = 'C_CATEGO_direct-delete.html'
	model = C_CATEGO
	
	def get_context_data(self, **kwargs):
		context = super(C_CATEGO_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class C_SUBC_DELETEVIEW(DeleteView):
	template_name = 'C_SUBC_direct-delete.html'
	model = C_SUBC
	
	def get_context_data(self, **kwargs):
		context = super(C_SUBC_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class C_TYPE_DELETEVIEW(DeleteView):
	template_name = 'C_TYPE_direct-delete.html'
	model = C_TYPE
	
	def get_context_data(self, **kwargs):
		context = super(C_TYPE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class COMPONENT_DELETEVIEW(DeleteView):
	template_name = 'COMPONENT_direct-delete.html'
	model = COMPONENT
	
	def get_context_data(self, **kwargs):
		context = super(COMPONENT_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class ROBOT_DELETEVIEW(DeleteView):
	template_name = 'ROBOT_direct-delete.html'
	model = ROBOT
	
	def get_context_data(self, **kwargs):
		context = super(ROBOT_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class CODE_DELETEVIEW(DeleteView):
	template_name = 'CODE_direct-delete.html'
	model = CODE
	
	def get_context_data(self, **kwargs):
		context = super(CODE_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_LIBRARY_DELETEVIEW(DeleteView):
	template_name = 'BASIC_LIBRARY_direct-delete.html'
	model = BASIC_LIBRARY
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_LIBRARY_DELETEVIEW, self).get_context_data(**kwargs)
		return context

class BASIC_COMP_DELETEVIEW(DeleteView):
	template_name = 'BASIC_COMP_direct-delete.html'
	model = BASIC_COMP
	
	def get_context_data(self, **kwargs):
		context = super(BASIC_COMP_DELETEVIEW, self).get_context_data(**kwargs)
		return context

