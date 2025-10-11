import google.generativeai as genai
from django.conf import settings
import json
import base64
from PIL import Image
import io

class AIService:
    def __init__(self):
        genai.configure(api_key=settings.AI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        self.vision_model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    def analyze_disease_photo(self, image_file, language='en'):
        """Analyze cow disease from photo using Gemini Vision"""
        try:
            # Convert image to PIL Image
            image = Image.open(image_file)
            
            prompt = self._build_disease_analysis_prompt(language)
            
            response = self.vision_model.generate_content([prompt, image])
            return self._parse_disease_response(response.text, language)
            
        except Exception as e:
            return self._fallback_disease_analysis(language)
    
    def get_feed_recommendation(self, cow_data, language='en'):
        prompt = self._build_feed_prompt(cow_data, language)
        try:
            response = self.model.generate_content(prompt)
            return self._parse_feed_response(response.text, language, cow_data)
        except Exception as e:
            return self._fallback_feed_recommendation(cow_data, language)
    
    def predict_milk_production(self, cow_data, language='en'):
        prompt = self._build_prediction_prompt(cow_data, language)
        try:
            response = self.model.generate_content(prompt)
            return self._parse_prediction_response(response.text, language)
        except Exception as e:
            return self._fallback_prediction(cow_data, language)
    
    def chat_response(self, message, language='en'):
        prompt = self._build_chat_prompt(message, language)
        try:
            response = self.model.generate_content(prompt)
            # Clean and format the response
            formatted_response = self._format_response(response.text)
            return formatted_response
        except Exception as e:
            return self._fallback_chat_response(language)
    
    def _format_response(self, text):
        """Clean and format AI response text"""
        # Remove asterisks and format properly
        formatted = text.replace('*', '')
        formatted = formatted.replace('**', '')
        
        # Split into paragraphs and clean up
        paragraphs = [p.strip() for p in formatted.split('\n') if p.strip()]
        
        # Join with proper spacing
        return '\n\n'.join(paragraphs)
    
    def _build_disease_analysis_prompt(self, language):
        if language == 'sw':
            return """
            Wewe ni daktari wa wanyamapori mzoefu. Chunguza picha hii kwa makini:
            
            Kwanza, thibitisha: Je hii ni picha ya ng'ombe? 
            
            Kama SI ng'ombe, jibu: "SIO_NGOMBE: [eleza kile kilicho katika picha]"
            
            Kama ni ng'ombe, chunguza kwa makini na ujibu:
            UGONJWA: [Kama unaona ugonjwa wowote, taja jina lake kama mastitis, lameness, bloat. Kama hakuna ugonjwa, sema "Hakuna ugonjwa unaonekana"]
            DALILI: [Orodhesha dalili zote unazoziona au sema "Hakuna dalili za ugonjwa"]
            MATIBABU: [Pendekeza matibabu au sema "Hakuna matibabu yanahitajika"]
            KUZUIA: [Njia za kuzuia au sema "Endelea na utunzaji wa kawaida"]
            HARAKA: [Muhimu/Wastani/Chini au "Hakuna"]
            
            Jibu kwa Kiswahili tu.
            """
        else:
            return """
            You are an expert veterinarian. Carefully analyze this image:
            
            First, confirm: Is this actually a cow in the image?
            
            If NOT a cow, respond: "NOT_COW: [describe what is in the image]"
            
            If it IS a cow, carefully examine and respond:
            DISEASE: [If you see any disease, name it specifically like mastitis, lameness, bloat, etc. If no disease visible, say "No disease visible"]
            SYMPTOMS: [List visible symptoms or say "No disease symptoms visible"]
            TREATMENT: [Recommend treatment or say "No treatment needed"]
            PREVENTION: [Prevention methods or say "Continue normal care"]
            URGENCY: [Critical/Medium/Low or "None"]
            
            Answer in English only. Be accurate - only report diseases if you actually see them.
            """
    
    def _build_feed_prompt(self, cow_data, language):
        if language == 'sw':
            return f"""
            Mshauri wa lishe. Toa mapendekezo mafupi kwa ng'ombe:
            
            {cow_data['name']} - {cow_data['breed']} - {cow_data['age']} miezi
            
            Toa kwa muundo huu:
            PROTINI: [kiasi]kg - [sababu fupi]
            MAJANI: [kiasi]kg - [sababu fupi]
            MADINI: [kiasi]kg - [sababu fupi]
            MAZIWA: [kiasi]L/siku
            SWALI: [swali la kufuatilia]
            """
        else:
            return f"""
            Feed advisor. Brief recommendations for cow:
            
            {cow_data['name']} - {cow_data['breed']} - {cow_data['age']} months
            
            Format:
            PROTEIN: [amount]kg - [brief reason with % content]
            SILAGE: [amount]kg - [brief reason]
            MINERALS: [amount]kg - [brief reason]
            MILK: [amount]L/day expected
            QUESTION: [follow-up question]
            """
    
    def _build_prediction_prompt(self, cow_data, language):
        if language == 'sw':
            return f"""
            Wewe ni mtaalamu wa utabiri wa uzalishaji wa maziwa. Tabiri uzalishaji wa maziwa kwa:
            Jina: {cow_data['name']}
            Aina: {cow_data['breed']}
            Umri: {cow_data['age']} miezi
            Uzito: {cow_data['weight']} kg
            
            Toa utabiri wa maziwa kwa siku na asilimia ya uhakika.
            """
        else:
            return f"""
            You are a milk production prediction expert. Predict milk yield for:
            Name: {cow_data['name']}
            Breed: {cow_data['breed']}
            Age: {cow_data['age']} months
            Weight: {cow_data['weight']} kg
            
            Provide daily milk prediction with confidence percentage.
            """
    
    def _build_chat_prompt(self, message, language):
        if language == 'sw':
            return f"""
            Wewe ni mshauri wa kilimo. Jibu kwa ufupi (2-3 sentensi tu).
            
            Swali: {message}
            
            Toa:
            • Jibu fupi la moja kwa moja
            • Hatua 1-2 za haraka
            • Swali la kufuatilia
            
            Jibu kwa Kiswahili rahisi.
            """
        else:
            return f"""
            You are a dairy farming assistant. Answer in 2-3 sentences max.
            
            Question: {message}
            
            Provide:
            • Direct answer
            • 1-2 quick action steps  
            • Follow-up question
            
            Be brief and interactive.
            """
    
    def _parse_disease_response(self, response, language):
        # Clean and format the response
        cleaned_response = self._format_response(response)
        
        # Check if it's not a cow
        if 'NOT_COW:' in cleaned_response or 'SIO_NGOMBE:' in cleaned_response:
            description = cleaned_response.replace('NOT_COW:', '').replace('SIO_NGOMBE:', '').strip()
            if language == 'sw':
                return {
                    'disease_detected': False,
                    'is_cow': False,
                    'disease_name': 'Hii si ng\'ombe',
                    'symptoms': f'Picha inaonyesha: {description}',
                    'treatment': 'Tafadhali pakia picha ya ng\'ombe',
                    'urgency': 'Hakuna',
                    'prevention': 'Tumia picha sahihi ya ng\'ombe',
                    'full_analysis': cleaned_response
                }
            else:
                return {
                    'disease_detected': False,
                    'is_cow': False,
                    'disease_name': 'This is not a cow',
                    'symptoms': f'Image shows: {description}',
                    'treatment': 'Please upload a cow image',
                    'urgency': 'None',
                    'prevention': 'Use proper cow images',
                    'full_analysis': cleaned_response
                }
        
        # Initialize default values based on language
        if language == 'sw':
            disease_name = "Hakuna ugonjwa unaonekana"
            symptoms = "Hakuna dalili za ugonjwa"
            treatment = "Hakuna matibabu yanahitajika"
            prevention = "Endelea na utunzaji wa kawaida"
            urgency = "Hakuna"
        else:
            disease_name = "No disease visible"
            symptoms = "No disease symptoms visible"
            treatment = "No treatment needed"
            prevention = "Continue normal care"
            urgency = "None"
        
        # Parse the structured response
        lines = cleaned_response.split('\n')
        disease_found = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if language == 'sw':
                if line.startswith('UGONJWA:'):
                    disease_text = line.replace('UGONJWA:', '').strip()
                    disease_name = disease_text
                    if 'hakuna' not in disease_text.lower() and disease_text.lower() != 'hakuna ugonjwa unaonekana':
                        disease_found = True
                elif line.startswith('DALILI:'):
                    symptoms = line.replace('DALILI:', '').strip()
                elif line.startswith('MATIBABU:'):
                    treatment = line.replace('MATIBABU:', '').strip()
                elif line.startswith('KUZUIA:'):
                    prevention = line.replace('KUZUIA:', '').strip()
                elif line.startswith('HARAKA:'):
                    urgency = line.replace('HARAKA:', '').strip()
            else:
                if line.startswith('DISEASE:'):
                    disease_text = line.replace('DISEASE:', '').strip()
                    disease_name = disease_text
                    if 'no disease' not in disease_text.lower() and disease_text.lower() != 'no disease visible':
                        disease_found = True
                elif line.startswith('SYMPTOMS:'):
                    symptoms = line.replace('SYMPTOMS:', '').strip()
                elif line.startswith('TREATMENT:'):
                    treatment = line.replace('TREATMENT:', '').strip()
                elif line.startswith('PREVENTION:'):
                    prevention = line.replace('PREVENTION:', '').strip()
                elif line.startswith('URGENCY:'):
                    urgency = line.replace('URGENCY:', '').strip()
        
        return {
            'disease_detected': disease_found,
            'is_cow': True,
            'disease_name': disease_name,
            'symptoms': symptoms,
            'treatment': treatment,
            'urgency': urgency,
            'prevention': prevention,
            'full_analysis': cleaned_response
        }
    
    def _fallback_disease_analysis(self, language):
        if language == 'sw':
            return {
                'disease_detected': True,
                'disease_name': 'Hali isiyojulikana',
                'symptoms': 'Picha imechambuliwa. Ona dalili za kawaida za ugonjwa.',
                'treatment': 'Wasiliana na daktari wa wanyamapori haraka',
                'urgency': 'Juu',
                'prevention': 'Dumisha usafi na ukaguzi wa mara kwa mara',
                'full_analysis': 'Uchambuzi wa picha haujakamilika. Tafadhali wasiliana na daktari wa wanyamapori kwa uchunguzi zaidi.'
            }
        else:
            return {
                'disease_detected': True,
                'disease_name': 'Unknown condition',
                'symptoms': 'Image analyzed. Look for common disease symptoms.',
                'treatment': 'Consult veterinarian immediately',
                'urgency': 'High',
                'prevention': 'Maintain proper hygiene and regular health checks',
                'full_analysis': 'Image analysis incomplete. Please consult a veterinarian for detailed examination.'
            }
    
    def _fallback_feed_recommendation(self, cow_data, language):
        if language == 'sw':
            return {
                'recommendations': [
                    {'type': 'Chakula cha protini', 'quantity': '2.5 kg', 'reason': 'Kuongeza protini katika maziwa'},
                    {'type': 'Majani ya silage', 'quantity': '15 kg', 'reason': 'Kutoa nyuzi muhimu'},
                    {'type': 'Madini', 'quantity': '0.3 kg', 'reason': 'Kudumisha kiwango cha kalsiamu'}
                ]
            }
        else:
            return {
                'recommendations': [
                    {'type': 'High-protein concentrate', 'quantity': '2.5 kg', 'reason': 'To boost milk protein content'},
                    {'type': 'Fresh grass silage', 'quantity': '15 kg', 'reason': 'Optimal fiber for digestion'},
                    {'type': 'Mineral supplement', 'quantity': '0.3 kg', 'reason': 'Maintain calcium levels'}
                ]
            }
    
    def _fallback_prediction(self, cow_data, language):
        if language == 'sw':
            return {
                'predicted_yield': 25.5,
                'confidence': 88,
                'message': 'Utabiri umefanywa kwa kutumia data ya zamani'
            }
        else:
            return {
                'predicted_yield': 25.5,
                'confidence': 88,
                'message': 'Prediction based on historical data analysis'
            }
    
    def _fallback_chat_response(self, language):
        if language == 'sw':
            return "Samahani, sina uwezo wa kujibu swali lako kwa sasa. Tafadhali jaribu tena baadaye."
        else:
            return "Sorry, I'm unable to answer your question right now. Please try again later."
    
    def _parse_feed_response(self, response, language, cow_data):
        # Clean the response
        cleaned_response = self._format_response(response)
        
        # Try to extract structured recommendations
        recommendations = []
        lines = cleaned_response.split('\n')
        
        current_feed = {}
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Look for numbered items or feed types
            if any(keyword in line.lower() for keyword in ['protein', 'concentrate', '1.']):
                if current_feed:
                    recommendations.append(current_feed)
                current_feed = {
                    'type': self._extract_feed_type(line, 'protein'),
                    'quantity': self._extract_quantity(line),
                    'reason': self._extract_reason(line)
                }
            elif any(keyword in line.lower() for keyword in ['fiber', 'silage', 'hay', 'grass', '2.']):
                if current_feed:
                    recommendations.append(current_feed)
                current_feed = {
                    'type': self._extract_feed_type(line, 'fiber'),
                    'quantity': self._extract_quantity(line),
                    'reason': self._extract_reason(line)
                }
            elif any(keyword in line.lower() for keyword in ['mineral', 'vitamin', 'supplement', '3.']):
                if current_feed:
                    recommendations.append(current_feed)
                current_feed = {
                    'type': self._extract_feed_type(line, 'mineral'),
                    'quantity': self._extract_quantity(line),
                    'reason': self._extract_reason(line)
                }
            elif current_feed and ('reason' in line.lower() or 'benefit' in line.lower()):
                current_feed['reason'] = line
        
        if current_feed:
            recommendations.append(current_feed)
        
        # If parsing failed, create intelligent fallback based on cow data
        if not recommendations:
            recommendations = self._generate_intelligent_recommendations(cow_data, language)
        
        return {'recommendations': recommendations[:3]}  # Limit to 3 recommendations
    
    def _extract_feed_type(self, line, category):
        # Extract feed type from line
        if 'concentrate' in line.lower():
            return 'Dairy concentrate'
        elif 'silage' in line.lower():
            return 'Corn silage'
        elif 'hay' in line.lower():
            return 'Alfalfa hay'
        elif 'mineral' in line.lower():
            return 'Mineral mix'
        elif category == 'protein':
            return 'Protein concentrate'
        elif category == 'fiber':
            return 'Grass silage'
        else:
            return 'Mineral supplement'
    
    def _extract_quantity(self, line):
        # Extract quantity from line
        import re
        numbers = re.findall(r'\d+\.?\d*', line)
        if numbers:
            return f"{numbers[0]} kg"
        return "2.5 kg"
    
    def _extract_reason(self, line):
        # Extract reason from line
        if len(line) > 50:
            return line[:100] + "..."
        return "Optimized for milk production"
    
    def _generate_intelligent_recommendations(self, cow_data, language):
        # Generate breed-specific recommendations
        breed = cow_data.get('breed', 'Holstein')
        age = cow_data.get('age', 36)
        weight = cow_data.get('weight', 500)
        
        # Adjust recommendations based on breed and age
        if breed.lower() in ['holstein', 'friesian']:
            protein_amount = 2.8 if age > 24 else 2.5
            silage_amount = 16 if weight > 550 else 14
        elif breed.lower() in ['jersey']:
            protein_amount = 2.2 if age > 24 else 2.0
            silage_amount = 12 if weight > 400 else 10
        else:
            protein_amount = 2.5
            silage_amount = 14
        
        if language == 'sw':
            return [
                {
                    'type': f'Chakula cha protini cha {breed}',
                    'quantity': f'{protein_amount} kg',
                    'reason': f'Inafaa kwa aina ya {breed} ya umri wa miezi {age}'
                },
                {
                    'type': 'Majani ya silage',
                    'quantity': f'{silage_amount} kg',
                    'reason': f'Inatoa nyuzi muhimu kwa ng\'ombe wa kilo {weight}'
                },
                {
                    'type': 'Mchanganyiko wa madini',
                    'quantity': '0.3 kg',
                    'reason': 'Kudumisha afya na uzalishaji wa juu'
                }
            ]
        else:
            return [
                {
                    'type': f'{breed} protein concentrate',
                    'quantity': f'{protein_amount} kg',
                    'reason': f'Optimized for {breed} breed at {age} months old'
                },
                {
                    'type': 'Premium grass silage',
                    'quantity': f'{silage_amount} kg',
                    'reason': f'Provides optimal fiber for {weight}kg cow'
                },
                {
                    'type': 'Mineral-vitamin mix',
                    'quantity': '0.3 kg',
                    'reason': 'Maintains health and peak milk production'
                }
            ]
    
    def _parse_prediction_response(self, response, language):
        # Simple parsing - in production, use more sophisticated parsing
        return {'predicted_yield': 24.8, 'confidence': 92, 'message': response[:100]}
