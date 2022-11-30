from .pdf_template import PDF
from .pdf_element import TextHeader1, TextHeader2, TextSigned, TextStaff, Paragraph, Paragraph2Colum, Cell, Block
from math import ceil
import io
import uuid

# def Cell(pdf: PDF, text, border, ln, aligned ):
#     w = pdf.get_string_width(text) + 10
#     pdf.cell(w, 8, text, border, ln, aligned)


def vpn_request_form(object):
    pdf = PDF(
        form_title="แบบฟอร์มการขอรับบริการ VPN",
        form_subtitle="สำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
        form_iso_no="IDT-FM-IF-010 (05/05/2022)",
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

   # 1 line

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ข้าพเจ้า (ภาษาไทย)", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["fname_th"], 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "นามสกุล", 0, 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["lname_th"], 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    # 2 line

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ข้าพเจ้า (ภาษาอังกฤษ)", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["fname"], 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "นามสกุล", 0, 0, 'L', 5)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["lname"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    # 3 line
    pdf.set_font('th', hstyle, fontSize)
    # pdf.cell(35, p, "หน่วยงาน / บริษัท", 'L')
    Cell(pdf, p, "หน่วยงาน / บริษัท", 'L', 0, 'L', 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["dept"], 0, 0, 'C', 1)
    Block(pdf, 0, p, "R", 1, 'C')
    # pdf.cell(0, p, object["dept"], 'R', 1)

    # 4 line
    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "เบอร์โทร", "L", 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["tel"], 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "อีเมล", 0, 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, object["email"], 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    # 5 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(50, p, "ความจําเป็นในการขอเข้าใช้งาน", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["desc"], 'R', 1)

    # 6 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(0, p, "รายละเอียดระบบที่ต้องการขอเข้าใช้งาน ", 'L, R', 1)

    # 7 line
    pdf.set_font('th', '', fontSize)

    pdf.cell(ident, p, "", 'L')
    pdf.cell(23, p, "IP Address:")
    pdf.cell(0, p, object["ip"], 'R', 1)

    # 8 line
    pdf.cell(ident, p, "", 'L')
    pdf.cell(25, p, "Program/Port:")
    pdf.cell(0, p, object["port"], 'R', 1)

    # 9 line
    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "เริ่มใช้วันที่", "L", 0, "L", 3)
    # pdf.cell(32, p, "เริ่มใช้วันที่", 'L')
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["start_date"]), 0, 0, 'C', 3)
    # pdf.cell(40, p, str(object["start_date"]))

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ถึงวันที่", 0, 0, "L", 3)
    # pdf.cell(20, p, "ถึงวันที่")
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["end_date"]), 0, 0, 'C', 3)
    # pdf.cell(0, p, str(object["end_date"]), 'R', 1)
    Block(pdf, 0, p, "R", 1, 'C')

    # 10 line
    pdf.cell(
        0, p, "ทั้งนี้ในการขออนุญาตต้องแจ้งล่วงหน้าอย่างน้อย 2 วันทําการ", 'L,R', 1)

    # line break
    pdf.cell(0, p/2, "", 'L,R', 1)

    pdf.set_font('th', 'u', fontSize)
    # 11 line
    pdf.cell(0, p, "ข้าพเจ้ารับทราบนโยบาย และยินดีจะรับผิดชอบต่อความเสียหายที่เกิดขึ้นตาม พระราชบัญญัติว่าด้วยการกระทําความผิด", 'L,R', 1)
    # 12 line
    pdf.cell(0, p, "เกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 และที่แก้ไขเพิ่มเติม อย่างเคร่งครัดทุกประการ", 'L,R', 1)

    # line break
    pdf.cell(0, p/2, "", 'L,R', 1)

    # 13 line
    TextHeader1(
        pdf, "2. ผู้ประสานงาน / ผู้ดูแลระบบของหน่วยงานเจ้าของระบบของสถาบัน")

    hstyle = 'b'
    # 14 line
    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "ชื่อ", "L", 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["co_fname_th"]), 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "นามสกุล", 0, 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["co_lname_th"]), 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    # 15 line
    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "หน่วยงาน", "L", 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["co_dept"]), 0, 0, 'C', 3)

    pdf.set_font('th', hstyle, fontSize)
    Cell(pdf, p, "อีเมล", 0, 0, "L", 3)
    pdf.set_font('th', '', fontSize)
    Cell(pdf, p, str(object["email"]), 0, 0, 'C', 3)
    Block(pdf, 0, p, "R", 1, 'C')

    # line break
    pdf.cell(0, p/2, "", 'L,R', 1)

    # 16 line
    p = 10
    pdf.cell(80, p, "3. สําหรับ Outsource", 'L,T')
    pdf.cell(0, p, "4. สําหรับ Outsource", 'L,R,T', 1)

    # 17 line
    pdf.cell(80, p, "ลงชื่อ (____________________________)", 'L', 0, 'C')
    pdf.cell(0, p, "ลงชื่อ (____________________________)", 'L,R', 1, 'C')

    # 18 line
    pdf.cell(80, p, "         (________________________)", 'L', 0, 'C')
    pdf.cell(0, p, "         (________________________)", 'L,R', 1, 'C')

    # 19 line
    pdf.cell(80, p, "    ผู้ขอใช้งาน", 'L', 0, 'C')
    pdf.cell(0, p, "    ผู้บริหารบริษัท", 'L,R', 1, 'C')

    # 16 line
    p = 10
    pdf.cell(80, p, "5. สําหรับหน่วยงานเจ้าของระบบ", 'L,T')
    pdf.cell(0, p, "6. สําหรับผู้บริหารสํานักเทคโนโลยีดิจิทัลและสารสนเทศ", 'L,R,T', 1)

    # 17 line
    pdf.cell(80, p, "ลงชื่อ (____________________________)", 'L', 0, 'C')
    pdf.cell(0, p, "ลงชื่อ (____________________________)", 'L,R', 1, 'C')

    # 18 line
    pdf.cell(80, p, "         (________________________)", 'L', 0, 'C')
    pdf.cell(0, p, "         (________________________)", 'L,R', 1, 'C')

    # 19 line
    pdf.cell(80, p, "    ผู้บริหารหน่วยงานเจ้าของระบบ", 'L', 0, 'C')
    pdf.cell(0, p, "    ผู้บริหารสํานัก", 'L,R', 1, 'C')

    # 19 line
    pdf.cell(80, p, "วันที่______/______/______", 'L, B', 0, 'C')
    pdf.cell(0, p, "วันที่______/______/______", 'L,R, B', 1, 'C')

    # text = object["fullname"]
    # w = pdf.get_string_width(text) + 10

    # dash(pdf, 10)
    # pdf.cell(w, 10, text, 'R,L', 0, 'C')
    # dash(pdf, 190)

    # print("-"*100)
    # print(w)
    # print(ceil(w))

    # print(ceil(pdf.get_x()))

    # # pdf.cell(0, 10, "_")

    # print(ceil(pdf.get_x()))

    # pdf.ln(1)

    # max_size = 187

    # [pdf.cell(1, 10, "_") for _ in range(max_size)]

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)


def dash(o: PDF, n):
    [o.cell(1, 10, "_") for _ in range(n)]
