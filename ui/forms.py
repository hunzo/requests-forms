from django import forms
from .models import VPS, COLO, ACCOUNT, GUEST, DOMAIN, VPN


class VPS_FORMS(forms.ModelForm):
    os_choice = (
        ("Ubuntu 16.0.4 TLS", "Ubuntu 16"),
        ("Ubuntu 19.0.4 TLS", "Ubuntu 19"),
        ("Ubuntu 20.0.4 TLS", "Ubuntu 20"),
        ("Ubuntu 21.0.4 TLS", "Ubuntu 21"),
        ("Ubuntu 22.0.4 TLS", "Ubuntu 22"),
        ("CentOS 7 ", "CentOS 7"),
        ("CentOS 8 ", "CentOS 8"),
        ("Oracle Linux", "OracleLinux"),
        ("Windows Server 2012", "Windows Server 2012"),
        ("Windows Server 2016", "Windows Server 2016"),
        ("Windows Server 2019", "Windows Server 2019"),
    )
    os_name = forms.ChoiceField(
        choices=os_choice, widget=forms.Select(attrs={'class': 'form-select'}), label="Operating System")

    vps_choice = (
        ("1 vcpu, memory 1G, disk 50G", "1 vcpu, memory 1G, disk 50G"),
        ("1 vcpu, memory 2G, disk 50G", "1 vcpu, memory 2G, disk 50G"),
        ("1 vcpu, memory 4G, disk 50G", "1 vcpu, memory 4G, disk 50G"),
        ("2 vcpu, memory 2G, disk 100G", "2 vcpu, memory 2G, disk 100G"),
        ("2 vcpu, memory 2G, disk 100G", "2 vcpu, memory 4G, disk 100G"),
        ("4 vcpu, memory 4G, disk 100G", "4 vcpu, memory 4G, disk 100G"),
        ("4 vcpu, memory 8G, disk 100G", "4 vcpu, memory 8G, disk 100G"),
    )

    vps_template = forms.ChoiceField(
        choices=vps_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="VPS Templates")

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันทีเริ่มใช้งาน"
    )

    class Meta:
        model = VPS
        fields = '__all__'
        labels = {
            "fname_th": "ชื่อ",
            "lname_th": "นามสกุล",
            "level": "ตำแหน่ง",
            "desc": "รายละเอียดการใช้งาน",
            "dept": "คณะ / สำนัก / ส่วนงาน",
            "tel": "เบอร์โทรศัพท์ ติดต่อผู้ประสานงาน",
            "email": "email ติดต่อผู้ประสานงาน",
        }
        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "domain": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 10}),
        }

        exclude = ("vcpu", "memory", "disk", "os")


class COLO_FORMS(forms.ModelForm):

    prefix_choice = (
        ("นาย", "นาย"),
        ("นาง", "นาง"),
        ("นางสาว", "นางสาว"),
    )

    prefix = forms.ChoiceField(
        choices=prefix_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="ข้าพเจ้า")

    class Meta:
        model = COLO
        fields = '__all__'
        labels = {
            "fname_th": "ชื่อ (ภาษาไทย)",
            "lname_th": "นามสกุล (ภาษาไทย)",
            "dept": "คณะ / สำนัก / ส่วนงาน",
            "level": "ตำแหน่ง",
            "tel": "เบอร์โทรติดต่อ",
            "server_info": "รายละเอียดเครื่องแม่ข่าย / ยี่ห้อรุ่น",
            "inv_no": "รหัสครุภัณฑ์",
            "os": "ระบบปฏิบัติการ OS",
            "rack_size": "ขนาดเครื่องแม่ข่าย U",
        }
        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "server_info": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 10}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "inv_no": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "os": forms.TextInput(attrs={'class': 'form-control'}),
            "rack_size": forms.TextInput(attrs={'class': 'form-control'}),
        }


class ACCOUNT_FORMS(forms.ModelForm):
    person_choice = (
        ("อาจารย์พิเศษ", "อาจารย์พิเศษ"),
        ("ผู้ช่วยนักวิจัย", "ผู้ช่วยนักวิจัย"),
        ("ผู้ทำงานในโครงการความร่วมมือของสถาบัน",
         "ผู้ทำงานในโครงการความร่วมมือของสถาบัน"),
    )

    person_type = forms.ChoiceField(
        choices=person_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="ประเภทผู้ใช้งาน")

    prefix_choice = (
        ("นาย", "นาย"),
        ("นาง", "นาง"),
        ("นางสาว", "นางสาว"),
    )

    prefix = forms.ChoiceField(
        choices=prefix_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="ข้าพเจ้า")

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันทีเริ่มใช้งาน"
    )

    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันที่สิ้นสุดการใช้งาน"
    )

    class Meta:
        model = ACCOUNT
        fields = '__all__'
        labels = {
            "fname_th": "ชื่อ",
            "lname_th": "นามสกุล",
            "fname": "ชื่อ (ภาษาอังกฤษ)",
            "lname": "นามสกุล (ภาษาอังกฤษ)",
            "dept": "คณะ / สำนัก / ส่วนงาน",
            "tel": "เบอร์โทรศัพท์ ติดต่อผู้ประสานงาน",
            "email": "อีเมลสำรอง (อีเมลสำหรับติดต่อ ใส่อีเมลอื่นที่ไม่ใช่อีเมลของสถาบัน)",
            "cid": "เลขบัตรประชาชน / เลขหนังสือเดินทาง",
        }
        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "fname": forms.TextInput(attrs={'class': 'form-control'}),
            "lname": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "cid": forms.TextInput(attrs={'class': 'form-control'}),
        }


