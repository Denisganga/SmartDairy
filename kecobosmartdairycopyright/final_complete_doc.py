#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_final_documentation():
    doc = SimpleDocTemplate("Smart_Dairy_Final_Copyright_Documentation.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', 
                               fontSize=7, leftIndent=15, backgroundColor=colors.lightgrey)
    
    # 1. TITLE PAGE
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=26, 
                                alignment=1, spaceAfter=20, textColor=colors.darkblue)
    
    story.append(Paragraph("SMART DAIRY", title_style))
    story.append(Paragraph("AI-Powered Dairy Management Platform", styles['Heading2']))
    story.append(Spacer(1, 30))
    
    info_data = [
        ['Software Name:', 'Smart Dairy Platform'],
        ['Version:', '1.0.0'],
        ['Authors:', 'Smart Dairy Development Team'],
        ['Owner:', 'Smart Dairy Development Team'],
        ['Date:', datetime.now().strftime('%B %d, %Y')]
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.lightblue),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold')
    ]))
    story.append(info_table)
    story.append(PageBreak())
    
    # 2. ABSTRACT
    story.append(Paragraph("ABSTRACT", styles['Heading1']))
    
    story.append(Paragraph("Purpose of the Software:", styles['Heading3']))
    story.append(Paragraph("Smart Dairy revolutionizes dairy farming through AI-powered health monitoring, disease detection, feed optimization, and production analytics.", styles['Normal']))
    
    story.append(Paragraph("Technologies Built From:", styles['Heading3']))
    story.append(Paragraph("Python Django 5.2.7, Google Gemini 2.0 Flash AI, Bootstrap 5.3.0, SQLite/PostgreSQL", styles['Normal']))
    
    story.append(Paragraph("Platform:", styles['Heading3']))
    story.append(Paragraph("Web-based application deployable on cloud platforms (AWS, Google Cloud, Azure)", styles['Normal']))
    story.append(PageBreak())
    
    # 3. INTRODUCTION - THE MISSING SECTION!
    story.append(Paragraph("INTRODUCTION", styles['Heading1']))
    story.append(Spacer(1, 15))
    
    intro_text = """Smart Dairy is an innovative web-based platform that leverages advanced artificial intelligence 
    to transform traditional dairy farming practices in Kenya and East Africa. The software addresses critical 
    challenges faced by dairy farmers including early disease detection, optimal feed management, and production optimization.

    Key Functionalities:
    • AI-powered disease detection through computer vision analysis of cow photographs
    • Personalized feed recommendations based on individual cow characteristics (breed, age, weight, health status)
    • Bilingual AI assistant providing expert advice in English and Swahili languages
    • Real-time health monitoring and production analytics dashboard
    • Comprehensive cow management system with detailed record keeping
    • Secure farmer registration and authentication system
    • Mobile-responsive interface for field use

    How the Software Works:
    Farmers begin by registering on the platform and creating their farm profile. They can then add individual cows 
    to their digital herd, recording essential details like breed, age, weight, and health status. The AI system 
    analyzes uploaded cow photos to detect diseases early, providing immediate diagnostic insights and treatment 
    recommendations with urgency levels.

    The feed optimization module generates personalized nutrition plans considering each cow's unique characteristics 
    and production goals. Farmers can interact with the bilingual AI assistant for instant expert advice on various 
    dairy farming topics. The system continuously learns from data to improve recommendations and predictions.

    The platform's dashboard provides comprehensive analytics on herd health, production trends, and feed efficiency, 
    enabling data-driven decision making for improved farm profitability and cow welfare."""
    
    story.append(Paragraph(intro_text, styles['Normal']))
    story.append(PageBreak())
    
    # 4. ACTUAL DOCUMENTATION
    story.append(Paragraph("SOFTWARE DOCUMENTATION", styles['Heading1']))
    
    # Screenshots with descriptions
    story.append(Paragraph("4.1 Main Landing Interface", styles['Heading2']))
    if os.path.exists("interface.png"):
        img1 = Image("interface.png", width=6.5*inch, height=3.5*inch)
        story.append(img1)
    story.append(Paragraph("The landing page showcases AI-powered dairy solutions with comprehensive navigation.", styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("4.2 AI Feed Personalization", styles['Heading2']))
    if os.path.exists("AI feed personalization.png"):
        img2 = Image("AI feed personalization.png", width=6.5*inch, height=3.5*inch)
        story.append(img2)
    story.append(Paragraph("AI generates personalized nutrition plans based on cow characteristics.", styles['Normal']))
    story.append(PageBreak())
    
    story.append(Paragraph("4.3 Disease Detection System", styles['Heading2']))
    if os.path.exists("disease detection system.png"):
        img3 = Image("disease detection system.png", width=6.5*inch, height=4*inch)
        story.append(img3)
    story.append(Paragraph("Computer vision provides instant disease diagnosis with treatment recommendations.", styles['Normal']))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("4.4 Bilingual AI Assistant", styles['Heading2']))
    if os.path.exists("bilingualchatbot.png"):
        img4 = Image("bilingualchatbot.png", width=6.5*inch, height=3.5*inch)
        story.append(img4)
    story.append(Paragraph("Natural language processing supports English and Swahili.", styles['Normal']))
    story.append(PageBreak())
    
    # Code sections
    story.append(Paragraph("4.5 Core Application Code", styles['Heading2']))
    
    # Models
    models_code = """# Database Models
class Cow(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    health_condition = models.CharField(max_length=20)

class DailyFeedRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    protein_feed = models.FloatField()
    silage = models.FloatField()
    minerals = models.FloatField()
    is_ai_recommended = models.BooleanField(default=False)"""
    
    story.append(Paragraph(models_code, code_style))
    story.append(Spacer(1, 10))
    
    # AI Service
    ai_code = """# AI Service Implementation
class AIService:
    def __init__(self):
        genai.configure(api_key=settings.AI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def analyze_disease_photo(self, image_file, language='en'):
        image = Image.open(image_file)
        prompt = self._build_disease_analysis_prompt(language)
        response = self.vision_model.generate_content([prompt, image])
        return self._parse_disease_response(response.text, language)
    
    def get_feed_recommendation(self, cow_data, language='en'):
        prompt = self._build_feed_prompt(cow_data, language)
        response = self.model.generate_content(prompt)
        return self._parse_feed_response(response.text, language)"""
    
    story.append(Paragraph(ai_code, code_style))
    story.append(PageBreak())
    
    # Views
    views_code = """# Django Views
@login_required
def dashboard(request):
    user_cows = Cow.objects.filter(owner=request.user)
    context = {'total_cows': user_cows.count(), 'cows': user_cows[:5]}
    return render(request, 'main/dashboard.html', context)

def ai_disease_detection(request):
    if request.method == 'POST' and request.FILES.get('cow_image'):
        image = request.FILES['cow_image']
        ai_service = AIService()
        analysis = ai_service.analyze_disease_photo(image)
        return JsonResponse(analysis)
    return render(request, 'main/disease_detection.html')"""
    
    story.append(Paragraph(views_code, code_style))
    
    # Build PDF
    doc.build(story)
    print("Final Complete Documentation with Introduction created!")

if __name__ == "__main__":
    create_final_documentation()
