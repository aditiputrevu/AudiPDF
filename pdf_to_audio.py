import os
import PyPDF2
import boto3

def convert_pdf_to_audio(pdf_path, voice_id='Joanna', engine='neural'):
    try:
        # Convert relative path to absolute path
        pdf_path = os.path.abspath(pdf_path)

        # Check if file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file {pdf_path} does not exist")

        # Open and read the PDF
        with open(pdf_path, 'rb') as pdf_file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Extract text from all pages
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Create output filename in the same directory as input
            output_path = os.path.splitext(pdf_path)[0] + '.mp3'

            # Initialize AWS Polly client
            polly = boto3.client(
                'polly',
                region_name='us-east-1',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEYID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESSKEY')
            )

            # Convert text to speech using AWS Polly
            print("Converting to audio...")
            response = polly.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId=voice_id,
                Engine=engine
            )

            # Save the audio file
            with open(output_path, 'wb') as audio_file:
                audio_file.write(response['AudioStream'].read())
            print(f"Audio file saved as: {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("\nPossible solutions:")
        print("1. Provide the full path to your PDF file")
        print("2. Make sure the PDF file is in the current directory:", os.getcwd())
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # You can use any of these formats:

    # 1. Full path (recommended)
    # convert_pdf_to_audio('/Users/aditiputrevu/AudiPDF/twinklestar.pdf')

    # 2. Relative path from current directory
    # convert_pdf_to_audio('./twinklestar.pdf')

    # 3. Just filename if the PDF is in the same directory as the script
    convert_pdf_to_audio('twinklestar.pdf')