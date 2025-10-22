#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_enhanced_documentation():
    doc = SimpleDocTemplate("Smart_Dairy_Enhanced_Copyright_Documentation.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Enhanced styles
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', 
                               fontSize=7, leftIndent=15, backgroundColor=colors.lightgrey,
                               borderWidth=1, borderColor=colors.grey, spaceAfter=10)
    
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=26, 
                                alignment=1, spaceAfter=20, textColor=colors.darkblue)
    
    # 1. ENHANCED TITLE PAGE
    story.append(Paragraph("SMART DAIRY", title_style))
    story.append(Paragraph("AI-Powered Dairy Management Platform", styles['Heading2']))
    story.append(Spacer(1, 30))
    
    # Enhanced info table
    info_data = [
        ['Software Name:', 'Smart Dairy Platform'],
        ['Version:', '1.0.0'],
        ['Release Date:', datetime.now().strftime('%B %d, %Y')],
        ['Authors:', 'Smart Dairy Development Team'],
        ['License:', 'Proprietary Software'],
        ['Platform:', 'Web Application (Django)'],
        ['AI Engine:', 'Google Gemini 2.0 Flash'],
        ['Database:', 'SQLite/PostgreSQL']
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.lightblue),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(info_table)
    story.append(PageBreak())
    
    # 2. ENHANCED ABSTRACT
    story.append(Paragraph("ABSTRACT", styles['Heading1']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Purpose:", styles['Heading3']))
    story.append(Paragraph("Smart Dairy revolutionizes dairy farming through AI-powered health monitoring, disease detection, feed optimization, and production analytics.", styles['Normal']))
    
    story.append(Paragraph("Core Technologies:", styles['Heading3']))
    tech_list = """• Python Django 5.2.7 Framework
• Google Gemini 2.0 Flash AI Engine
• Computer Vision for Disease Detection
• Natural Language Processing (English/Swahili)
• Bootstrap 5.3.0 Responsive UI
• SQLite/PostgreSQL Database
• RESTful API Architecture"""
    story.append(Paragraph(tech_list, styles['Normal']))
    
    story.append(Paragraph("Deployment Platform:", styles['Heading3']))
    story.append(Paragraph("Cloud-native web application supporting AWS, Google Cloud, Azure deployment with mobile-responsive interface.", styles['Normal']))
    story.append(PageBreak())
    
    # 3. SYSTEM ARCHITECTURE
    story.append(Paragraph("SYSTEM ARCHITECTURE", styles['Heading1']))
    
    # Database Models
    story.append(Paragraph("3.1 Database Models", styles['Heading2']))
    models_code = """# Complete Cow Management Model
class Cow(models.Model):
    HEALTH_CHOICES = [
        ('excellent', 'Excellent'), ('good', 'Good'), 
        ('fair', 'Fair'), ('poor', 'Poor'), ('sick', 'Sick')
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=50, unique=True)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    health_condition = models.CharField(max_length=20, choices=HEALTH_CHOICES)
    date_added = models.DateTimeField(default=timezone.now)

class DailyFeedRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    protein_feed = models.FloatField()
    silage = models.FloatField()
    minerals = models.FloatField()
    milk_yield = models.FloatField(null=True, blank=True)
    is_ai_recommended = models.BooleanField(default=False)
    week_start_date = models.DateField(default=timezone.now)"""
    
    story.append(Paragraph(models_code, code_style))
    story.append(PageBreak())
    
    # AI Service
    story.append(Paragraph("3.2 AI Service Engine", styles['Heading2']))
    ai_code = """class AIService:
    def __init__(self):
        genai.configure(api_key=settings.AI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        self.vision_model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def analyze_disease_photo(self, image_file, language='en'):
        image = Image.open(image_file)
        prompt = self._build_disease_analysis_prompt(language)
        response = self.vision_model.generate_content([prompt, image])
        return self._parse_disease_response(response.text, language)
    
    def get_feed_recommendation(self, cow_data, language='en'):
        prompt = self._build_feed_prompt(cow_data, language)
        response = self.model.generate_content(prompt)
        return self._parse_feed_response(response.text, language, cow_data)
    
    def chat_response(self, message, language='en'):
        simple_prompt = f"Answer this farming question: {message}"
        response = self.model.generate_content(simple_prompt)
        return response.text.strip() if response.text else "No response"
    
    def predict_milk_production(self, cow_data, language='en'):
        prompt = self._build_prediction_prompt(cow_data, language)
        response = self.model.generate_content(prompt)
        return self._parse_prediction_response(response.text, language)"""
    
    story.append(Paragraph(ai_code, code_style))
    story.append(PageBreak())
    
    # Screenshots Section
    story.append(Paragraph("4. USER INTERFACE DOCUMENTATION", styles['Heading1']))
    
    # Landing Page
    story.append(Paragraph("4.1 Main Landing Interface", styles['Heading2']))
    story.append(Paragraph("The main interface showcases AI-powered dairy solutions with comprehensive navigation and feature highlights.", styles['Normal']))
    if os.path.exists("interface.png"):
        img1 = Image("interface.png", width=6.5*inch, height=3.5*inch)
        story.append(img1)
    story.append(Spacer(1, 15))
    
    # AI Feed System
    story.append(Paragraph("4.2 AI Feed Personalization System", styles['Heading2']))
    story.append(Paragraph("Advanced AI generates personalized nutrition plans based on cow characteristics, health status, and production goals.", styles['Normal']))
    if os.path.exists("AI feed personalization.png"):
        img2 = Image("AI feed personalization.png", width=6.5*inch, height=3.5*inch)
        story.append(img2)
    story.append(PageBreak())
    
    # Disease Detection
    story.append(Paragraph("4.3 Computer Vision Disease Detection", styles['Heading2']))
    story.append(Paragraph("AI-powered image analysis provides instant disease diagnosis with treatment recommendations and urgency levels.", styles['Normal']))
    if os.path.exists("disease detection system.png"):
        img3 = Image("disease detection system.png", width=6.5*inch, height=4*inch)
        story.append(img3)
    story.append(Spacer(1, 15))
    
    # Bilingual Chatbot
    story.append(Paragraph("4.4 Bilingual AI Assistant", styles['Heading2']))
    story.append(Paragraph("Natural language processing supports English and Swahili for comprehensive farmer assistance.", styles['Normal']))
    if os.path.exists("bilingualchatbot.png"):
        img4 = Image("bilingualchatbot.png", width=6.5*inch, height=3.5*inch)
        story.append(img4)
    story.append(PageBreak())
    
    # Technical Implementation
    story.append(Paragraph("5. TECHNICAL IMPLEMENTATION", styles['Heading1']))
    
    # Views
    story.append(Paragraph("5.1 Core Application Views", styles['Heading2']))
    views_code = """@login_required
def dashboard(request):
    user_cows = Cow.objects.filter(owner=request.user)
    total_cows = user_cows.count()
    context = {
        'total_cows': total_cows,
        'cows': user_cows[:5],
        'recent_records': DailyFeedRecord.objects.filter(
            cow__owner=request.user
        ).order_by('-date')[:10]
    }
    return render(request, 'main/dashboard.html', context)

def ai_disease_detection(request):
    if request.method == 'POST' and request.FILES.get('cow_image'):
        image = request.FILES['cow_image']
        language = request.POST.get('language', 'en')
        ai_service = AIService()
        analysis = ai_service.analyze_disease_photo(image, language)
        return JsonResponse(analysis)
    return render(request, 'main/disease_detection.html')

def generate_feed_plan(request, cow_id):
    cow = get_object_or_404(Cow, id=cow_id, owner=request.user)
    ai_service = AIService()
    cow_data = {
        'breed': cow.breed, 'weight': cow.weight,
        'age': cow.age, 'health_condition': cow.health_condition
    }
    feed_plan = ai_service.get_feed_recommendation(cow_data)
    return JsonResponse(feed_plan)"""
    
    story.append(Paragraph(views_code, code_style))
    story.append(PageBreak())
    
    # URL Configuration
    story.append(Paragraph("5.2 URL Routing Configuration", styles['Heading2']))
    urls_code = """urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-cow/', views.add_cow, name='add_cow'),
    path('cow/<int:cow_id>/', views.cow_detail, name='cow_detail'),
    path('ai-analysis/<int:cow_id>/', views.ai_analysis, name='ai_analysis'),
    path('feed-plan/<int:cow_id>/', views.generate_feed_plan, name='feed_plan'),
    path('disease-detection/', views.disease_detection, name='disease_detection'),
    path('chat/', views.ai_chat, name='ai_chat'),
    path('production-stats/', views.production_stats, name='production_stats'),
]"""
    
    story.append(Paragraph(urls_code, code_style))
    story.append(Spacer(1, 20))
    
    # Copyright Section
    story.append(Paragraph("COPYRIGHT & LEGAL INFORMATION", styles['Heading1']))
    copyright_text = f"""This software and all associated intellectual property, including but not limited to:
    • Source code and algorithms
    • User interface designs
    • AI model implementations
    • Database schemas
    • Documentation and methodologies
    
    Are the exclusive property of Smart Dairy Development Team.
    
    © {datetime.now().year} Smart Dairy Development Team. All Rights Reserved.
    
    Patent Pending: AI-powered dairy management and disease detection systems.
    Trademark: "Smart Dairy" and associated branding elements."""
    
    story.append(Paragraph(copyright_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("Enhanced Smart Dairy Documentation created successfully!")

if __name__ == "__main__":
    create_enhanced_documentation()
