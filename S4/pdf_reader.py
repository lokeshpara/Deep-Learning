import PyPDF2
import os

def read_pdf(pdf_path):
    """
    Read and extract text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Check if file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Total pages in PDF: {num_pages}")
            
            # Extract text from each page
            text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
                
            return text
            
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
        return None

def main():
    # Example usage
    pdf_path = "S4.pdf"
    text = read_pdf(pdf_path)
    
    if text:
        # Print first 500 characters as preview
        print("\nPreview of extracted text:")
        print(text[:500])
        
        # Save extracted text to a file
        output_file = "pdf_content.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\nFull text saved to: {output_file}")

if __name__ == "__main__":
    main() 