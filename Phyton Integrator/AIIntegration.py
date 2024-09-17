import requests
import openai

INSTAGRAM_ACCESS_TOKEN = 'INSTAGRAM_api_token'
INSTAGRAM_API_URL = 'https://graph.instagram.com/me/media?fields=id,caption&access_token='

openai.api_key = 'OPENAI_api_key'

def fetch_instagram_posts():
    """
    Fetch the latest posts from the authenticated Instagram user
    """
    url = INSTAGRAM_API_URL + INSTAGRAM_ACCESS_TOKEN
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error fetching Instagram posts: {response.status_code}")
        return []

def summarize_text(text):
    """
    Summarize the provided text using OpenAI's GPT model.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Summarize the following text:\n\n{text}",
            max_tokens=100,
            temperature=0.5
        )
        summary = response.choices[0].text.strip()
        return summary
    except Exception as e:
        print(f"Error with OpenAI API: {str(e)}")
        return None

def main():
    posts = fetch_instagram_posts()

    if not posts:
        print("No posts available.")
        return

    for post in posts:
        caption = post.get('caption', 'No caption available.')
        post_id = post['id']
        
        print(f"\nPost ID: {post_id}")
        print(f"Original Caption: {caption}")

        summary = summarize_text(caption)
        if summary:
            print(f"Summary: {summary}")
        else:
            print("Could not generate summary.")

if __name__ == "__main__":
    main()