class GUEST_FORMS(forms.ModelForm):
    prefix_choice = (
        ("นาย", "นาย"),
        ("นาง", "นาง"),
        ("นางสาว", "นางสาว"),
    )

    prefix = forms.ChoiceField(
        choices=prefix_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="ข้าพเจ้า")

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันทีเริ่มใช้งาน"
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันที่สิ้นสุดการใช้งาน"
    )

    class Meta:
        model = GUEST
        fields = '__all__'
        labels = {
            "fname_th": "ชื่อ (ภาษาไทย)",
            "lname_th": "นามสกุล (ภาษาไทย)",
            "dept": "คณะ / สำนัก / ส่วนงาน",
            "level": "ตำแหน่ง",
            "accounts": "จำนวนบัญชีผู้ใช้อินเทอร์เน็ตที่ต้องการ",
            "tel": "เบอร์โทรติดต่อ",
            "desc": "มีความประสงค์ขอบัญชีผู้ใช้งานเครือข่ายอินเทอร์เน็ตสำหรับ (60 ตัวอักษร)",
        }
        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "accounts": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 10}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "domain": forms.TextInput(attrs={'class': 'form-control'}),
        }


class DOMAIN_FORMS(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันทีเริ่มใช้งาน"
    )
    prefix_choice = (
        ("นาย", "นาย"),
        ("นาง", "นาง"),
        ("นางสาว", "นางสาว"),
    )

    prefix = forms.ChoiceField(
        choices=prefix_choice, widget=forms.Select(
            attrs={'class': 'form-select'}), label="ข้าพเจ้า")

    class Meta:
        model = DOMAIN
        fields = '__all__'
        labels = {
            "fname_th": "ชื่อ (ภาษาไทย)",
            "lname_th": "นามสกุล (ภาษาไทย)",
            "dept": "คณะ / สำนัก / ส่วนงาน",
            "level": "ตำแหน่ง",
            "domain": "ชื่อโดเมนที่ต้องการ",
            "tel": "เบอร์โทรติดต่อ",
            "desc": "มีความประสงค์ขอรับบริการโดเมนสำหรับ (60 ตัวอักษร)",
        }
        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 10}),
            "level": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "domain": forms.TextInput(attrs={'class': 'form-control'}),
        }


class VPN_FORMS(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันทีเริ่มใช้งาน"
    )

    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control"}
        ),
        label="วันที่สิ้นสุดการใช้งาน"
    )

    class Meta:
        model = VPN
        fields = '__all__'

        labels = {
            "co_fname_th": "ชื่อ-ผู้ประสานงาน (ภาษาไทย)",
            "co_lname_th": "นามสกุล-ผู้ประสานงาน (ภาษาไทย)",
            "fname_th": "ชื่อ-ผู้ปฎิบัติงาน",
            "lname_th": "นามสกุล-ผู้ปฎิบัติงาน",
            "fname": "ชื่อ-ผู้ปฎิบัติงาน (ภาษาอังกฤษ)",
            "lname": "นามสกุล-ผู้ปฎิบัติงาน (ภาษาอังกฤษ)",
            "co_dept": "คณะ / สำนัก / ส่วนงาน",
            "dept": "หน่วยงาน / บริษัท",
            "tel": "เบอร์โทรศัพท์ ติดต่อผู้ประสานงาน",
            "email": "อีเมลสำรอง (อีเมลสำหรับติดต่อ ใส่อีเมลอื่นที่ไม่ใช่อีเมลของสถาบัน)",
            "cid": "เลขบัตรประชาชน / เลขหนังสือเดินทาง",
            "ip": "IP Address ปลายทาง",
            "port": "Program/Port ที่ต้องการใช้งาน",
            # "desc": "ความจำเป็นในการขอเข้าใช้งาน(กรณีอื่นๆกรอกข้อมูลไม่เกิน 40 ตัวอักษร)"
            "desc": "ความจำเป็นในการขอเข้าใช้งาน(กรอกข้อมูลไม่เกิน 40 ตัวอักษร)"
        }

        widgets = {
            "fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "co_fname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "co_lname_th": forms.TextInput(attrs={'class': 'form-control'}),
            "fname": forms.TextInput(attrs={'class': 'form-control'}),
            "lname": forms.TextInput(attrs={'class': 'form-control'}),
            "dept": forms.TextInput(attrs={'class': 'form-control'}),
            "co_dept": forms.TextInput(attrs={'class': 'form-control'}),
            "tel": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "cid": forms.TextInput(attrs={'class': 'form-control'}),
            "ip": forms.TextInput(attrs={'class': 'form-control'}),
            "port": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 10}),
        }
