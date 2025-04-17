import os
import sys
import re
import yaml
import time
import concurrent.futures
from openai import OpenAI
from dotenv import load_dotenv

# Supported languages and their codes
SUPPORTED_LANGUAGES = {
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'italian': 'it',
    'irish': 'ie'
}

# Maximum number of parallel translations
MAX_WORKERS = 3

def extract_front_matter(md_content):
    """
    Extract the front matter from the markdown content.
    """
    match = re.match(r'---\n(.*?)\n---', md_content, re.DOTALL)
    if match:
        return match.group(1), md_content[match.end():].strip()
    return None, md_content

def translate_content(content, target_language):
    """
    Translate content to the target language using OpenAI's API.
    """
    # Load environment variables
    load_dotenv()
    
    # Get API key and assistant ID from environment
    api_key = os.getenv("OPENAI_API_KEY")
    translator_assistant_id = os.getenv("TRANSLATOR_ASSISTANT_ID")
    
    if not api_key or not translator_assistant_id:
        raise ValueError("OPENAI_API_KEY and TRANSLATOR_ASSISTANT_ID must be set in .env file")
    
    client = OpenAI(api_key=api_key)
    
    # Create a thread
    thread = client.beta.threads.create()
    
    # Add the content to translate to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"""Please translate the following content to {target_language}. 
Maintain the original formatting, including markdown syntax, headings, lists, and code blocks. 
Preserve any technical terms that should not be translated.

Return the translation in JSON format with a single key 'translation' containing the translated text.

Content to translate:

