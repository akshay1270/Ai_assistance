import requests
import spacy
import wikipediaapi

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

def extract_keywords(query):
    """Extract keywords from the user query using spaCy."""
    doc = nlp(query)
    return [token.text for token in doc if token.is_alpha and not token.is_stop]

def answer_factual_question(query):
    """Answer factual questions using the Wikipedia API."""
    keywords = extract_keywords(query)
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent='YourName AI Assistant (https://example.com)'  # Update with your user agent
    )

    try:
        print(f"Querying Wikipedia for: {' '.join(keywords)}")  # Debug statement
        page = wiki_wiki.page(" ".join(keywords))  # Join keywords to create a search string
        if page.exists():
            return page.summary[:500]  # Return the first 500 characters of the summary
        else:
            return "Sorry, I couldn't find any information on that topic."
    except requests.ConnectionError:
        return "Connection error. Please check your internet connection."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """Main function to run the AI Assistant."""
    while True:
        print("\nWelcome to YourName AI Assistant!")
        query = input("Enter your question or type 'exit' to quit: ")
        if query.lower() == 'exit':
            print("Exiting the AI Assistant. Goodbye!")
            break
        response = answer_factual_question(query)
        print(response)

if __name__ == "__main__":
    main()
