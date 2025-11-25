#!/usr/bin/env python3
"""
Diagnostic script to test OpenAI API connection
"""
import sys
try:
    from openai import OpenAI
    from config import apikey
    print("✓ Imports successful")
    
    # Test API key format
    if apikey.startswith("sk-proj-"):
        print("✓ API key format looks correct (project key)")
    elif apikey.startswith("sk-"):
        print("✓ API key format looks correct")
    else:
        print("❌ API key format is invalid")
        sys.exit(1)
    
    # Initialize client
    client = OpenAI(api_key=apikey)
    print("✓ OpenAI client initialized")
    
    # Test simple API call
    print("\n🔍 Testing OpenAI API connection...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Hello, this is a test. Please respond with 'API connection successful'"}
            ],
            max_tokens=50
        )
        
        response_text = response.choices[0].message.content
        print(f"✅ API Test Successful!")
        print(f"Response: {response_text}")
        
    except Exception as e:
        print(f"❌ API Test Failed!")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Message: {str(e)}")
        
        # Common error diagnostics
        error_str = str(e).lower()
        if "authentication" in error_str or "api key" in error_str:
            print("\n🔧 Possible Solutions:")
            print("1. Check if your API key is correct")
            print("2. Ensure your OpenAI account has billing enabled")
            print("3. Verify the API key has the right permissions")
        elif "quota" in error_str or "billing" in error_str:
            print("\n🔧 Possible Solutions:")
            print("1. Check your OpenAI billing and add payment method")
            print("2. Check if you've exceeded your usage limits")
        elif "network" in error_str or "connection" in error_str:
            print("\n🔧 Possible Solutions:")
            print("1. Check your internet connection")
            print("2. Try again in a few minutes")
        
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please make sure all packages are installed correctly")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
