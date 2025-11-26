from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'todos_miembros': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'miembro': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  template = loader.get_template('template.html')
  miembros = Member.objects.all().values()
  colum_firstname = Member.objects.values_list('firstname')
  records_Kamila = Member.objects.filter(firstname='Kamila').values()   
  record_Tatiana_Bayona = Member.objects.filter(firstname='Tatiana',id=3).values()
  record_or_Sandra_Jorge =  Member.objects.filter(firstname='Sandra').values() | Member.objects.filter(firstname='Jorge').values()
  record_like_star_L = Member.objects.filter(firstname__startswith='L').values()
  record_like_ends_s = Member.objects.filter(firstname__iendswith='s').values()
  record_like_contains_ez = Member.objects.filter(firstname__icontains='re').values()
  record_like_endswith_ez = Member.objects.filter(lastname__endswith='ez').values()
  record_like_gt_2022_01_01 = Member.objects.filter(joined_date__gt='2022-01-01').values()
  order_by_asc = Member.objects.all().order_by('firstname').values()
  order_by_desc = Member.objects.all().order_by('-firstname').values()
  
  
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'miembros': miembros,
    'colum_firstname': colum_firstname,
    'records_Kamila': records_Kamila,
    'record_Tatiana_Bayona': record_Tatiana_Bayona,
    'record_or_Sandra_Jorge': record_or_Sandra_Jorge,
    'record_like_star_L': record_like_star_L,
    'record_like_ends_s': record_like_ends_s,
    'record_like_contains_ez': record_like_contains_ez,
    'record_like_endswith_ez': record_like_endswith_ez,
    'record_like_gt_2022_01_01': record_like_gt_2022_01_01,
    'order_by_asc': order_by_asc,
    'order_by_desc': order_by_desc,
    
  }
  return HttpResponse(template.render(context, request))