"""
Content Personalization Service
Adjusts content difficulty based on user's software and hardware background
"""

from typing import Dict, Optional

class PersonalizationService:
    """Personalizes content based on user background"""
    
    def __init__(self):
        # Define content adjustments for different levels
        self.adjustments = {
            "beginner": {
                "tone": "simple",
                "details": "minimal",
                "examples": "many",
                "prerequisites": "explained"
            },
            "intermediate": {
                "tone": "balanced",
                "details": "moderate",
                "examples": "some",
                "prerequisites": "referenced"
            },
            "advanced": {
                "tone": "technical",
                "details": "comprehensive",
                "examples": "few",
                "prerequisites": "assumed"
            }
        }
    
    def personalize_prompt(
        self,
        original_query: str,
        software_background: str,
        hardware_background: str
    ) -> str:
        """
        Enhance the RAG prompt with personalization instructions
        """
        # Determine overall user level (use the lower of the two)
        levels = ["beginner", "intermediate", "advanced"]
        sw_idx = levels.index(software_background) if software_background in levels else 1
        hw_idx = levels.index(hardware_background) if hardware_background in levels else 1
        user_level = levels[min(sw_idx, hw_idx)]
        
        adjustments = self.adjustments[user_level]
        
        # Create personalization instructions
        personalization_prompt = f"""
PERSONALIZATION CONTEXT:
- User's software background: {software_background}
- User's hardware background: {hardware_background}
- Response style: {adjustments['tone']}
- Technical details: {adjustments['details']}
- Code examples: {adjustments['examples']}
- Prerequisites: {adjustments['prerequisites']}

USER QUERY: {original_query}

Please adapt your response to match the user's background level. """
        
        if user_level == "beginner":
            personalization_prompt += """
For beginners:
- Explain technical terms in simple language
- Provide step-by-step instructions
- Include many practical examples
- Avoid assuming prior knowledge
- Use analogies when helpful"""
        
        elif user_level == "intermediate":
            personalization_prompt += """
For intermediate users:
- Balance theory with practice
- Reference prerequisites but don't over-explain
- Provide moderate technical depth
- Focus on practical application"""
        
        else:  # advanced
            personalization_prompt += """
For advanced users:
- Use technical terminology freely
- Provide comprehensive details
- Focus on edge cases and optimization
- Assume strong foundational knowledge
- Reference research papers if relevant"""
        
        return personalization_prompt
    
    def get_chapter_intro(
        self,
        chapter_title: str,
        software_background: str,
        hardware_background: str
    ) -> Dict[str, str]:
        """
        Generate personalized chapter introduction
        """
        levels = ["beginner", "intermediate", "advanced"]
        sw_idx = levels.index(software_background) if software_background in levels else 1
        hw_idx = levels.index(hardware_background) if hardware_background in levels else 1
        user_level = levels[min(sw_idx, hw_idx)]
        
        intros = {
            "beginner": {
                "greeting": f"Welcome to **{chapter_title}**! 👋",
                "message": "This chapter is customized for your background. We'll explain concepts step-by-step with plenty of examples.",
                "tip": "💡 Don't worry if some terms are new - we'll explain everything as we go!"
            },
            "intermediate": {
                "greeting": f"**{chapter_title}** 🚀",
                "message": "This content is tailored to your experience level. We'll balance theory with practical implementation.",
                "tip": "💡 Feel free to skip sections you're already familiar with."
            },
            "advanced": {
                "greeting": f"**{chapter_title}** ⚡",
                "message": "Advanced content ahead. We'll dive deep into technical details and edge cases.",
                "tip": "💡 This  chapter assumes strong foundational knowledge."
            }
        }
        
        return intros[user_level]
