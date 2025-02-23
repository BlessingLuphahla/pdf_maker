from flask import Flask, request, render_template, make_response
from fpdf import FPDF

app = Flask(__name__)

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
        
        # Create response
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        response = make_response(pdf_bytes)
        response.headers.set('Content-Type', 'application/pdf')
        response.headers.set('Content-Disposition', 'attachment', filename='output.pdf')
        return response
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)