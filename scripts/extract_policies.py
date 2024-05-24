import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

pdf_path = 'company_policies.pdf'
company_policies_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a file for easy access
with open('data/company_policies.txt', 'w') as f:
    f.write(company_policies_text)