{content}"""
    )
    
    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=translator_assistant_id
    )
    
    # Wait for the run to complete with progress indicator
    print(f"Translation to {target_language} in progress...", end="", flush=True)
    dots = 0
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        
        # Show progress indicator
        if dots < 3:
            print(".", end="", flush=True)
            dots += 1
        else:
            print("\b\b\b...", end="", flush=True)
            dots = 0
        
        if run_status.status == 'completed':
            print("\nTranslation completed!")
            break
        elif run_status.status in ['failed', 'cancelled', 'expired']:
            print("\nTranslation failed!")
            raise Exception(f"Run failed with status: {run_status.status}")
        
        time.sleep(1)  # Wait a second before checking again
    
    # Get the messages after the run is complete
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    # Get the assistant's response
    for message in messages.data:
        if message.role == "assistant":
            # Parse the JSON response
            try:
                response_text = message.content[0].text.value
                response_json = yaml.safe_load(response_text)
                return response_json.get('translation', response_text)
            except Exception as e:
                print(f"Error parsing JSON response: {e}")
                return message.content[0].text.value
    
    raise Exception("No response from assistant found")

def translate_front_matter(front_matter, target_language):
    """
    Translate the front matter content to the target language.
    """
    if not front_matter:
        return None
    
    try:
        # Parse the front matter
        front_matter_dict = yaml.safe_load(front_matter)
        
        # Fields to translate
        fields_to_translate = [
            'title',
            'description',
            'keywords',
            'og_title',
            'og_description',
            'twitter_title',
            'twitter_description'
        ]
        
        # Translate each field
        for field in fields_to_translate:
            if field in front_matter_dict:
                if field == 'keywords':
                    # Handle keywords array
                    if isinstance(front_matter_dict[field], list):
                        translated_keywords = []
                        for keyword in front_matter_dict[field]:
                            try:
                                translated_keyword = translate_content(keyword, target_language)
                                translated_keywords.append(translated_keyword)
                            except Exception as e:
                                print(f"Error translating keyword '{keyword}': {e}")
                                translated_keywords.append(keyword)
                        front_matter_dict[field] = translated_keywords
                else:
                    # Handle string fields
                    try:
                        translated_text = translate_content(front_matter_dict[field], target_language)
                        front_matter_dict[field] = translated_text
                    except Exception as e:
                        print(f"Error translating {field}: {e}")
        
        # Add translation metadata
        front_matter_dict['translated'] = True
        front_matter_dict['original_language'] = 'en'
        front_matter_dict['translated_to'] = target_language
        
        # Convert back to YAML
        return yaml.dump(front_matter_dict, default_flow_style=False)
    
    except Exception as e:
        print(f"Error translating front matter: {e}")
        return front_matter

def get_language_code(target_language):
    """
    Get the language code for the target language.
    """
    lang_code = target_language.lower()
    
    if lang_code in SUPPORTED_LANGUAGES:
        return SUPPORTED_LANGUAGES[lang_code]
    else:
        raise ValueError(f"Unsupported language: {target_language}. Supported languages are: {', '.join(SUPPORTED_LANGUAGES.keys())}")

def translate_markdown_file(md_file, target_language):
    """
    Translate a markdown file to the target language.
    """
    # Check if the file exists
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"File not found: {md_file}")
    
    # Get the language code
    try:
        lang_code = get_language_code(target_language)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
    # Read the markdown file
    try:
        with open(md_file, 'r') as f:
            md_content = f.read()
    except Exception as e:
        raise IOError(f"Error reading file {md_file}: {e}")
    
    # Extract front matter and body
    front_matter, body = extract_front_matter(md_content)
    
    # Translate the front matter
    translated_front_matter = translate_front_matter(front_matter, target_language)
    
    # Translate the content
    try:
        translated_body = translate_content(body, target_language)
    except Exception as e:
        print(f"Translation error for {target_language}: {e}")
        return None
    
    # Get the relative path components
    file_path = os.path.normpath(md_file)
    path_parts = file_path.split(os.sep)
    
    # Find the 'content' directory in the path
    try:
        content_index = path_parts.index('content')
    except ValueError:
        raise ValueError("File must be in a subdirectory of 'content'")
    
    # Remove 'content' and any language code directory (like 'en') from the path
    relative_path = path_parts[content_index + 2:]  # Skip 'content' and language directory
    
    # Create the new path with the target language code
    new_path_parts = ['content', lang_code] + relative_path
    translated_file = os.path.join(*new_path_parts)
    
    # Create the directory structure if it doesn't exist
    os.makedirs(os.path.dirname(translated_file), exist_ok=True)
    
    # Write the translated content to the new file
    try:
        with open(translated_file, 'w') as f:
            f.write(f"---\n{translated_front_matter}---\n\n{translated_body}")
    except Exception as e:
        raise IOError(f"Error writing translated file {translated_file}: {e}")
    
    print(f"Translated file saved to: {translated_file}")
    return translated_file

def translate_file_worker(args):
    """
    Worker function for parallel translation.
    """
    md_file, target_language = args
    try:
        print(f"\nTranslating to {target_language}...")
        result = translate_markdown_file(md_file, target_language)
        return target_language, result, None
    except Exception as e:
        return target_language, None, str(e)

def main():
    if len(sys.argv) != 2:
        print("Usage: python Translator.py <markdown_file.md>")
        print(f"Supported languages: {', '.join(SUPPORTED_LANGUAGES.keys())}")
        sys.exit(1)
    
    md_file = sys.argv[1]
    
    # Skip English as it's the source language
    target_languages = list(SUPPORTED_LANGUAGES.keys())
    
    successful_translations = 0
    failed_translations = 0
    
    # Create arguments for parallel processing
    translation_args = [(md_file, lang) for lang in target_languages]
    
    # Run translations in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_lang = {executor.submit(translate_file_worker, args): args[1] for args in translation_args}
        
        for future in concurrent.futures.as_completed(future_to_lang):
            lang = future_to_lang[future]
            try:
                lang, result, error = future.result()
                if result:
                    successful_translations += 1
                    print(f"✓ Successfully translated to {lang}")
                else:
                    failed_translations += 1
                    print(f"✗ Failed to translate to {lang}: {error}")
            except Exception as e:
                failed_translations += 1
                print(f"✗ Error translating to {lang}: {e}")
    
    print(f"\nTranslation Summary:")
    print(f"Successful translations: {successful_translations}")
    print(f"Failed translations: {failed_translations}")
    print(f"Total languages attempted: {len(target_languages)}")

if __name__ == '__main__':
    main() 