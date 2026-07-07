import os
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# -----------------------------------
# Folders
# -----------------------------------
NOTES_FOLDER = "notes/generated_notes"
SUMMARY_FOLDER = "notes/generated_notes/summary"
PDF_FOLDER = "notes/generated_notes/pdf"

os.makedirs(PDF_FOLDER, exist_ok=True)


# -----------------------------------
# Get Latest File
# -----------------------------------
def get_latest_file(folder):

    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".txt")
    ]

    if not files:
        return None

    return max(files, key=os.path.getmtime)


# -----------------------------------
# Create PDF
# -----------------------------------
def create_pdf():

    notes_file = get_latest_file(NOTES_FOLDER)
    summary_file = get_latest_file(SUMMARY_FOLDER)

    if notes_file is None:
        print("No lecture notes found.")
        return

    with open(notes_file, "r", encoding="utf-8") as file:
        notes = file.read()

    summary = ""

    if summary_file:
        with open(summary_file, "r", encoding="utf-8") as file:
            summary = file.read()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    pdf_file = os.path.join(
        PDF_FOLDER,
        f"Lecture_Notes_{timestamp}.pdf"
    )

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b><font size=18>AI Virtual Classroom</font></b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<b>Automatic Lecture Notes</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(notes.replace("\n", "<br/>"), styles["BodyText"])
    )

    if summary.strip():

        story.append(
            Paragraph(
                "<br/><b>Summary</b>",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                summary.replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

    doc.build(story)

    print("\n==============================")
    print("PDF Created Successfully")
    print("==============================")
    print("Saved to:", pdf_file)


# -----------------------------------
# Main
# -----------------------------------
if __name__ == "__main__":
    create_pdf()
