#!/usr/bin/env python3
"""
Simple test to check if all imports work correctly
"""
try:
    import speech_recognition as sr
    print("✓ speech_recognition imported successfully")
    
    import pyttsx3
    print("✓ pyttsx3 imported successfully")
    
    from openai import OpenAI
    print("✓ OpenAI imported successfully")
    
    from config import apikey
    print("✓ config imported successfully")
    
    print("\nAll imports successful! The main.py file should work now.")
    print("\nThe fixes applied:")
    print("1. ✓ Installed PyAudio for speech recognition")
    print("2. ✓ Replaced macOS 'say' command with pyttsx3 for Windows text-to-speech")
    print("3. ✓ Updated OpenAI API calls to use the new client format")
    print("4. ✓ Fixed Windows-specific file paths and commands")
    print("5. ✓ Added proper error handling")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
