from pylatex import Document, Section, Subsection, Command
from pylatex.utils import NoEscape

def create_beamer_presentation(filename="beamer_slideshow"):
    # Create a beamer document
    doc = Document(documentclass="beamer")

    # Add title, author, date
    doc.preamble.append(Command('title', 'Sample Beamer Presentation'))
    doc.preamble.append(Command('author', 'Your Name'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\frame{\titlepage}'))

    # Add a frame (slide) with a section and content
    doc.append(NoEscape(r'\begin{frame}'))
    doc.append(NoEscape(r'\frametitle{Introduction}'))
    doc.append('This is the first slide. Welcome to the presentation!')
    doc.append(NoEscape(r'\end{frame}'))

    # Another slide
    doc.append(NoEscape(r'\begin{frame}'))
    doc.append(NoEscape(r'\frametitle{Main Points}'))
    doc.append(NoEscape(r'\begin{itemize}'))
    doc.append(NoEscape(r'\item Point 1'))
    doc.append(NoEscape(r'\item Point 2'))
    doc.append(NoEscape(r'\item Point 3'))
    doc.append(NoEscape(r'\end{itemize}'))
    doc.append(NoEscape(r'\end{frame}'))

    # Closing slide
    doc.append(NoEscape(r'\begin{frame}'))
    doc.append(NoEscape(r'\frametitle{Conclusion}'))
    doc.append('Thank you for your attention!')
    doc.append(NoEscape(r'\end{frame}'))

    # Generate the PDF
    doc.generate_pdf(filename, clean_tex=False)
    print(f"PDF '{filename}.pdf' generated successfully.")

# Run the function
if __name__ == "__main__":
    create_beamer_presentation()
