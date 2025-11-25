#!/usr/bin/env python3
"""
Simple OpenAI API test with timeout
"""
from openai import OpenAI
from config import apikey
import sys

print("Testing OpenAI API with timeout...")

client = OpenAI(api_key=apikey)

try:
    # Simple test with short timeout
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'Hello'"}],
        max_tokens=10,
        timeout=10  # 10 second timeout
    )
    
    print("✅ SUCCESS: OpenAI API is working!")
    print(f"Response: {response.choices[0].message.content}")
    
except Exception as e:
    print(f"❌ ERROR: {type(e).__name__}")
    print(f"Details: {str(e)}")
    
    # Check common issues
    error_str = str(e).lower()
    print("\n🔧 Troubleshooting:")
    
    if "authentication" in error_str or "401" in error_str:
        print("- Issue: Invalid API key")
        print("- Solution: Check your OpenAI API key in config.py")
        print("- Make sure billing is set up in your OpenAI account")
        
    elif "quota" in error_str or "429" in error_str or "billing" in error_str:
        print("- Issue: Quota exceeded or billing problem")
        print("- Solution: Add payment method to your OpenAI account")
        print("- Check usage limits at https://platform.openai.com/usage")
        
    elif "timeout" in error_str or "network" in error_str:
        print("- Issue: Network/timeout problem")
        print("- Solution: Check internet connection")
        print("- Try again in a few minutes")
        
    elif "model" in error_str:
        print("- Issue: Model access problem")
        print("- Solution: Make sure you have access to gpt-3.5-turbo")
        
    else:
        print("- Unknown error - check your OpenAI account status")
        print("- Visit https://platform.openai.com/ to check account status")
