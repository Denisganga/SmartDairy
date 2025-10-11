from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-cow/', views.add_cow, name='add_cow'),
    path('cows/', views.cow_list, name='cow_list'),
    path('cow/<int:cow_id>/', views.cow_detail, name='cow_detail'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('disease-detection/', views.disease_detection, name='disease_detection'),
    path('api/analyze-disease/', views.analyze_disease_api, name='analyze_disease_api'),
    path('api/apply-recommendation/<int:cow_id>/', views.apply_recommendation_api, name='apply_recommendation_api'),
    path('api/update-milk-yield/<int:record_id>/', views.update_milk_yield_api, name='update_milk_yield_api'),
    path('api/add-manual-entry/<int:cow_id>/', views.add_manual_entry_api, name='add_manual_entry_api'),
    path('api/get-health-insights/', views.get_health_insights_api, name='get_health_insights_api'),
    path('api/update-health-condition/', views.update_health_condition_api, name='update_health_condition_api'),
]
