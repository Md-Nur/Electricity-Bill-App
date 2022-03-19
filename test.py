#!/usr/bin/env python
# -*- coding: utf8 -*-

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add a DejaVu Unicode font (uses UTF-8)
# Supports more than 200 languages. For a coverage status see:
# http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
pdf.add_font(
    "SutonnyMJ", "", "SutonnyMJ Regular.ttf", uni=True
)
pdf.set_font("SutonnyMJ", "", 14)

text = """
খেলা হবে
আজকে
তাই নাকি 
পাককা
কহলাম
কহীলাম কিছু করবেন না
কীমনী করবেন না
Avgvi Kwig
"""

for txt in text.split("\n"):
    pdf.write(8, txt)
    pdf.ln(8)

# Add a Indic Unicode font (uses UTF-8)
# Supports: Bengali, Devanagari, Gujarati,
#           Gurmukhi (including the variants for Punjabi)
#           Kannada, Malayalam, Oriya, Tamil, Telugu, Tibetan

# Add a AR PL New Sung Unicode font (uses UTF-8)
# The Open Source Chinese Font (also supports other east Asian languages)


# Add a Alee Unicode font (uses UTF-8)
# General purpose Hangul truetype fonts that contain Korean syllable
# and Latin9 (iso8859-15) characters.


# Add a Fonts-TLWG (formerly ThaiFonts-Scalable) (uses UTF-8)


# Select a standard font (uses windows-1252)

pdf.output("unicode.pdf", "F")
