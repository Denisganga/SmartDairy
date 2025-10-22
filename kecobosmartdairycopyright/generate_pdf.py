#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_smart_dairy_documentation():
    # Create PDF
    doc = SimpleDocTemplate("Smart_Dairy_Documentation.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], 
                                fontSize=24, spaceAfter=30, alignment=1, textColor=colors.blue)
    story.append(Paragraph("SMART DAIRY PLATFORM", title_style))
    story.append(Paragraph("AI-Powered Dairy Management System", styles['Heading2']))
    story.append(Spacer(1, 20))
    
    # Overview
    story.append(Paragraph("SYSTEM OVERVIEW", styles['Heading2']))
    overview_text = """
    Smart Dairy is an innovative AI-powered platform designed to revolutionize dairy farm management 
    through advanced artificial intelligence, computer vision, and data analytics. The system provides 
    comprehensive solutions for cow health monitoring, feed optimization, disease detection, and 
    production analytics.
    """
    story.append(Paragraph(overview_text, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Key Features
    story.append(Paragraph("KEY FEATURES", styles['Heading2']))
    features = [
        "AI-Powered Disease Detection using Computer Vision",
        "Personalized Feed Optimization based on cow characteristics",
        "Bilingual AI Assistant (English/Swahili) for farmer support",
        "Real-time Health Monitoring and Analytics",
        "Production Prediction and Optimization",
        "User-friendly Web Interface"
    ]
    
    for feature in features:
        story.append(Paragraph(f"• {feature}", styles['Normal']))
    
    story.append(PageBreak())
    
    # Technical Specifications
    story.append(Paragraph("TECHNICAL SPECIFICATIONS", styles['Heading2']))
    tech_specs = """
    <b>Backend Technology:</b> Django 5.2.7 (Python)<br/>
    <b>Frontend:</b> HTML5, CSS3, JavaScript, Bootstrap 5.3.0<br/>
    <b>AI Integration:</b> Google Gemini AI, Computer Vision<br/>
    <b>Database:</b> SQLite (Development), PostgreSQL (Production)<br/>
    <b>Deployment:</b> Cloud-ready architecture<br/>
    <b>Security:</b> Django authentication, CSRF protection
    """
    story.append(Paragraph(tech_specs, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Copyright and Developer Info
    story.append(Paragraph("COPYRIGHT INFORMATION", styles['Heading2']))
    copyright_text = f"""
    <b>Software Name:</b> Smart Dairy Platform<br/>
    <b>Version:</b> 1.0.0<br/>
    <b>Developer:</b> KECOSO Smart Dairy Team<br/>
    <b>Copyright Year:</b> {datetime.now().year}<br/>
    <b>License:</b> Proprietary Software<br/>
    <b>Contact:</b> info@kecososmartdairy.com
    """
    story.append(Paragraph(copyright_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("PDF documentation created successfully!")

if __name__ == "__main__":
    create_smart_dairy_documentation()
