"""
Certificate generation utilities using PIL (Pillow)
"""

import os
import uuid
import qrcode
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.core.files.base import ContentFile
from django.utils import timezone
from io import BytesIO
import logging

logger = logging.getLogger(__name__)


def get_default_font(size=24):
    """Get default font for certificate text"""
    try:
        # Try to use a system font
        font_paths = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
            '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
            '/System/Library/Fonts/Arial.ttf',  # macOS
            'C:/Windows/Fonts/arial.ttf',  # Windows
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                return ImageFont.truetype(font_path, size)
        
        # Fallback to default font
        return ImageFont.load_default()
    except Exception as e:
        logger.warning(f"Could not load font: {e}")
        return ImageFont.load_default()


def generate_qr_code(data, size=(100, 100)):
    """Generate QR code image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize(size, Image.Resampling.LANCZOS)
    return qr_img


def get_text_size(text, font):
    """Get text size using PIL"""
    # Create a temporary image to measure text
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

from PIL import Image, ImageDraw
import os
from django.core.files.base import ContentFile
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os
from django.core.files.base import ContentFile
from django.conf import settings

def get_default_font(size):
    """
    Returns a default PIL font with fallback to system or PIL default font.
    You can configure FONT_PATH in settings if needed.
    """
    try:
        font_path = getattr(settings, "CERTIFICATE_FONT_PATH", None)
        if font_path and os.path.exists(font_path):
            return ImageFont.truetype(font_path, size)
        else:
            return ImageFont.load_default()
    except:
        return ImageFont.load_default()
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Mock settings and utility functions for demonstration
class MockSettings:
    CERTIFICATE_TEMPLATE_PATH = '/home/ubuntu/upload/original_certificate.jpg'
    CERTIFICATE_OUTPUT_PATH = './output_certificates'

settings = MockSettings()

def get_default_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except IOError:
        return ImageFont.load_default()

def draw_text_with_wrap(draw, text, x, y, font, max_width, fill):
    words = text.split(" ")
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if font.getlength(test_line) <= max_width:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    lines.append(" ".join(current_line))

    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += font.getbbox(line)[3] - font.getbbox(line)[1] + 5 # Line spacing

def generate_qr_code(data, size):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=7,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize(size, Image.LANCZOS)  # Ensure sharp resizing

class MockCertificateObj:
    def __init__(self):
        self.full_name = "John Doe"
        self.college_name = "University of Example"
        self.affiliated_name = "Example Affiliation"
        self.roll_number = "123456789"
        self.course = "Internship Program in Data Science"
        self.start_date = "01/01/2024"
        self.end_date = "31/03/2024"
        self.certificate_id = "A6A7A3C579Bb66"
        self.created_at = "2024-04-15"

    def get_verification_url(self):
        return "https://example.com/verify/" + self.certificate_id

    
    
    def get_certificate_filename(self):
        return f"{self.roll_number.replace(' ', '_')}.png"


    def get_qr_filename(self):
        return f"qr_{self.roll_number.replace(' ', '_')}.png"

from PIL import Image, ImageDraw, ImageFont
import os
from django.core.files.base import ContentFile
from django.conf import settings




from PIL import ImageFont
import os
from django.conf import settings

def get_default_font(size):
    """
    Returns a PIL ImageFont object using the custom font from settings or falls back to default.
    """
    try:
        font_path = getattr(settings, "CERTIFICATE_FONT_PATH", None)
        if font_path and os.path.exists(font_path):
            print(f"Font loaded from: {font_path}")  # Or alert if it falls back
            return ImageFont.truetype(str(font_path), size)  # ✅ Ensure it's a string
        
        else:
            print("Font path not found. Using default PIL font.")
            return ImageFont.load_default()
    except Exception as e:
        print(f"Font loading error: {e}")
        return ImageFont.load_default()
from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
import os
from django.conf import settings

# --- Helper functions ---
from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
import os
from django.conf import settings

# --- Helper functions ---

def draw_centered(draw, text, font, y, x_start, x_end, fill="black"):
    """Draw text centered between x_start and x_end."""
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    x = x_start + (x_end - x_start - text_width) / 2
    draw.text((x, y), text, font=font, fill=fill)

def draw_left(draw, text, font, x, y, fill="black"):
    """Draw left-aligned text."""
    draw.text((x, y), text, font=font, fill=fill)

from django.core.files.base import ContentFile
from io import BytesIO
import os


from django.core.files.base import ContentFile
from io import BytesIO
import os

def generate_certificate_image(certificate_obj, template_name='Pragna'):
    try:
        # Load certificate template
        template_filename = f"original_certificate_{template_name.lower().replace(' ', '')}.jpg"
        template_path = os.path.join(settings.MEDIA_ROOT, 'templates', template_filename)
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        template = Image.open(template_path).convert("RGB")
        draw = ImageDraw.Draw(template)

        # Fonts
        base_size = settings.CERTIFICATE_FONT_SIZE
        name_font = get_default_font(int(base_size * 1.4))
        small_font = get_default_font(int(base_size * 1.0))
        small_font2 = get_default_font(int(base_size * 0.8))
        draw_centered(draw, certificate_obj.full_name, small_font, y=375, x_start=460, x_end=1080)
        draw_centered(draw, certificate_obj.college_name, small_font, y=415, x_start=245, x_end=1065)
        draw_centered(draw, certificate_obj.affiliated_name, small_font, y=462, x_start=290, x_end=670)
        draw_centered(draw, certificate_obj.roll_number, small_font, y=458, x_start=915, x_end=1080)
        draw_centered(draw, certificate_obj.course, small_font, y=512, x_start=690, x_end=1130)
        draw_centered(draw, certificate_obj.start_date.strftime("%d-%m-%Y"), small_font, y=605, x_start=600, x_end=830)
        draw_centered(draw, certificate_obj.end_date.strftime("%d-%m-%Y"), small_font, y=605, x_start=910, x_end=1130)
        draw_left(draw, str(certificate_obj.certificate_id), small_font2, x=296, y=665)
        draw_left(draw, certificate_obj.created_at.strftime("%d-%m-%Y"), small_font2, x=229, y=700)
        draw_centered(draw, "Verify at https://verify.cscindia.org.in/", small_font2, 805, 292, 1080)

        # QR Code
        verification_url = certificate_obj.get_verification_url()
        qr_img = generate_qr_code(verification_url, size=(110, 80))
        template.paste(qr_img, (963, 278))

        # Convert template image to memory
        image_io = BytesIO()
        template.save(image_io, format="PNG", quality=95)
        image_io.seek(0)

        # Use only the student's name for the filename, spaces replaced by underscores
        base_filename = certificate_obj.roll_number.replace(' ', '_')
        certificate_filename = f"{base_filename}.png"
        certificate_obj.certificate_image.save(certificate_filename, ContentFile(image_io.read()), save=False)

        # Save QR to model (optional)
        qr_io = BytesIO()
        qr_img.save(qr_io, format="PNG")
        qr_io.seek(0)
        qr_filename = f"qr_{base_filename}.png"
        certificate_obj.qr_code_image.save(qr_filename, ContentFile(qr_io.read()), save=False)

        certificate_obj.save()

        print(f"✅ Saved via Django model: {certificate_filename}")
        return certificate_obj.certificate_image.url

    except Exception as e:
        print(f"❌ Error: {e}")
        logger.error(f"Error generating certificate: {str(e)}")
        raise


# Example usage (for testing)
if __name__ == "__main__":
    mock_cert = MockCertificateObj()
    generate_certificate_image(mock_cert)

from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.conf import settings
from django.core.files.base import ContentFile
import os

def generate_certificate_pdf(certificate_obj):
    context = {
        'full_name': certificate_obj.full_name.upper(),
        'college_name': certificate_obj.college_name,
        'roll_number': certificate_obj.roll_number,
        'course': certificate_obj.course,
        'certificate_id': str(certificate_obj.certificate_id)[:12],
        'issue_date': certificate_obj.created_at.strftime("%d-%m-%Y"),
        'qr_code_url': certificate_obj.qr_code_image.url  # Must be full/static URL
    }

    html = render_to_string("certificate_template.html", context)
    cert_filename = certificate_obj.get_certificate_filename().replace('.png', '.pdf')
    cert_path = os.path.join(settings.CERTIFICATE_OUTPUT_PATH, cert_filename)
    os.makedirs(settings.CERTIFICATE_OUTPUT_PATH, exist_ok=True)

    with open(cert_path, "wb") as out_file:
        pisa_status = pisa.CreatePDF(html, dest=out_file)

    if pisa_status.err:
        raise Exception("Error creating PDF")

    with open(cert_path, 'rb') as f:
        certificate_obj.certificate_pdf.save(cert_filename, ContentFile(f.read()), save=False)

    certificate_obj.save()
    return cert_path
 


from datetime import datetime
def create_certificate_from_form_data(form_data):
    """
    Create certificate from form data and generate all files
    """
    from .models import Certificate
    
    # Create certificate object
    certificate = Certificate.objects.create(
        full_name=form_data['full_name'].upper(),
        roll_number=form_data['roll_number'],
        course=form_data['course'],
        college_name=form_data['college_name'],
        affiliated_name=form_data['affiliated_name'],
        email=form_data['email'],
        start_date=form_data['start_date'],
        end_date=form_data['end_date'],
    )
    
    # Generate certificate image and QR code
    template_name = form_data.get('template', 'Pragna')
    generate_certificate_image(certificate, template_name=template_name)
    
    # Generate PDF (optional)
    try:
        generate_certificate_pdf(certificate)

    except Exception as e:
        logger.warning(f"PDF generation failed: {e}")
    
    return certificate


def send_certificate_email(certificate_obj):
    """
    Send internship certificate via email with professional styled HTML and plain-text fallback.
    """
    try:
        from django.core.mail import EmailMultiAlternatives
        from django.conf import settings
        from django.utils import timezone
        import logging
        import os

        logger = logging.getLogger(__name__)

        if not certificate_obj.certificate_image:
            raise ValueError("Certificate image must be generated first")

        subject = f"🎓 Internship Completion Certificate – {certificate_obj.course}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [certificate_obj.email]

        # Plain text fallback
        text_content = f"""
