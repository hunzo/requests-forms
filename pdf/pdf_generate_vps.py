from .pdf_template import PDF
from .pdf_element import TextHeader1, TextHeader2, TextSigned, TextStaff, Paragraph, Cell
import io
import uuid


def vps_request_form(object):
    pdf = PDF(
        # form_title="การขอรับบริการ Virtual Private Server / domain",
        form_title=object["form_title"],
        form_subtitle="สำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
        # form_iso_no="IDT-FM-IF-010 (05/05/2022)",
        form_iso_no=object["form_iso_no"],
        form_no=str(uuid.uuid4()),

        orientation="P",
        unit="mm",
    )

    pdf.alias_nb_pages()
    pdf.add_page()

    # fontSize = 14
    # effective_page_width = pdf.w - 2*pdf.l_margin

    TextHeader2(pdf, "1. ส่วนงาน: ", object["dept"])
    TextHeader1(pdf, "2. ข้อมูลผู้ดูแลระบบหรือผู้ประสานงานของหน่วยงาน")
    Paragraph(pdf, "ชื่อ-นามสกุล", object["fullname"], 5, 8)
    Paragraph(pdf, "ตำแหน่ง", object["level"], 5, 8)
    Paragraph(pdf, "โทรศัพท์", object["tel"], 5, 8)
    Paragraph(pdf, "อีเมล", object["email"], 5, 8)

    pdf.cell(0, 5, "", 'L,R', 1)

    date_string = object["date"]

    TextHeader1(pdf, "3. รายละเอียด Virtual Private Server")
    Paragraph(pdf, "เพื่อใช้งาน", object["desc"], 5, 8)
    Paragraph(pdf, "เริ่มใช้งานวันที่",
              f"{date_string},  (ต้องแจ้งล่วงหน้าอย่างน้อย 3 วันทำการ)", 5, 8)
    Paragraph(pdf, "ระบบปฏิบัติการ", object["os_name"], 5, 8)

    pdf.cell(5, 8, "", 'L')
    vps_tmp = object["vps_template"]
    pdf.cell(
        # 0, 8, txt=f"รายละเอียด: {cpu} vCPUs, Memory: {memory} GB, HDD: {disk} GB", ln=1, border="R")
        0, 8, txt=f"รายละเอียด: {vps_tmp}", ln=1, border="R")

    pdf.cell(
        0, 9, "หากมีข้อสงสัยในการกรอกข้อมูล ติดต่อสอบถามได้ที่ โทร 02-727-3246", 'L,R', 1)
    pdf.cell(0, 1, "", 'L,R, B', 1)

    # TextHeader2(pdf, "4. ชื่อโดเมน: ", 20, object["domain"])
    TextHeader2(pdf, "4. ชื่อโดเมน: ", object["domain"])

    pdf.set_font("th", 'B', 16)
    pdf.cell(0, 10, "5. ข้าพเจ้ารับทราบนโยบาย และยินดีจะรับผิดชอบต่อความเสียหายที่เกิดขึ้นตาม พระราชบัญญัติว่าด้วยการกระทำ", 'L, R, T', 1)
    pdf.cell(0, 3, "   ความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. 2550 และที่แก้ไขเพิ่มเติม อย่างเคร่งครัดทุกประการ", 'L,R', 1)
    pdf.cell(0, 5, "", 'L,R', 1)

    TextSigned(pdf, object["fullname"])
    pdf.cell(0, 3, "", 'L,R', 1)

    TextStaff(pdf)


    
    ret = pdf.output(dest='S')

    return io.BytesIO(ret)

def vpn_request_form(object):
    render_pdf = PDF(
        form_title="การขอรับบริการ Virtual Private Server / domain",
        form_subtitle="สำนักเทคโนโลยีดิจิทัลและสารสนเทศ",
        form_iso_no="IDT-FM-IF-010 (05/05/2022)",
        form_no=str(uuid.uuid4()),

        orientation="P",
        unit="mm",
    )

    render_pdf.alias_nb_pages()
    render_pdf.add_page()

    ret = render_pdf.output(dest='S')

    return io.BytesIO(ret)
