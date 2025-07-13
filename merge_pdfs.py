from PyPDF2 import PdfMerger

def merge_pdfs(input_pdfs, output_pdf):
    # Initialize the PdfMerger object
    merger = PdfMerger()
    
    # Loop through the list of input PDFs and add them to the merger
    for pdf in input_pdfs:
        merger.append(pdf)
    
    # Write the merged PDF to the output file
    merger.write(output_pdf)
    merger.close()
    print(f"Merged PDFs into {output_pdf}")

# Example usage
if __name__ == "__main__":
    # List of PDF files to merge
    input_files = ["cover_letter/cover_letter.pdf", "resume.pdf"]
    # Output file name
    output_file = "resume_&_coverletter.pdf"
    
    # Call the merge function
    merge_pdfs(input_files, output_file)