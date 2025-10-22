#!/usr/bin/env python3
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
import os

def create_copyright_documentation():
    doc = SimpleDocTemplate("Smart_Dairy_Copyright_Registration.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # 1. TITLE PAGE
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, 
                                alignment=1, spaceAfter=20, textColor=colors.darkblue)
    subtitle_style = ParagraphStyle('Subtitle', parent=styles['Heading2'], 
                                   alignment=1, spaceAfter=30)
    
    story.append(Paragraph("SMART DAIRY", title_style))
    story.append(Paragraph("AI-Powered Dairy Management Platform", subtitle_style))
    story.append(Spacer(1, 30))
    
    # Version and Authors
    info_style = ParagraphStyle('Info', parent=styles['Normal'], alignment=1, fontSize=12)
    story.append(Paragraph("Version 1.0", info_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Software Authors: Smart Dairy Development Team", info_style))
    story.append(Paragraph("Current Software Owner: Smart Dairy Development Team", info_style))
    story.append(Paragraph(f"Documentation Date: {datetime.now().strftime('%B %d, %Y')}", info_style))
    story.append(PageBreak())
    
    # 2. ABSTRACT SECTION
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
    
    # 4. ACTUAL DOCUMENTATION WITH SCREENSHOTS
    story.append(Paragraph("SOFTWARE DOCUMENTATION", styles['Heading1']))
    story.append(Spacer(1, 20))
    
    # 4a. Access/Login/Loading
    story.append(Paragraph("4.1 Accessing the Software", styles['Heading2']))
    access_text = """Smart Dairy is accessed through a web browser by navigating to the application URL. 
    The landing page provides an overview of the platform's capabilities and allows users to register or login."""
    story.append(Paragraph(access_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    # Main Interface Screenshot
    story.append(Paragraph("Landing Page Interface:", styles['Heading3']))
    if os.path.exists("interface.png"):
        img1 = Image("interface.png", width=6.5*inch, height=3.5*inch)
        story.append(img1)
    story.append(Spacer(1, 15))
    
    login_text = """The main interface showcases the "AI-Powered Dairy Solutions" with options to start a free trial 
    or learn more. The navigation includes Home, Features, How It Works, Testimonials, About, Language selection, 
    Login, and Register buttons. The interface displays key features like AI Analysis, Health Check, and Production Stats."""
    story.append(Paragraph(login_text, styles['Normal']))
    story.append(PageBreak())
    
    # 4b. Key Interfaces and Functionalities
    story.append(Paragraph("4.2 AI Feed Personalization System", styles['Heading2']))
    feed_text = """The AI Feed Personalization feature allows farmers to generate customized nutrition plans 
    for individual cows based on their unique characteristics including breed, age, weight, and health condition."""
    story.append(Paragraph(feed_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    if os.path.exists("AI feed personalization.png"):
        img2 = Image("AI feed personalization.png", width=6.5*inch, height=3.5*inch)
        story.append(img2)
    story.append(Spacer(1, 15))
    
    feed_desc = """This interface shows cow status categories (Expecting calf, Currently milking, Rest before calving, 
    Recovering) with a selected cow named Kairo. The system displays the cow's production status as "High Producer" 
    and provides an AI-Powered Personalized Feed Plan button to generate custom nutrition recommendations."""
    story.append(Paragraph(feed_desc, styles['Normal']))
    story.append(PageBreak())
    
    story.append(Paragraph("4.3 AI Disease Detection System", styles['Heading2']))
    disease_text = """The AI Disease Detection feature uses computer vision to analyze uploaded cow photos 
    and identify potential health issues, providing immediate diagnostic insights and treatment recommendations."""
    story.append(Paragraph(disease_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    if os.path.exists("disease detection system.png"):
        img3 = Image("disease detection system.png", width=6.5*inch, height=4*inch)
        story.append(img3)
    story.append(Spacer(1, 15))
    
    disease_desc = """The disease detection interface allows farmers to upload cow photos for AI analysis. 
    The system provides comprehensive analysis results including Disease Status (Mastitis detected), 
    Urgency Level (Critical - call veterinarian now), detailed Symptoms description, Treatment recommendations, 
    and Prevention measures. The interface supports multiple languages as shown by the English language selector."""
    story.append(Paragraph(disease_desc, styles['Normal']))
    story.append(PageBreak())
    
    story.append(Paragraph("4.4 Bilingual AI Assistant", styles['Heading2']))
    chatbot_text = """The Smart Dairy AI Assistant provides bilingual support in English and Swahili, 
    offering farmers instant access to dairy farming expertise and guidance."""
    story.append(Paragraph(chatbot_text, styles['Normal']))
    story.append(Spacer(1, 15))
    
    if os.path.exists("bilingualchatbot.png"):
        img4 = Image("bilingualchatbot.png", width=6.5*inch, height=3.5*inch)
        story.append(img4)
    story.append(Spacer(1, 15))
    
    chatbot_desc = """The AI Assistant interface features a conversational chatbot that introduces itself as 
    "Smart Dairy AI assistant" ready to help with dairy farming, cow health, feed management, or milk production questions. 
    The interface includes quick question buttons for common inquiries like "How to increase milk production?", 
    "What feed is best for Holstein cows?", and "Signs of cow illness?". The system supports language switching 
    between English and other local languages."""
    story.append(Paragraph(chatbot_desc, styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Conclusion
    conclusion_text = """Smart Dairy represents a comprehensive solution for modern dairy farm management, 
    integrating artificial intelligence with user-friendly interfaces to provide farmers with powerful tools 
    for optimizing their operations. The software's key functionalities work together to create an ecosystem 
    that supports informed decision-making and improved farm productivity."""
    story.append(Paragraph(conclusion_text, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("Smart Dairy Copyright Registration Documentation created successfully!")

if __name__ == "__main__":
    create_copyright_documentation()
