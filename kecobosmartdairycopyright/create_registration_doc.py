#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_registration_document():
    doc = SimpleDocTemplate("KECOSO_Smart_Dairy_Registration.pdf", pagesize=A4, 
                           topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    story = []
    
    # Title Page
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=20, 
                                alignment=1, spaceAfter=30, textColor=colors.darkblue)
    story.append(Paragraph("SOFTWARE REGISTRATION DOCUMENTATION", title_style))
    story.append(Paragraph("KECOSO SMART DAIRY PLATFORM", styles['Heading1']))
    story.append(Spacer(1, 30))
    
    # Registration Details Table
    reg_data = [
        ['Software Name:', 'KECOSO Smart Dairy Platform'],
        ['Version:', '1.0.0'],
        ['Developer/Company:', 'KECOSO Smart Dairy Team'],
        ['Registration Date:', datetime.now().strftime('%B %d, %Y')],
        ['Software Type:', 'Web-based AI Dairy Management System'],
        ['Programming Language:', 'Python (Django Framework)'],
        ['Database:', 'SQLite/PostgreSQL'],
        ['License Type:', 'Proprietary Commercial License']
    ]
    
    reg_table = Table(reg_data, colWidths=[2*inch, 4*inch])
    reg_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.black),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('GRID', (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(reg_table)
    story.append(PageBreak())
    
    # Abstract
    story.append(Paragraph("ABSTRACT", styles['Heading2']))
    abstract = """
    KECOSO Smart Dairy Platform is an innovative AI-powered web application designed to revolutionize 
    dairy farm management in Kenya and East Africa. The system integrates advanced artificial intelligence, 
    computer vision, and data analytics to provide comprehensive solutions for:
    
    • AI-powered disease detection through image analysis
    • Personalized feed optimization based on individual cow characteristics  
    • Bilingual AI assistant supporting English and Swahili languages
    • Real-time health monitoring and production analytics
    • Predictive modeling for milk yield optimization
    
    The platform addresses critical challenges in dairy farming by providing farmers with intelligent, 
    data-driven insights to improve cow health, optimize feed costs, and maximize milk production efficiency.
    """
    story.append(Paragraph(abstract, styles['Normal']))
    story.append(PageBreak())
    
    # System Architecture
    story.append(Paragraph("SYSTEM ARCHITECTURE & FEATURES", styles['Heading2']))
    
    # Add screenshots
    try:
        # Main Interface
        story.append(Paragraph("1. Main Dashboard Interface", styles['Heading3']))
        if os.path.exists("interface.png"):
            img1 = Image("interface.png", width=6*inch, height=3*inch)
            story.append(img1)
        story.append(Spacer(1, 10))
        
        # AI Feed Personalization
        story.append(Paragraph("2. AI-Powered Feed Personalization", styles['Heading3']))
        if os.path.exists("AI feed personalization.png"):
            img2 = Image("AI feed personalization.png", width=6*inch, height=3*inch)
            story.append(img2)
        story.append(Spacer(1, 10))
        
        story.append(PageBreak())
        
        # Disease Detection
        story.append(Paragraph("3. AI Disease Detection System", styles['Heading3']))
        if os.path.exists("disease detection system.png"):
            img3 = Image("disease detection system.png", width=6*inch, height=4*inch)
            story.append(img3)
        story.append(Spacer(1, 10))
        
        # Bilingual Chatbot
        story.append(Paragraph("4. Bilingual AI Assistant", styles['Heading3']))
        if os.path.exists("bilingualchatbot.png"):
            img4 = Image("bilingualchatbot.png", width=6*inch, height=3*inch)
            story.append(img4)
            
    except Exception as e:
        story.append(Paragraph(f"Screenshots will be embedded from: interface.png, AI feed personalization.png, disease detection system.png, bilingualchatbot.png", styles['Normal']))
    
    story.append(PageBreak())
    
    # Technical Implementation
    story.append(Paragraph("TECHNICAL IMPLEMENTATION", styles['Heading2']))
    
    # Core Code Structure
    story.append(Paragraph("Core Application Structure (Django Views):", styles['Heading3']))
    code_sample = """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cow, HealthRecord, ProductionRecord
from .gemini_service import AIService

@login_required
def dashboard(request):
    user_cows = Cow.objects.filter(farmer=request.user)
    total_cows = user_cows.count()
    avg_production = user_cows.aggregate(Avg('daily_milk_yield'))
    
    context = {
        'total_cows': total_cows,
        'avg_production': avg_production['daily_milk_yield__avg'] or 0,
        'cows': user_cows[:5]  # Recent 5 cows
    }
    return render(request, 'main/dashboard.html', context)

def ai_disease_detection(request):
    if request.method == 'POST' and request.FILES.get('cow_image'):
        image = request.FILES['cow_image']
        ai_service = AIService()
        analysis = ai_service.analyze_cow_health(image)
        return JsonResponse(analysis)
    return render(request, 'main/disease_detection.html')
    """
    
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', 
                               fontSize=8, leftIndent=20, backgroundColor=colors.lightgrey)
    story.append(Paragraph(code_sample, code_style))
    story.append(PageBreak())
    
    # AI Integration
    story.append(Paragraph("AI SERVICE INTEGRATION", styles['Heading3']))
    ai_code = """
import google.generativeai as genai
from PIL import Image as PILImage

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro-vision')
    
    def analyze_cow_health(self, image_file):
        image = PILImage.open(image_file)
        prompt = '''Analyze this cow image for health conditions. 
                   Identify any visible diseases, symptoms, and provide 
                   treatment recommendations.'''
        
        response = self.model.generate_content([prompt, image])
        return {
            'disease_detected': self.extract_disease(response.text),
            'symptoms': self.extract_symptoms(response.text),
            'treatment': self.extract_treatment(response.text),
            'urgency_level': self.assess_urgency(response.text)
        }
    
    def generate_feed_plan(self, cow_data):
        prompt = f'''Create personalized feed plan for cow:
                    Breed: {cow_data['breed']}
                    Weight: {cow_data['weight']}kg
                    Age: {cow_data['age']} months
                    Production: {cow_data['milk_yield']}L/day'''
        
        response = self.model.generate_content(prompt)
        return self.parse_feed_recommendations(response.text)
    """
    story.append(Paragraph(ai_code, code_style))
    story.append(PageBreak())
    
    # Copyright and Legal
    story.append(Paragraph("COPYRIGHT & INTELLECTUAL PROPERTY", styles['Heading2']))
    copyright_text = f"""
    <b>Copyright Notice:</b><br/>
    © {datetime.now().year} KECOSO Smart Dairy Team. All rights reserved.<br/><br/>
    
    <b>Intellectual Property Rights:</b><br/>
    This software and all associated documentation, algorithms, user interfaces, and 
    methodologies are the exclusive intellectual property of KECOSO Smart Dairy Team.<br/><br/>
    
    <b>Patent Pending:</b><br/>
    AI-powered dairy management algorithms and computer vision disease detection methods.<br/><br/>
    
    <b>Trademark:</b><br/>
    "KECOSO Smart Dairy" and associated logos are trademarks of KECOSO Smart Dairy Team.<br/><br/>
    
    <b>Contact Information:</b><br/>
    Email: info@kecososmartdairy.com<br/>
    Phone: +254-XXX-XXXXXX<br/>
    Address: Nairobi, Kenya
    """
    story.append(Paragraph(copyright_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("Registration documentation created successfully!")

if __name__ == "__main__":
    create_registration_document()
