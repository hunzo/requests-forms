from .pdf_template import PDF
from .pdf_element import TextHeader1, TextHeader2, TextSigned, TextStaff, Paragraph, Paragraph2Colum, Cell, Block
from math import ceil
import io
import uuid

# def Cell(pdf: PDF, text, border, ln, aligned ):
#     w = pdf.get_string_width(text) + 10
#     pdf.cell(w, 8, text, border, ln, aligned)


def account_request_form(object):
    pdf = PDF(
        form_title=object["form_title"],
        form_subtitle="สำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
        form_iso_no=object["form_iso_no"],
        form_no=str(uuid.uuid4()),

        orientation="P",
        unit="mm",
    )
    print("VPN")

    pdf.alias_nb_pages()
    pdf.add_page()

    fontSize = 16
    # effective_page_width = pdf.w - 2*pdf.l_margin
    p = 8
    ident = 15
    hstyle = 'b'

    pdf.set_font('th', "b", fontSize)
    Cell(pdf, p, "1. ผู้ใช้งาน", "L", 0, "L", 3)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ข้าพเจ้า (ภาษาไทย)", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["fname_th"], 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "นามสกุล", 0, 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["lname_th"], 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ข้าพเจ้า (ภาษาอังกฤษ)", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["fname"], 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "นามสกุล", 0, 0, 'L', 5)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["lname"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "เลขที่บัตรประจําตัวประชาชน / หนังสือเดินทาง", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["cid"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ส่วนงาน", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["dept"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "โทรศัพท์ ", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["tel"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "อีเมลสํารอง( อีเมลสําหรับติดต่อ ใส่อีเมลอื่นที่ไม่ใช่อีเมลของสถาบัน)", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["email"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ตั้งแต่วันที่", "L", 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["start_date"]), 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ถึงวันที่", 0, 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["end_date"]), 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.set_font('th', 'bu', fontSize)
    Cell(pdf, p, "หมายเหตุ", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, "ต้องแจ้งล่วงหน้าก่อนใช้งานอย่างน้อย 3 วันทําการ", 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.cell(0, p/2, "", 'L,R', 1)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "2. ประเภทผู้ใช้งาน", 'L, T', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["person_type"], 'T', 0, 'C', 1)
    Block(pdf, 0, p, "R, T", 1, 'C')

    pdf.set_font('th', 'b', fontSize)
    pdf.cell(0, p, "3. ข้าพเจ้ารับทราบนโยบาย และยินดีจะรับผิดชอบต่อความเสียหายที่เกิดขึ้นตาม พระราชบัญญัติว่าด้วยการกระทําความผิด", 'L,R, T', 1)
    pdf.cell(0, p, "   เกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 และที่แก้ไขเพิ่มเติม อย่างเคร่งครัดทุกประการ", 'L,R', 1)

    b = 80
    p = 8
    pdf.set_font('th', '', fontSize)
    Block(pdf, 0, p, "L,R", 1, 'C')
    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "ลงชื่อผู้ขอบัญชี (____________________________)    ", 'R', 1, 'R')
    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "(____________________________)    ", 'R', 1, 'R')
    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "ตำแหน่ง ______________________________    ", 'R', 1, 'R')
    Block(pdf, 0, p, "L,R", 1, 'C')

    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "ลงชื่อหัวหน้างาน (____________________________)    ", 'R', 1, 'R')
    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "(____________________________)    ", 'R', 1, 'R')
    Block(pdf, b, p, "L", 0, 'C')
    pdf.cell(0, p, "ตำแหน่ง ______________________________    ", 'R', 1, 'R')
    # Block(pdf, b, p, "L", 1, 'C')
    Block(pdf, 0, p, "L,R", 1, 'C')

    p = 10
    i = 100
    pdf.set_font('th', 'b', fontSize)
    pdf.cell(i, p, "4. สําหรับเจ้าหน้าที่สํานักเทคโนโลยีดิจิทัลและสารสนเทศ", 'L,T')
    pdf.cell(0, p, "5. ข้าพเจ้าได้รับใบส่งมอบรหัสบัญชีเรียบร้อยแล้ว", 'L,R,T', 1)

    pdf.set_font('th', '', fontSize)
    # 17 line
    pdf.cell(i, p, "ลงชื่อ _______________________________ ผู้ดำเนินการ", 'L', 0, 'L')
    pdf.cell(0, p, "ลงชื่อ _________________________________ ผู้รับ", 'L,R', 1, 'L')

    pdf.cell(i, p, "วันที่ _________________________________________", 'L', 0, 'L')
    pdf.cell(0, p, "วันที่ _____________________________________", 'L,R', 1, 'L')

    Block(pdf, i, 4, "L, R", 0, 'C')
    Block(pdf, 0, 4, "R", 1, 'C')

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "รายละเอียด", 'L, T', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)

    p = 10
    dash(pdf, p, 167, 'T')
    Block(pdf, 0, p, "R,T", 1, 'C')

    Block(pdf, 3, p, "L", 0, 'C')
    dash(pdf, 8, 185, 0)
    Block(pdf, 0, p, "R", 1, 'C')

    pdf.cell(0, 2, "", "B, L,R", 1)

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)


def dash(o: PDF, h, r, b):
    [o.cell(1, h, "_", b, 0, 'C') for _ in range(r)]

def cdash(o: PDF, h, r, b):
    [o.cell(1, h, "_", b, 0, 'C') for _ in range(r)]