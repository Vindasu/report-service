"""
Quick test for Report Microservice
Run this AFTER starting report-microservice.py
"""

import requests
import json

URL = "http://localhost:5003"

print("\n" + "="*50)
print("Testing Report Microservice")
print("="*50 + "\n")
succeeded = True


# Test 1: Average
print("1. Testing Average Endpoint...")
data = [10, 20, 30]
response = requests.post(f"{URL}/average", json=data)
result = response.json()
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {result}")
print( "   Expected: {'average': 20.0}\n")
if response.status_code != 200:
    print(f"   Test Failed: Response Status Error")
    succeeded = False
if str(result) != "{'average': 20.0}":
    print(f"    Test Failed: Unexpected Result")
    succeeded = False
if succeeded:
    print(f"    Test Passed")


# Test 2: Sum
print("2. Testing Sum Endpoint...")
data = [25.50, 30.00, 45.75]
response = requests.post(f"{URL}/sum", json=data)
result = response.json()
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {result}")
print( "   Expected: {'sum': 101.25}\n")
if response.status_code != 200:
    print(f"   Test Failed: Response Status Error")
    succeeded = False
if str(result) != "{'sum': 101.25}":
    print(f"    Test Failed: Unexpected Result")
    succeeded = False
if succeeded:
    print(f"    Test Passed")


# Test 3: Minimum
print("3. Testing Minimum Endpoint...")
data = [100, 50, 75, 125, 30]
response = requests.post(f"{URL}/minimum", json=data)
result = response.json()
print(f"   Input: {data}")
print(f"   Status: {response.status_code}")
print(f"   Result: {result}")
print( "   Expected: {'minimum': 30}\n")
if response.status_code != 200:
    print(f"   Test Failed: Response Status Error")
    succeeded = False
if str(result) != "{'minimum': 30}":
    print(f"    Test Failed: Unexpected Result")
    succeeded = False
if succeeded:
    print(f"    Test Passed")

print("="*50)
print("✅ All tests complete!")
print("="*50 + "\n")
