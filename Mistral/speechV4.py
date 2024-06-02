"""import time

import requests

# Define the API endpoint
url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"

# Set your Deepgram API key
api_key = "255be827c5a585a1265a43ba25b2869129b92142"

# Define the headers
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

# Define the payload
a = time.time()
payload = {
    "text": "It's important to note that when calculating population parameters from sample statistics, like mean and variance, they are only estimates of the true population parameters. In this case, the sample mean and variance are used as estimates of the population mean and variance, respectively."
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    with open("your_output_file.mp3", "wb") as f:
        f.write(response.content)
    print("File saved successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")
b = time.time()
print("Latency",b-a)"""

import asyncio
"""from TTS.api import  TTS
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS("tts_models/en/jenny/jenny",progress_bar=False).to(device)
tts.tts_to_file(text=" It is a measure of a computer's performance or the capability of a computing device to perform floating-point arithmetic operations. Floating-point operations are mathematical calculations involving numbers with decimal points, which are common in many scientific, engineering, and graphical applications.",file_path="coquie.wav")

"""
