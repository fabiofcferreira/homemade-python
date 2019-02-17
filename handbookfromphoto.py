from docx import Document
import os

# Orientation
from docx.enum.section import WD_ORIENTATION
# Unit system
from docx.shared import Inches


EXTS = [
    'JPG',
    'JPEG'
]

docname = ''
imgsdir = ''

def changeOrientation(doc: Document):
    section = doc.sections[-1]
    # Change orientation
    section.orientation = WD_ORIENTATION.LANDSCAPE
    # Switch width and height
    new_width, new_height = section.page_height, section.page_width
    # Apply the new dimensions
    section.page_width = new_width
    section.page_height = new_height


def changeMargins(doc: Document):
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.right_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.5)


def getImageList(path):
    images = []
    for file in os.listdir(path):
        ext = file[len(file)-3:]
        if ext.upper() in EXTS:
            images.append(file)

    return images


def insertImage(doc: Document, filename):
    doc.add__picture(imgsdir + '/' + filename, width=Inches(6.6))


def main():
    try:
        docname = input('Word document name: ')
        if docname == '':
            raise Exception('Invalid word document filename')

        imgsdir = input('Image files directory: ')
        if imgsdir == '':
            raise Exception('Invalid image files directory')

        document = Document()  # yay, create new stuff
        changeOrientation(document)
        print('Orientation changed to landscape mode')
        changeMargins(document)
        print('Margins are 0.5"')

        imgList = getImageList(imgsdir)
        if len(imgList) <= 0:
            raise Exception('No image files found')
        else:
            print('Found %s images.' % len(imgList))

        for i in range(len(imgList)):
            print('Inserting image #%s' % i)
            document.add_picture(imgsdir + '/' + imgList[i], height=Inches(6.6))
            # insertImage(document, imgList[i])

        document.save(docname + '.docx')
        print('Successfully saved %s.docx' % docname)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()