
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IntentClassifier:
    def __init__(self):
        # In a real scenario, this would load a trained model or complex rule sets.
        # For this example, we'll use a simple keyword-based approach.
        self.keywords = {
            "POLICY_QUERY": ["policy", "scheme", "program", "regulation"],
            "ELIGIBILITY_CHECK": ["eligible", "qualify", "requirements", "am I"],
            "BENEFIT_MATCH": ["benefit", "aid", "support", "help with"],
            "APPLICATION_GUIDE": ["apply", "application", "how to", "guide", "steps"],
            "OUT_OF_SCOPE": ["hello", "hi", "weather", "news", "random"],
        }

    def classify(self, message: str) -> str:
        message_lower = message.lower()
        
        # Check for OUT_OF_SCOPE first as it's a hard stop condition
        for keyword in self.keywords["OUT_OF_SCOPE"]:
            if keyword in message_lower:
                logging.info(f"Classified message as OUT_OF_SCOPE: '{message}'")
                return "OUT_OF_SCOPE"

        for intent, keywords in self.keywords.items():
            if intent == "OUT_OF_SCOPE": # Already checked
                continue
            for keyword in keywords:
                if keyword in message_lower:
                    logging.info(f"Classified message as {intent}: '{message}'")
                    return intent
        
        # Default to OUT_OF_SCOPE if no other intent matches clear keywords
        logging.info(f"Classified message as OUT_OF_SCOPE (default): '{message}'")
        return "OUT_OF_SCOPE"

def handle_message(message: str) -> str:
    """
    Processes an incoming message, classifies it, and returns the appropriate response.
    """
    classifier = IntentClassifier()
    intent = classifier.classify(message)
    
    response = ""
    
    if intent == "OUT_OF_SCOPE":
        response = "I can only help with government schemes and benefits."
    else:
        # In a real skill, you would now proceed to call other tools/skills
        # based on the 'intent' and add the prefix.
        # For demonstration, we simulate a placeholder response.
        response = f"This message is about {intent}. Further processing would happen here."
        
    return f"[INTENT: {intent}] {response}"

# Example Usage (for testing purposes):
if __name__ == "__main__":
    test_messages = [
        "What is the policy for student loans?",
        "Am I eligible for unemployment benefits?",
        "How do I apply for a housing grant?",
        "Tell me about the new healthcare initiative.",
        "Can you help me find a job?",
        "Hello there!",
        "What's the weather today?",
        "I need information on the latest regulations.",
        "What are the requirements to get a visa?",
        "This is completely unrelated to government services."
    ]

    for msg in test_messages:
        print(f"User: {msg}")
        print(f"Agent: {handle_message(msg)}
")
