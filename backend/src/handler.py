import json
import os
import random

# List of inspirational quotes
QUOTES = [
    "The best way to predict the future is to create it.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Innovation distinguishes between a leader and a follower.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Don't watch the clock; do what it does. Keep going.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Everything you've ever wanted is on the other side of fear.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream big and dare to fail.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "The only person you are destined to become is the person you decide to be."
]

def get_quote(event, context):
    """
    Lambda function that returns a random quote.
    """
    # Check if this is a request for the root path
    if event.get('path') == '/':
        try:
            with open('public/index.html', 'r') as f:
                html_content = f.read()
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'text/html',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': html_content
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Content-Type': 'text/plain',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': 'Error loading page'
            }

    # Return a random quote for /quote endpoint
    random_quote = random.choice(QUOTES)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({"quote": random_quote})
    } 