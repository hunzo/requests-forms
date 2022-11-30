from .pdf_template import PDF
from .pdf_element import TextHeader1, TextHeader2, TextSigned, TextStaff, Paragraph, Paragraph2Colum
import io
import uuid


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

    TextHeader1(pdf, "1. ผู้ใช้งาน")
    p = 8
    ident = 10
    hstyle = 'b'
    # 1 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(35, p, "ข้าพเจ้า (ภาษาไทย)", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(40, p, object["fname_th"])

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "นามสกุล")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["lname_th"], 'R', 1)

    # 2 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(32, p, "ชื่อ (ภาษาอังกฤษ)", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(40, p, object["fname"])

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "นามสกุล")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["lname"], 'R', 1)

    # 3 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(35, p, "หน่วยงาน / บริษัท", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["dept"], 'R', 1)

    # 4 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(32, p, "เบอร์โทร", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(40, p, object["tel"])

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "อีเมล")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["email"], 'R', 1)

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
    pdf.cell(32, p, "เริ่มใช้วันที่", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(40, p, str(object["start_date"]))

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "ถึงวันที่")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, str(object["end_date"]), 'R', 1)

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
    pdf.cell(10, p, "ชื่อ", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(30, p, object["co_fname_th"])

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "นามสกุล")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["co_lname_th"], 'R', 1)

    # 15 line
    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "หน่วยงาน", 'L')
    pdf.set_font('th', '', fontSize)
    pdf.cell(30, p, object["co_dept"])

    pdf.set_font('th', hstyle, fontSize)
    pdf.cell(20, p, "อีเมล ")
    pdf.set_font('th', '', fontSize)
    pdf.cell(0, p, object["email"], 'R', 1)

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

    ret = pdf.output(dest='S')

    return io.BytesIO(ret)
