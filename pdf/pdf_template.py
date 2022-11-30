from fpdf import FPDF
from math import ceil
from django.conf import settings

class PDF(FPDF):
    # def __init__(self, **kwargs):
    def __init__(self, form_title, form_subtitle, form_no, form_iso_no, **kwargs):
        super(PDF, self).__init__(**kwargs)

        font_path = f"{settings.MEDIA_ROOT}/fonts"

        self.add_font(
            "prompt", "", f"{font_path}/Prompt-Regular.ttf", uni=True)
        self.add_font("th", "", f"{font_path}/THSarabunNew.ttf", uni=True)
        self.add_font("th", "B", f"{font_path}/THSarabunNew-Bold.ttf", uni=True)

        self.form_title = form_title
        self.form_subtitle = form_subtitle
        self.form_no = form_no
        self.form_iso_no = form_iso_no

    def header(self):
        # Logo
        self.set_font('th', '', 10)
        logo_path = f"{settings.MEDIA_ROOT}/logo"

        self.image(f'{logo_path}/xlogo.jpg', 11, 20.8, 18)

        # Line break
        self.cell(0, 10, f'Job No. __{self.form_no}__(สำหรับเจ้าหน้าที่)', 0, 1, 'R')
        self.set_font('th', 'B', 16)

        self.cell(w=20, h=20, txt="", border=1)
        self.cell(w=0, h=10, txt=self.form_title,
                  border='T,R,B', ln=2, align='C')
        self.set_font('th', '', 16)
        self.cell(w=0, h=10, txt=self.form_subtitle,
                  border='B, R', align='C', ln=1)

    # Page footer

    def footer(self):
        # Position at 1.5 cm from bottom
        # self.cell(0, 0, "", 'T', 1)
        self.set_y(-15)
        # Arial italic 8
        self.set_font('th', '', 12)
        # Page number
        # self.cell(0, 10, self.form_iso_no + 'IDT-FM-IF-010 (05/05/2022) หน้า ' +
        self.cell(0, 10, self.form_iso_no + ' หน้า ' +
                  str(self.page_no()) + '/{nb}', 0, 0, 'R')

    def get_xy(self):
        return f"x:{ceil(self.get_x())}, y:{ceil(self.get_y())}"
