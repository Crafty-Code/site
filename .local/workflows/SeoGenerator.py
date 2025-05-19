import os
import sys
import re
import tomli
import tomli_w
import json
from openai import OpenAI
from dotenv import load_dotenv

def extract_front_matter(md_content):
    """
    Extract the front matter from the markdown content.
    """
    match = re.match(r'\+\+\+\n(.*?)\n\+\+\+', md_content, re.DOTALL)
    if match:
        return match.group(1), md_content[match.end():].strip()
    return None, md_content

def generate_seo(content):
    """
    Generate SEO metadata using the existing OpenAI agent.
    """
    # Load environment variables from the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, '.env')
    print(f"Loading environment from: {env_path}")
    load_dotenv(env_path)
    
    # Get API key and assistant ID from environment
    api_key = os.getenv("OPENAI_API_KEY")
    assistant_id = os.getenv("SEO_ASSISTANT_ID")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment")
        raise ValueError("OPENAI_API_KEY must be set in .env file")
    if not assistant_id:
        print("Error: SEO_ASSISTANT_ID not found in environment")
        raise ValueError("SEO_ASSISTANT_ID must be set in .env file")
    
    client = OpenAI(api_key=api_key)
    
    thread = client.beta.threads.create()
    
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="""Please analyze this content and generate SEO metadata in JSON format with the following structure:
        {
            "description": "SEO meta description",
            "keywords": ["keyword1", "keyword2", ...],
            "tags": ["tag1", "tag2", ...],
            "summary": "Use the first paragraph of the content as a summary",
            "og_title": "Open Graph title",
            "og_description": "Open Graph description"
        }

        Content to analyze:

        """ + content
    )
    
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )
    
    # Wait for the run to complete
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_status.status == 'completed':
            break
        elif run_status.status in ['failed', 'cancelled', 'expired']:
            raise Exception(f"Run failed with status: {run_status.status}")
    
    # Get the messages after the run is complete
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    
    # Get the assistant's response
    for message in messages.data:
        if message.role == "assistant":
            try:
                # Parse the JSON response first
                response_text = message.content[0].text.value
                print(f"Received response: {response_text}")
                json_data = json.loads(response_text)
                return json_data
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON response: {e}")
                print(f"Raw response: {response_text}")
                raise
            except Exception as e:
                print(f"Unexpected error: {e}")
                raise
    
    raise Exception("No response from assistant found")

def update_front_matter(front_matter, new_data):
    """
    Update the front matter dictionary with new data.
    """
    if not front_matter:
        front_matter = {}
    else:
        front_matter = tomli.loads(front_matter)

    front_matter.update(new_data)
    return tomli_w.dumps(front_matter)

def insert_seo_metadata_to_file(md_file, seo_data):
    """
    Add the SEO metadata back into the markdown file.
    """
    with open(md_file, 'r') as f:
        md_content = f.read()

    front_matter, body = extract_front_matter(md_content)
    updated_front_matter = update_front_matter(front_matter, seo_data)
    new_md_content = f"+++\n{updated_front_matter}+++\n\n{body}"

    with open(md_file, 'w') as f:
        f.write(new_md_content)

def main(md_file):
    if not os.path.exists(md_file):
        print(f"File {md_file} not found.")
        sys.exit(1)

    # Load environment variables from the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, '.env')
    load_dotenv(env_path)
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set in the .env file.")
        sys.exit(1)

    with open(md_file, 'r') as f:
        md_content = f.read()

    _, body = extract_front_matter(md_content)

    print("Generating SEO metadata using OpenAI agent...")
    seo_data = generate_seo(body)

    print("Inserting SEO metadata back into the markdown file...")
    insert_seo_metadata_to_file(md_file, seo_data)

    print(f"SEO metadata updated for {md_file}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python seo_generator.py <markdown_file.md>")
        sys.exit(1)

    md_file = sys.argv[1]
    main(md_file)
