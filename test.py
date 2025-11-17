"""
Quick test for Statistics Microservice
Run this AFTER starting report-microservice.py
"""

import requests
import json

URL = "http://localhost:5003"

print("\n" + "="*50)
print("Testing Statistics Microservice")
print("="*50 + "\n")


# Test 1: Average
print("1. Testing Average Endpoint...")
data = [10, 20, 30]
response = requests.post(f"{URL}/average", json=data)
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {response.json()}")
print( "   Expected: {'average': 20.0}\n")

# Test 2: Sum
print("2. Testing Sum Endpoint...")
data = [25.50, 30.00, 45.75]
response = requests.post(f"{URL}/sum", json=data)
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {response.json()}")
print(f"   Expected: 101.25\n")

# Test 3: Minimum
print("3. Testing Minimum Endpoint...")
data = [100, 50, 75, 125, 30]
response = requests.post(f"{URL}/minimum", json=data)
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {response.json()}")
print(f"   Expected: 30\n")

print("="*50)
print("✅ All tests complete!")
print("="*50 + "\n")