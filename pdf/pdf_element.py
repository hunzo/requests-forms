from .pdf_template import PDF

font_size = 16


def Cell(pdf: PDF, h, txt, border, ln, align, i: int):
    w = pdf.get_string_width(txt) + i
    pdf.cell(w, h, txt, border, ln, align)


def Block(pdf: PDF, w, h, border, ln, aligned):
    pdf.cell(w, h, "", border, ln, aligned)


def Paragraph(pdf: PDF, key: str, value: str, indent: int, h: int):
    pdf.cell(w=indent, h=h, border='L', txt="")
    pdf.cell(w=0, h=h, txt=f"{key}: {value}", border='R', ln=1)


def Paragraph2Colum(pdf: PDF, key: list, value: list, w: int, h: int):

    # pdf.cell(w=w, h=h, border='L', txt="")
    pdf.cell(w=w, h=h, txt=f"{key[0]}: {value[0]}", ln=0, border='L')

    pdf.cell(w=w, h=h, txt="")
    pdf.cell(w=0, h=h, txt=f"{key[1]}: {value[1]}", border='R', ln=1)


def TextHeader1(pdf: PDF, message: str):
    fontSize = font_size
    hY = 10
    pdf.set_font("th", 'B', fontSize)
    pdf.cell(0, hY, message, 'L, R, T', 1, 'L')
    pdf.set_font("th", '', fontSize)


def TextHeader2(pdf: PDF, message: str, info: str):
    fontSize = font_size
    x = pdf.get_string_width(message) + 3
    hY = 10
    pdf.set_font("th", 'B', fontSize)
    pdf.cell(x, hY, message, 'L', 0, 'L')
    pdf.set_font("th", '', fontSize)
    pdf.cell(0, hY, info, 'R', 1, 'L')


def TextSigned(obj: PDF, name: str):
    hY = 8
    fontSize = font_size
    border = 'L, R'
    obj.set_font("th", '', fontSize)
    obj.cell(0, hY, f"ลงชื่อ ________________________    ", border, 1, 'R')
    obj.cell(0, hY, f"( {name} )    ", border, 1, 'R')
    # obj.cell(0, hY, "ตำแหน่ง ____________________________    ", border, 1, 'R')
    obj.cell(
        0, hY, "ลงนามผู้บริหารหน่วยงาน ____________________________    ", border, 1, 'R')
    # obj.cell(0, hY, "( คณบดี / ผู้อำนวยการ หรือเทียบเท่า )    ", border, 1, 'R')
    obj.cell(0, hY, "( ___________________________ )    ", border, 1, 'R')
    obj.cell(0, hY, "วันที่ ________/________/________    ", border, 1, 'R')


def TextSignedColo(obj: PDF, name: str):
    hY = 8
    fontSize = font_size
    border = 'L, R'
    obj.set_font("th", '', fontSize)
    obj.cell(
        0, hY, f"ลงนามผู้ดูแลเครื่อง ________________________    ", border, 1, 'R')
    obj.cell(0, hY, f"( {name} )    ", border, 1, 'R')
    obj.cell(
        0, hY, "ลงนามผู้บริหารหน่วยงาน ____________________________    ", border, 1, 'R')
    obj.cell(0, hY, "( ___________________________)    ", border, 1, 'R')
    obj.cell(0, hY, "วันที่ ________/________/________    ", border, 1, 'R')


def TextStaff(obj: PDF):
    fontSize = font_size
    h = 8
    boxw = 85
    obj.set_font("th", 'B', fontSize)
    obj.cell(boxw, h, txt="6. ความเห็นเจ้าหน้าที่", border='L, T, R')
    obj.cell(0, h, txt="7. ความเห็นของ ผู้อำนวยการสำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
             border='R, T', ln=1, align='C')

    obj.set_font("th", '', fontSize)
    obj.cell(boxw, h, txt="_____________________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="[ ] อนุมัติ   [ ] ไม่อนุมัติ",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="นัดส่งมอบวันที่ ________/________/________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="ลงนาม __________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="ลงนาม _____________________________________",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="(_______________________)    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="(_______________________)    ",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="วันที่ ________/________/________    ",
             border='L', align='R')
    obj.cell(0, h, txt="วันที่ ________/________/________",
             border='L, R', ln=1, align='C')

    obj.cell(boxw, h, txt="", border='L,R, B')
    obj.cell(0, h, txt="", border='R, B')


def TextStaffCoLo(obj: PDF):
    fontSize = font_size
    h = 8
    boxw = 80
    obj.set_font("th", 'B', fontSize)
    obj.cell(boxw, h, txt="6. ความเห็นเจ้าหน้าที่", border='L, T, R')
    obj.cell(0, h, txt="7. ความเห็นของ ผู้อำนวยการสำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
             border='R, T', ln=1, align='C')

    obj.set_font("th", '', fontSize)
    obj.cell(boxw, h, txt="    _________________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="[ ] อนุมัติ   [ ] ไม่อนุมัติ",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="    _________________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="ลงนาม __________________________    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="ลงนาม _____________________________________",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="(_______________________)    ",
             border='L,R', align='R')
    obj.cell(0, h, txt="(_______________________)    ",
             border='R', ln=1, align='C')

    obj.cell(boxw, h, txt="วันที่ ________/________/________    ",
             border='L', align='R')
    obj.cell(0, h, txt="วันที่ ________/________/________",
             border='L, R', ln=1, align='C')

    obj.cell(boxw, h, txt="", border='L,R, B')
    obj.cell(0, h, txt="", border='R, B')
