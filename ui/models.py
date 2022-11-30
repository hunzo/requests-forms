from django.db import models

# Create your models here.


class VPS(models.Model):

    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    desc = models.TextField()
    email = models.EmailField()
    date = models.DateField()
    domain = models.CharField(max_length=30)
    vps_template = models.CharField(max_length=50)
    os_name = models.CharField(max_length=20)


class COLO(models.Model):

    prefix = models.CharField(max_length=5)
    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    server_info = models.TextField()
    inv_no = models.CharField(max_length=20)
    os = models.CharField(max_length=30)
    rack_size = models.CharField(max_length=10)


class VPN(models.Model):
    desc_choice = (
        ("บริษัทผู้ทำการพัฒนา / ผู้ดูแลระบบ", "บริษัทผู้ทำการพัฒนา / ผู้ดูแลระบบ"),
        ("หน่วยงานเจ้าของระบบ / ผู้ใช้งาน", "หน่วยงานเจ้าของระบบ / ผู้ใช้งาน"),
    )

    co_fname_th = models.CharField(max_length=20)
    co_lname_th = models.CharField(max_length=20)
    co_dept = models.CharField(max_length=20)

    # prefix = models.CharField(max_length=5)
    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    ip = models.CharField(max_length=15)
    port = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    # desc = models.CharField(max_length=40, choices=desc_choice)
    desc = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()


class ACCOUNT(models.Model):
    prefix = models.CharField(max_length=5)
    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    cid = models.CharField(max_length=30)
    dept = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    person_type = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()


class GUEST(models.Model):

    prefix = models.CharField(max_length=5)
    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    accounts = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    tel = models.CharField(max_length=20)
    desc = models.CharField(max_length=40)
    # end_date = models.DateField()


class DOMAIN(models.Model):

    prefix = models.CharField(max_length=5)
    fname_th = models.CharField(max_length=20)
    lname_th = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    domain = models.EmailField(max_length=30)
    tel = models.CharField(max_length=20)
    desc = models.CharField(max_length=40)
    start_date = models.DateField()
    # end_date = models.DateField()
