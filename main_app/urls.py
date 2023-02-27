
from django.contrib import admin
from django.urls import path

from main_app.views import *
urlpatterns=[]
urlpatterns +=[path('',Index.as_view(),name='Index'),]
urlpatterns +=[path('BASIC_STRUCTURE_CREATEVIEW',BASIC_STRUCTURE_CREATEVIEW.as_view(),name='BASIC_STRUCTURE_CREATEVIEW'),]
urlpatterns +=[path('FULL_CODE_CREATEVIEW',FULL_CODE_CREATEVIEW.as_view(),name='FULL_CODE_CREATEVIEW'),]
urlpatterns +=[path('RB_CATEGO_CREATEVIEW',RB_CATEGO_CREATEVIEW.as_view(),name='RB_CATEGO_CREATEVIEW'),]
urlpatterns +=[path('RB_SUBC_CREATEVIEW',RB_SUBC_CREATEVIEW.as_view(),name='RB_SUBC_CREATEVIEW'),]
urlpatterns +=[path('RB_TYPE_CREATEVIEW',RB_TYPE_CREATEVIEW.as_view(),name='RB_TYPE_CREATEVIEW'),]
urlpatterns +=[path('C_CATEGO_CREATEVIEW',C_CATEGO_CREATEVIEW.as_view(),name='C_CATEGO_CREATEVIEW'),]
urlpatterns +=[path('C_SUBC_CREATEVIEW',C_SUBC_CREATEVIEW.as_view(),name='C_SUBC_CREATEVIEW'),]
urlpatterns +=[path('C_TYPE_CREATEVIEW',C_TYPE_CREATEVIEW.as_view(),name='C_TYPE_CREATEVIEW'),]
urlpatterns +=[path('COMPONENT_CREATEVIEW',COMPONENT_CREATEVIEW.as_view(),name='COMPONENT_CREATEVIEW'),]
urlpatterns +=[path('ROBOT_CREATEVIEW',ROBOT_CREATEVIEW.as_view(),name='ROBOT_CREATEVIEW'),]
urlpatterns +=[path('CODE_CREATEVIEW',CODE_CREATEVIEW.as_view(),name='CODE_CREATEVIEW'),]
urlpatterns +=[path('BASIC_LIBRARY_CREATEVIEW',BASIC_LIBRARY_CREATEVIEW.as_view(),name='BASIC_LIBRARY_CREATEVIEW'),]
urlpatterns +=[path('BASIC_COMP_CREATEVIEW',BASIC_COMP_CREATEVIEW.as_view(),name='BASIC_COMP_CREATEVIEW'),]
urlpatterns +=[path('BASIC_STRUCTURE_LISTVIEW',BASIC_STRUCTURE_LISTVIEW.as_view(),name='BASIC_STRUCTURE_LISTVIEW'),]
urlpatterns +=[path('FULL_CODE_LISTVIEW',FULL_CODE_LISTVIEW.as_view(),name='FULL_CODE_LISTVIEW'),]
urlpatterns +=[path('RB_CATEGO_LISTVIEW',RB_CATEGO_LISTVIEW.as_view(),name='RB_CATEGO_LISTVIEW'),]
urlpatterns +=[path('RB_SUBC_LISTVIEW',RB_SUBC_LISTVIEW.as_view(),name='RB_SUBC_LISTVIEW'),]
urlpatterns +=[path('RB_TYPE_LISTVIEW',RB_TYPE_LISTVIEW.as_view(),name='RB_TYPE_LISTVIEW'),]
urlpatterns +=[path('C_CATEGO_LISTVIEW',C_CATEGO_LISTVIEW.as_view(),name='C_CATEGO_LISTVIEW'),]
urlpatterns +=[path('C_SUBC_LISTVIEW',C_SUBC_LISTVIEW.as_view(),name='C_SUBC_LISTVIEW'),]
urlpatterns +=[path('C_TYPE_LISTVIEW',C_TYPE_LISTVIEW.as_view(),name='C_TYPE_LISTVIEW'),]
urlpatterns +=[path('COMPONENT_LISTVIEW',COMPONENT_LISTVIEW.as_view(),name='COMPONENT_LISTVIEW'),]
urlpatterns +=[path('ROBOT_LISTVIEW',ROBOT_LISTVIEW.as_view(),name='ROBOT_LISTVIEW'),]
urlpatterns +=[path('CODE_LISTVIEW',CODE_LISTVIEW.as_view(),name='CODE_LISTVIEW'),]
urlpatterns +=[path('BASIC_LIBRARY_LISTVIEW',BASIC_LIBRARY_LISTVIEW.as_view(),name='BASIC_LIBRARY_LISTVIEW'),]
urlpatterns +=[path('BASIC_COMP_LISTVIEW',BASIC_COMP_LISTVIEW.as_view(),name='BASIC_COMP_LISTVIEW'),]
urlpatterns +=[path('BASIC_STRUCTURE_UPDATEVIEW',BASIC_STRUCTURE_UPDATEVIEW.as_view(),name='BASIC_STRUCTURE_UPDATEVIEW'),]
urlpatterns +=[path('FULL_CODE_UPDATEVIEW',FULL_CODE_UPDATEVIEW.as_view(),name='FULL_CODE_UPDATEVIEW'),]
urlpatterns +=[path('RB_CATEGO_UPDATEVIEW',RB_CATEGO_UPDATEVIEW.as_view(),name='RB_CATEGO_UPDATEVIEW'),]
urlpatterns +=[path('RB_SUBC_UPDATEVIEW',RB_SUBC_UPDATEVIEW.as_view(),name='RB_SUBC_UPDATEVIEW'),]
urlpatterns +=[path('RB_TYPE_UPDATEVIEW',RB_TYPE_UPDATEVIEW.as_view(),name='RB_TYPE_UPDATEVIEW'),]
urlpatterns +=[path('C_CATEGO_UPDATEVIEW',C_CATEGO_UPDATEVIEW.as_view(),name='C_CATEGO_UPDATEVIEW'),]
urlpatterns +=[path('C_SUBC_UPDATEVIEW',C_SUBC_UPDATEVIEW.as_view(),name='C_SUBC_UPDATEVIEW'),]
urlpatterns +=[path('C_TYPE_UPDATEVIEW',C_TYPE_UPDATEVIEW.as_view(),name='C_TYPE_UPDATEVIEW'),]
urlpatterns +=[path('COMPONENT_UPDATEVIEW',COMPONENT_UPDATEVIEW.as_view(),name='COMPONENT_UPDATEVIEW'),]
urlpatterns +=[path('ROBOT_UPDATEVIEW',ROBOT_UPDATEVIEW.as_view(),name='ROBOT_UPDATEVIEW'),]
urlpatterns +=[path('CODE_UPDATEVIEW',CODE_UPDATEVIEW.as_view(),name='CODE_UPDATEVIEW'),]
urlpatterns +=[path('BASIC_LIBRARY_UPDATEVIEW',BASIC_LIBRARY_UPDATEVIEW.as_view(),name='BASIC_LIBRARY_UPDATEVIEW'),]
urlpatterns +=[path('BASIC_COMP_UPDATEVIEW',BASIC_COMP_UPDATEVIEW.as_view(),name='BASIC_COMP_UPDATEVIEW'),]
urlpatterns +=[path('BASIC_STRUCTURE_DETAILVIEW',BASIC_STRUCTURE_DETAILVIEW.as_view(),name='BASIC_STRUCTURE_DETAILVIEW'),]
urlpatterns +=[path('FULL_CODE_DETAILVIEW',FULL_CODE_DETAILVIEW.as_view(),name='FULL_CODE_DETAILVIEW'),]
urlpatterns +=[path('RB_CATEGO_DETAILVIEW',RB_CATEGO_DETAILVIEW.as_view(),name='RB_CATEGO_DETAILVIEW'),]
urlpatterns +=[path('RB_SUBC_DETAILVIEW',RB_SUBC_DETAILVIEW.as_view(),name='RB_SUBC_DETAILVIEW'),]
urlpatterns +=[path('RB_TYPE_DETAILVIEW',RB_TYPE_DETAILVIEW.as_view(),name='RB_TYPE_DETAILVIEW'),]
urlpatterns +=[path('C_CATEGO_DETAILVIEW',C_CATEGO_DETAILVIEW.as_view(),name='C_CATEGO_DETAILVIEW'),]
urlpatterns +=[path('C_SUBC_DETAILVIEW',C_SUBC_DETAILVIEW.as_view(),name='C_SUBC_DETAILVIEW'),]
urlpatterns +=[path('C_TYPE_DETAILVIEW',C_TYPE_DETAILVIEW.as_view(),name='C_TYPE_DETAILVIEW'),]
urlpatterns +=[path('COMPONENT_DETAILVIEW',COMPONENT_DETAILVIEW.as_view(),name='COMPONENT_DETAILVIEW'),]
urlpatterns +=[path('ROBOT_DETAILVIEW',ROBOT_DETAILVIEW.as_view(),name='ROBOT_DETAILVIEW'),]
urlpatterns +=[path('CODE_DETAILVIEW',CODE_DETAILVIEW.as_view(),name='CODE_DETAILVIEW'),]
urlpatterns +=[path('BASIC_LIBRARY_DETAILVIEW',BASIC_LIBRARY_DETAILVIEW.as_view(),name='BASIC_LIBRARY_DETAILVIEW'),]
urlpatterns +=[path('BASIC_COMP_DETAILVIEW',BASIC_COMP_DETAILVIEW.as_view(),name='BASIC_COMP_DETAILVIEW'),]
urlpatterns +=[path('BASIC_STRUCTURE_DELETEVIEW',BASIC_STRUCTURE_DELETEVIEW.as_view(),name='BASIC_STRUCTURE_DELETEVIEW'),]
urlpatterns +=[path('FULL_CODE_DELETEVIEW',FULL_CODE_DELETEVIEW.as_view(),name='FULL_CODE_DELETEVIEW'),]
urlpatterns +=[path('RB_CATEGO_DELETEVIEW',RB_CATEGO_DELETEVIEW.as_view(),name='RB_CATEGO_DELETEVIEW'),]
urlpatterns +=[path('RB_SUBC_DELETEVIEW',RB_SUBC_DELETEVIEW.as_view(),name='RB_SUBC_DELETEVIEW'),]
urlpatterns +=[path('RB_TYPE_DELETEVIEW',RB_TYPE_DELETEVIEW.as_view(),name='RB_TYPE_DELETEVIEW'),]
urlpatterns +=[path('C_CATEGO_DELETEVIEW',C_CATEGO_DELETEVIEW.as_view(),name='C_CATEGO_DELETEVIEW'),]
urlpatterns +=[path('C_SUBC_DELETEVIEW',C_SUBC_DELETEVIEW.as_view(),name='C_SUBC_DELETEVIEW'),]
urlpatterns +=[path('C_TYPE_DELETEVIEW',C_TYPE_DELETEVIEW.as_view(),name='C_TYPE_DELETEVIEW'),]
urlpatterns +=[path('COMPONENT_DELETEVIEW',COMPONENT_DELETEVIEW.as_view(),name='COMPONENT_DELETEVIEW'),]
urlpatterns +=[path('ROBOT_DELETEVIEW',ROBOT_DELETEVIEW.as_view(),name='ROBOT_DELETEVIEW'),]
urlpatterns +=[path('CODE_DELETEVIEW',CODE_DELETEVIEW.as_view(),name='CODE_DELETEVIEW'),]
urlpatterns +=[path('BASIC_LIBRARY_DELETEVIEW',BASIC_LIBRARY_DELETEVIEW.as_view(),name='BASIC_LIBRARY_DELETEVIEW'),]
urlpatterns +=[path('BASIC_COMP_DELETEVIEW',BASIC_COMP_DELETEVIEW.as_view(),name='BASIC_COMP_DELETEVIEW'),]