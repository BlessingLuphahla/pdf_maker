from flask import Flask, request, render_template, make_response
from fpdf import FPDF
from dotenv import load_dotenv
import os
from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

# Load environment variables from .env file
load_dotenv()

# Access environment variables
PORT = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set

app = Flask(__name__)

random = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text_content = request.form.get('text', '')

        # Generate PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        try:
            pdf.add_font('Arial', '', 'arial.ttf', uni=True)
            pdf.set_font('Arial', '', 12)
        except:
            pdf.set_font('Arial', '', 12)

        pdf.multi_cell(0, 8, text_content)

        # Corrected output handling
        pdf_bytes = pdf.output(dest='S')
        response = make_response(bytes(pdf_bytes))
        response.headers.set('Content-Type', 'application/pdf')
        response.headers.set('Content-Disposition', 'attachment', filename=f'output{get_current_date()}.pdf')

        return response

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
