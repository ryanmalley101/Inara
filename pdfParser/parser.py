import pdfrw

def extract_form_data(pdf_path):
    form_data = {}
    pdf = pdfrw.PdfReader(pdf_path)
    for page in pdf.pages:
        annotations = page['/Annots']
        if not annotations:
            continue
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget' and '/T' in annotation:
                field_name = annotation['/T']
                if '/V' in annotation:
                    field_value = annotation['/V']
                    form_data[field_name] = field_value
                elif '/DV' in annotation:
                    field_value = annotation['/DV']
                    form_data[field_name] = field_value
    return form_data

if __name__ == "__main__":
    pdf_path = "doomsdaydesign_1429365.pdf"
    extracted_data = extract_form_data(pdf_path)
    print(extracted_data)