Dear {certificate_obj.full_name},

Greetings from Council for Skills and Competencies (CSC India)!

We are delighted to inform you that you have successfully completed the internship program titled "{certificate_obj.course}", organized under the guidance of CSC India.

Your official internship certificate is attached with this email. You may also verify the certificate using the unique Certificate ID or through the link provided below.
 Verify your certificate at "https://verify.cscindia.org.in/".
       
Certificate Details:
• Course: {certificate_obj.course}
• College: {certificate_obj.college_name}
• Roll Number: {certificate_obj.roll_number}
• Certificate ID: {certificate_obj.certificate_id}
• Issue Date: {certificate_obj.created_at.strftime("%d %B %Y")}

Verify your certificate here: {certificate_obj.verification_url}

We congratulate you on this achievement and wish you continued success in your academic and professional journey.

Warm regards,  
Certificate Management Team  
Council for Skills and Competencies (CSC India)  
Visakhapatnam, Andhra Pradesh, India

WhatsApp: 9666500222  
Email: rammohan@cscindia.org.in  
Website: www.cscindia.org.in
"""

        # HTML version
        html_content = f"""
<html>
<head>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background-color: #f9fafc;
            color: #333;
            padding: 30px;
        }}
        .container {{
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            max-width: 600px;
            margin: auto;
            padding: 30px;
        }}
        h2 {{
            text-align: center;
            color: #2c3e50;
        }}
        p {{
            font-size: 15px;
            line-height: 1.6;
        }}
        .details-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        .details-table th {{
            background-color: #004c97;
            color: white;
            padding: 10px;
            text-align: left;
        }}
        .details-table td {{
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }}
        .verify-button {{
            display: block;
            width: max-content;
            margin: 20px auto;
            padding: 12px 20px;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }}
        .imp {{
            font-size: 13px;
            text-align: center;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2>🎉 Congratulations, {certificate_obj.full_name}!</h2>

        <p>We are pleased to inform you that you have successfully completed the internship program titled 
        <strong>"{certificate_obj.course}"</strong>, organized under the guidance of the <strong>Council for Skills and Competencies (CSC India)</strong>.</p>

        <p>Your internship completion certificate is attached for your reference. You may also verify the authenticity of this certificate using the Certificate ID mentioned below or by visiting the verification link provided.</p>
        <p><b> Verify your certificate at <a href="https://verify.cscindia.org.in/" target="_blank">www.verify.cscindia.org.in</a></b><p>
        <table class="details-table">
            <tr><th colspan="2">📋 Certificate Summary</th></tr>
            <tr><td><strong>Full Name</strong></td><td>{certificate_obj.full_name}</td></tr>
            <tr><td><strong>Course</strong></td><td>{certificate_obj.course}</td></tr>
            <tr><td><strong>College</strong></td><td>{certificate_obj.college_name}</td></tr>
            <tr><td><strong>Roll Number</strong></td><td>{certificate_obj.roll_number}</td></tr>
            <tr><td><strong>Certificate ID</strong></td><td>{certificate_obj.certificate_id}</td></tr>
            <tr><td><strong>Issue Date</strong></td><td>{certificate_obj.created_at.strftime("%d %B %Y")}</td></tr>
        </table>

        <a class="verify-button" href="{certificate_obj.verification_url}" target="_blank">✅ Verify Certificate</a>

        <div class="imp">
            Best Regards,<br>
            <strong>Certificate Management Team</strong><br>
            Council for Skills and Competencies (CSC India)<br>
            Visakhapatnam, Andhra Pradesh, India<br><br>
            <b>WhatsApp:</b> 9666500222<br>
            <b>Email:</b> <a href="mailto:rammohan@cscindia.org.in">rammohan@cscindia.org.in</a><br>
            <b>Website:</b> <a href="https://www.cscindia.org.in" target="_blank">www.cscindia.org.in</a>
        </div>
    </div>
</body>
</html>
"""

        # Compose and attach email contents
        email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        email.attach_alternative(html_content, "text/html")

        # Attach certificate image with name only
        image_filename = f"{certificate_obj.rollnumber.replace(' ', '_')}.png"
        with open(certificate_obj.certificate_image.path, 'rb') as f:
            email.attach(image_filename, f.read(), 'image/png')

        # Attach PDF if available
        if certificate_obj.certificate_pdf:
            pdf_filename = f"{certificate_obj.roll_number.replace(' ', '_')}.pdf"
            with open(certificate_obj.certificate_pdf.path, 'rb') as f:
                email.attach(pdf_filename, f.read(), 'application/pdf')

        # Send email
        email.send()

        # Update certificate status
        certificate_obj.email_sent = True
        certificate_obj.email_sent_at = timezone.now()
        certificate_obj.save()

        logger.info(f"✅ Certificate email sent successfully to {certificate_obj.email}")

    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"❌ Error sending certificate email: {str(e)}")
        raise


def upload_to_google_drive(certificate_obj):
    """
    Upload certificate to Google Drive with student name as filename.
    """
    try:
        from googleapiclient.discovery import build
        from google.oauth2.service_account import Credentials
        from googleapiclient.http import MediaFileUpload
        from django.conf import settings
        from django.utils import timezone
        import os
        import logging

        logger = logging.getLogger(__name__)

        if not certificate_obj.certificate_image:
            raise ValueError("Certificate image must be generated first")

        credentials_file = settings.GOOGLE_DRIVE_CREDENTIALS_FILE
        if not credentials_file or not os.path.exists(credentials_file):
            raise FileNotFoundError("Google Drive credentials file not found")

        SCOPES = ['https://www.googleapis.com/auth/drive.file']
        credentials = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
        service = build('drive', 'v3', credentials=credentials)

        # File name is just student's name
        file_name = f"{certificate_obj.roll_number.replace(' ', '_')}.png"
        file_metadata = {
            'name': file_name,
            'parents': [settings.GOOGLE_DRIVE_FOLDER_ID] if settings.GOOGLE_DRIVE_FOLDER_ID else []
        }

        media = MediaFileUpload(
            certificate_obj.certificate_image.path,
            mimetype='image/png'
        )

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()

        # Save file ID and update status
        certificate_obj.drive_uploaded = True
        certificate_obj.drive_file_id = file.get('id')
        certificate_obj.drive_uploaded_at = timezone.now()
        certificate_obj.save()

        logger.info(f"Certificate uploaded to Google Drive: {file.get('id')}")
        return file.get('id')

    except Exception as e:
        logger.error(f"Error uploading to Google Drive: {str(e)}")
        raise


# def upload_to_google_drive(certificate_obj):
#     """
#     Upload certificate to Google Drive
#     """
#     from django.conf import settings
#     import os
#     import logging

#     logger = logging.getLogger(__name__)

#     logger.info("📁 Checking Google Drive credentials file:")
#     logger.info(f"Path: {settings.GOOGLE_DRIVE_CREDENTIALS_FILE}")
#     logger.info(f"Exists: {os.path.exists(settings.GOOGLE_DRIVE_CREDENTIALS_FILE)}")

#     try:
#         from googleapiclient.discovery import build
#         from google.oauth2.service_account import Credentials
#         from googleapiclient.http import MediaFileUpload
#         from django.utils import timezone

#         if not certificate_obj.certificate_image:
#             raise ValueError("Certificate image must be generated first")

#         # Check if credentials file exists
#         credentials_file = settings.GOOGLE_DRIVE_CREDENTIALS_FILE
#         if not credentials_file or not os.path.exists(credentials_file):
#             raise FileNotFoundError("Google Drive credentials file not found")

#         # Set up credentials and service
#         SCOPES = ['https://www.googleapis.com/auth/drive.file']
#         credentials = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)
#         service = build('drive', 'v3', credentials=credentials, cache_discovery=False)

#         # Prepare file metadata
#         file_name = f"certificate_{certificate_obj.full_name.replace(' ', '_')}_{certificate_obj.certificate_id}.png"
#         file_metadata = {
#             'name': file_name,
#             'parents': [settings.GOOGLE_DRIVE_FOLDER_ID] if settings.GOOGLE_DRIVE_FOLDER_ID else []
#         }

#         # Upload file
#         media = MediaFileUpload(
#             certificate_obj.certificate_image.path,
#             mimetype='image/png'
#         )

#         file = service.files().create(
#             body=file_metadata,
#             media_body=media,
#             fields='id'
#         ).execute()

#         # Update certificate status
#         certificate_obj.drive_uploaded = True
#         certificate_obj.drive_file_id = file.get('id')
#         certificate_obj.drive_uploaded_at = timezone.now()
#         certificate_obj.save()

#         logger.info(f"✅ Certificate uploaded to Google Drive: {file.get('id')}")
#         return file.get('id')

#     except Exception as e:
#         logger.error(f"❌ Error uploading to Google Drive: {str(e)}")
#         raise

def process_certificate_request(form_data):
    """
    Complete certificate processing workflow:
    1. Create certificate
    2. Generate image and QR code
    3. Send email
    4. Upload to Google Drive
    """
    try:
        # Create and generate certificate
        certificate = create_certificate_from_form_data(form_data)
        
        # Send email (if configured)
        
        try:
            send_certificate_email(certificate)
        except Exception as e:
            logger.warning(f"Email sending failed: {e}")
        
        # # Upload to Google Drive (if configured)
        # try:
        #     upload_to_google_drive(certificate)
        # except Exception as e:
        #     logger.warning(f"Google Drive upload failed: {e}")
        
        return certificate
        
    except Exception as e:
        logger.error(f"Error processing certificate request: {str(e)}")
        raise



