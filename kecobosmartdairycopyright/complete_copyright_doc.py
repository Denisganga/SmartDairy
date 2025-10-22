#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_complete_documentation():
    doc = SimpleDocTemplate("Smart_Dairy_Complete_Copyright_Documentation.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Code style
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', 
                               fontSize=8, leftIndent=20, backgroundColor=colors.lightgrey,
                               borderWidth=1, borderColor=colors.grey)
    
    # 1. TITLE PAGE
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, 
                                alignment=1, spaceAfter=20, textColor=colors.darkblue)
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Heading2'], 
                                   alignment=1, spaceAfter=30)
    
    story.append(Paragraph("SMART DAIRY", title_style))
    story.append(Paragraph("AI-Powered Dairy Management Platform", subtitle_style))
    story.append(Spacer(1, 30))
    
    info_style = ParagraphStyle('Info', parent=styles['Normal'], alignment=1, fontSize=12)
    story.append(Paragraph("Version 1.0", info_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Software Authors: Smart Dairy Development Team", info_style))
    story.append(Paragraph("Current Software Owner: Smart Dairy Development Team", info_style))
    story.append(Paragraph(f"Documentation Date: {datetime.now().strftime('%B %d, %Y')}", info_style))
    story.append(PageBreak())
    
    # 2. ABSTRACT
    story.append(Paragraph("ABSTRACT", styles['Heading1']))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Purpose of the Software:", styles['Heading3']))
    purpose_text = """Smart Dairy is designed to revolutionize dairy farm management through artificial intelligence. 
    The software helps farmers optimize cow health monitoring, personalize feed recommendations, detect diseases early, 
    and maximize milk production efficiency through data-driven insights."""
    story.append(Paragraph(purpose_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Technologies Built From:", styles['Heading3']))
    tech_text = """• Backend: Python Django Framework 5.2.7
    • Frontend: HTML5, CSS3, JavaScript, Bootstrap 5.3.0
    • AI Integration: Google Gemini AI for computer vision and natural language processing
    • Database: SQLite (development), PostgreSQL (production)
    • Authentication: Django built-in authentication system"""
    story.append(Paragraph(tech_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Platform:", styles['Heading3']))
    platform_text = """Smart Dairy runs as a web-based application accessible through web browsers. 
    It can be deployed on cloud platforms (AWS, Google Cloud, Azure) and accessed from desktop computers, 
    tablets, and mobile devices with internet connectivity."""
    story.append(Paragraph(platform_text, styles['Normal']))
    story.append(PageBreak())
    
    # 3. INTRODUCTION
    story.append(Paragraph("INTRODUCTION", styles['Heading1']))
    story.append(Spacer(1, 20))
    
    intro_text = """Smart Dairy is an innovative web-based platform that leverages advanced artificial intelligence 
    to transform traditional dairy farming practices. The software addresses critical challenges faced by dairy farmers 
    including disease detection, feed optimization, and production management.

    Key Functionalities:
    • AI-powered disease detection through image analysis of cow photos
    • Personalized feed recommendations based on individual cow characteristics
    • Bilingual AI assistant supporting English and Swahili languages
    • Real-time health monitoring and production analytics
    • User-friendly dashboard for farm management
    • Secure farmer registration and authentication system

    How the Software Works:
    Farmers register and log into the platform to access a comprehensive dashboard. They can add individual cows 
    to their farm profile, upload photos for AI-powered health analysis, receive personalized feed recommendations, 
    and interact with an intelligent chatbot for farming advice. The system uses machine learning algorithms to 
    analyze data and provide actionable insights for improved dairy farm productivity."""
    
    story.append(Paragraph(intro_text, styles['Normal']))
    story.append(PageBreak())
    
    # 4. SOFTWARE DOCUMENTATION WITH CODE
    story.append(Paragraph("SOFTWARE DOCUMENTATION", styles['Heading1']))
    story.append(Spacer(1, 20))
    
    # 4.1 Main Application Structure
    story.append(Paragraph("4.1 Main Application Structure (Django Views)", styles['Heading2']))
    
    views_code = """from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum
from django.http import JsonResponse
from .models import Cow, HealthRecord, FeedRecord, ProductionRecord, DailyFeedRecord
from .gemini_service import AIService
import json
from datetime import datetime, timedelta

def landing_page(request):
    return render(request, 'main/landing.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'main/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'main/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login')
    
    return render(request, 'main/register.html')

@login_required
def dashboard(request):
    user_cows = Cow.objects.filter(farmer=request.user)
    total_cows = user_cows.count()
    
    context = {
        'total_cows': total_cows,
        'cows': user_cows[:5]
    }
    return render(request, 'main/dashboard.html', context)"""
    
    story.append(Paragraph(views_code, code_style))
    story.append(PageBreak())
    
    # 4.2 AI Service Integration
    story.append(Paragraph("4.2 AI Service Integration (Gemini AI)", styles['Heading2']))
    
    ai_code = """import google.generativeai as genai
from django.conf import settings
import json
import re
from PIL import Image as PILImage
import io

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.vision_model = genai.GenerativeModel('gemini-pro-vision')
    
    def analyze_cow_health(self, image_file):
        try:
            image = PILImage.open(image_file)
            prompt = '''Analyze this cow image for health conditions. 
                       Identify any visible diseases, symptoms, and provide 
                       treatment recommendations. Format response as JSON.'''
            
            response = self.vision_model.generate_content([prompt, image])
            return self.parse_health_analysis(response.text)
        except Exception as e:
            return {'error': str(e)}
    
    def generate_feed_plan(self, cow_data):
        prompt = f'''Create personalized feed plan for cow:
                    Breed: {cow_data.get('breed', 'Unknown')}
                    Weight: {cow_data.get('weight', 0)}kg
                    Age: {cow_data.get('age', 0)} months
                    Production: {cow_data.get('milk_yield', 0)}L/day
                    Health: {cow_data.get('health_condition', 'Good')}'''
        
        response = self.model.generate_content(prompt)
        return self.parse_feed_recommendations(response.text)
    
    def chat_response(self, message, language='en'):
        if language == 'sw':
            prompt = f"Respond in Swahili about dairy farming: {message}"
        else:
            prompt = f"As a dairy farming expert, answer: {message}"
        
        response = self.model.generate_content(prompt)
        return response.text"""
    
    story.append(Paragraph(ai_code, code_style))
    story.append(PageBreak())
    
    # 4.3 Database Models
    story.append(Paragraph("4.3 Database Models", styles['Heading2']))
    
    models_code = """from django.db import models
from django.contrib.auth.models import User

class Cow(models.Model):
    BREED_CHOICES = [
        ('holstein', 'Holstein'),
        ('jersey', 'Jersey'),
        ('guernsey', 'Guernsey'),
        ('ayrshire', 'Ayrshire'),
        ('brown_swiss', 'Brown Swiss'),
    ]
    
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=20, choices=BREED_CHOICES)
    age_months = models.IntegerField()
    weight = models.FloatField()
    daily_milk_yield = models.FloatField(default=0)
    health_condition = models.CharField(max_length=50, default='Good')
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.breed})"

class HealthRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    checkup_date = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField()
    diagnosis = models.CharField(max_length=200)
    treatment = models.TextField()
    veterinarian_notes = models.TextField(blank=True)
    
class ProductionRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    morning_yield = models.FloatField()
    evening_yield = models.FloatField()
    total_yield = models.FloatField()
    
    def save(self, *args, **kwargs):
        self.total_yield = self.morning_yield + self.evening_yield
        super().save(*args, **kwargs)"""
    
    story.append(Paragraph(models_code, code_style))
    story.append(PageBreak())
    
    # Screenshots with descriptions
    story.append(Paragraph("4.4 User Interface Screenshots", styles['Heading2']))
    
    # Landing Page
    story.append(Paragraph("Landing Page Interface:", styles['Heading3']))
    if os.path.exists("interface.png"):
        img1 = Image("interface.png", width=6.5*inch, height=3.5*inch)
        story.append(img1)
    story.append(Spacer(1, 10))
    
    # AI Feed System
    story.append(Paragraph("AI Feed Personalization System:", styles['Heading3']))
    if os.path.exists("AI feed personalization.png"):
        img2 = Image("AI feed personalization.png", width=6.5*inch, height=3.5*inch)
        story.append(img2)
    story.append(PageBreak())
    
    # Disease Detection
    story.append(Paragraph("AI Disease Detection Interface:", styles['Heading3']))
    if os.path.exists("disease detection system.png"):
        img3 = Image("disease detection system.png", width=6.5*inch, height=4*inch)
        story.append(img3)
    story.append(Spacer(1, 10))
    
    # Chatbot
    story.append(Paragraph("Bilingual AI Assistant:", styles['Heading3']))
    if os.path.exists("bilingualchatbot.png"):
        img4 = Image("bilingualchatbot.png", width=6.5*inch, height=3.5*inch)
        story.append(img4)
    story.append(PageBreak())
    
    # 4.5 URL Configuration
    story.append(Paragraph("4.5 URL Configuration", styles['Heading2']))
    
    urls_code = """from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-cow/', views.add_cow, name='add_cow'),
    path('cow/<int:cow_id>/', views.cow_detail, name='cow_detail'),
    path('ai-analysis/<int:cow_id>/', views.ai_analysis, name='ai_analysis'),
    path('feed-plan/<int:cow_id>/', views.generate_feed_plan, name='feed_plan'),
    path('chat/', views.ai_chat, name='ai_chat'),
    path('disease-detection/', views.disease_detection, name='disease_detection'),
]"""
    
    story.append(Paragraph(urls_code, code_style))
    story.append(Spacer(1, 20))
    
    # Conclusion
    conclusion_text = """Smart Dairy represents a comprehensive AI-powered solution for modern dairy farm management. 
    The complete source code demonstrates the integration of Django web framework with Google Gemini AI to provide 
    farmers with intelligent tools for cow health monitoring, feed optimization, and production management. 
    The system's modular architecture ensures scalability and maintainability for future enhancements."""
    story.append(Paragraph(conclusion_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("Complete Smart Dairy Copyright Documentation with Code created successfully!")

if __name__ == "__main__":
    create_complete_documentation()
