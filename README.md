# 📚✨ AudiPDF ✨📚

Welcome to the **PDF-to-Audiobook Converter**! 🎉  
This project turns your boring PDFs into exciting audiobooks using **AWS Polly**, Amazon's state-of-the-art text-to-speech service. Whether commuting, working out, or just too lazy to read, this tool covers you! 🚀

---

## 🎯 **What Does This Project Do?**

- **Converts PDFs to Audiobooks**: Upload a PDF, and this tool will extract the text, convert it to speech, and save it as an MP3 file. 🎧
- **Uses AWS Polly**: Leverages Amazon's powerful text-to-speech service for high-quality, natural-sounding audio. 🗣️
- **Customizable Voices**: Choose from various voices (e.g., Joanna, Matthew) and switch between standard and neural engines for better audio quality. 🎙️
- **Easy to Use**: Just run the script, and you're ready! No complicated setup is required. 🛠️

---

## 🚀 **How to Get Started**

### 1. **Prerequisites**
Before diving in, make sure you have the following:

- **Python 3.x**: If you don't have Python installed, grab it from [here](https://www.python.org/downloads/).
- **AWS Account**: You'll need an AWS account to use AWS Polly. Sign up [here](https://aws.amazon.com/).
- **AWS Credentials**: Set up your AWS Access Key ID and Secret Access Key. Follow [this guide](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) to get started.

---

### 2. **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/aditiputrevu/AudiPDF.git
   cd AudiPDF
   ```

2. **Set Up a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

### 3. **Configure AWS Credentials**

1. **Set Up Environment Variables**:
   Add your AWS credentials to your environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key-id"
   export AWS_SECRET_ACCESS_KEY="your-secret-access-key"
   ```

   Or, use the AWS CLI to configure your credentials:
   ```bash
   aws configure
   ```

2. **Test AWS Polly**:
   Make sure AWS Polly is working by running:
   ```bash
   aws polly describe-voices --region us-east-1
   ```

---

### 4. **Run the Script**

1. **Place Your PDF**:
   Add your PDF file (e.g., `twinklestar.pdf`) to the project directory.

2. **Run the Converter**:
   ```bash
   python pdf_to_audio.py
   ```

3. **Enjoy Your Audiobook**:
   The script will generate an MP3 file in the same directory as your PDF. Grab your headphones and enjoy! 🎧

---

## 🛠️ **Customization**

### **Change the Voice**
You can customize the voice used for the audiobook. Here's how:

1. **List Available Voices**:
   Run the following command to see all available voices:
   ```bash
   aws polly describe-voices --region us-east-1
   ```

2. **Update the Script**:
   Modify the `voice_id` parameter in the script:
   ```python
   voice_id = 'Joanna'  # Change to your preferred voice
   ```

### **Switch to Neural Engine**
For even better audio quality, switch to the neural engine:
```python
engine = 'neural'  # Change to 'standard' if you prefer
```

---

## 🐛 **Troubleshooting**

### **1. AWS Credentials Error**
If you see an error like `UnrecognizedClientException`, double-check your AWS credentials and region. Ensure they're correctly set in your environment variables or AWS CLI configuration.

### **2. File Not Found**
If the script can't find your PDF, make sure:
- The file is in the correct directory.
- You're providing the correct file path.

### **3. Character Limit**
AWS Polly has a limit of **3000 characters per request**. If your PDF is large, split the text into smaller chunks and process them sequentially.

---

## 🚨 **Important Notes**

- **AWS Costs**: AWS Polly charges based on the number of characters processed. Check the [AWS Polly Pricing](https://aws.amazon.com/polly/pricing/) page for details.
- **Secrets Management**: Never hardcode your AWS credentials in the script. Use environment variables or AWS CLI configuration.

---

## 📜 **License**

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as you see fit. Check out the [LICENSE](LICENSE) file for more details.

---

## 🙏 **Credits**

- **AWS Polly**: For providing the amazing text-to-speech service.
- **PyPDF2**: This is for making PDF text extraction a breeze.
- **You**: For using this tool and making it better! 🚀

---

Happy Listening! 🎧✨
