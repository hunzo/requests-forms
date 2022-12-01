from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import FileResponse
# Create your views here.

from .forms import VPS_FORMS, COLO_FORMS, DOMAIN_FORMS, VPN_FORMS, ACCOUNT_FORMS, GUEST_FORMS
from pdf.pdf_generate_vps import vps_request_form
from pdf.pdf_generate_colo import colo_request_form
from pdf.pdf_generate_vpn import vpn_request_form
from pdf.pdf_generate_account import account_request_form

from datetime import datetime


def Home(request):

    context = {
        "title": "Forms",
        "data": [
            {
                "name": "แบบฟอร์มการขอรับบริการ Virtual Private Server",
                "link": reverse("vps-form")
            },
            {
                "name": "แบบฟอร์มการขอรับบริการ Co-Location",
                "link": reverse("colo-form")
            },
            {
                "name": "แบบฟอร์มการขอรับบริการ VPN",
                "link": reverse("vpn-form")
            },
            {
                "name": "แบบฟอร์มการขอบัญชีผู้ใช้งานเครือข่ายอินเทอร์เน็ตแบบชั่วคราว LAN, WIFI",
                "link": reverse("account-form")
            },
            {
                "name": "แบบฟอร์มขอใช้อินเทอร์เน็ต สำหรับผู้เข้าอบรม / โครงการความร่วมมือ",
                "link": reverse("guest-form")
            },
            {
                "name": "แบบฟอร์มการขอรับบริการ Domain",
                "link": reverse("domain-form")
            },
        ]
    }
    return render(request, "home.html", context)


def VPSHome(request):
    title = "แบบฟอร์มการขอรับบริการ Virtual Private Server"
    iso = "IDT-FM-IF-010"
    if request.method == "POST":

        form = VPS_FORMS(request.POST)

        if form.is_valid():

            fullname = form.cleaned_data["fname_th"] + \
                " " + form.cleaned_data["lname_th"]

            payload = form.cleaned_data
            payload["fullname"] = fullname
            payload["desc"] = str(
                form.cleaned_data["desc"]).replace("\r\n", " ")
            payload["form_title"] = title
            payload["form_iso_no"] = iso

            buffer = vps_request_form(payload)

            timenow = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            return FileResponse(buffer, filename=f"ISO-{iso}-{timenow}.pdf", as_attachment=False)

        # show alert message
        print(form.is_valid())

        return redirect("vps-form")

    form = VPS_FORMS(initial={"domain": "ยังไม่ได้กำหนดชื่อ domain"})
    context = {
        "title": title,
        "form": form
    }

    return render(request, 'request.html', context)


def COLOHome(request):
    title = "แบบฟอร์มการขอรับบริการ Co-Location"
    iso = "IDT-FM-IF-010"

    if request.method == "POST":

        form = COLO_FORMS(request.POST)
        print(form.data)

        if form.is_valid():

            fullname = form.cleaned_data["fname_th"] + \
                " " + form.cleaned_data["lname_th"]

            payload = form.cleaned_data
            payload["fullname"] = fullname
            payload["server_info"] = str(
                form.cleaned_data["server_info"]).replace("\r\n", " ")

            payload["form_title"] = title
            payload["form_iso_no"] = iso

            buffer = colo_request_form(payload)

            timenow = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            return FileResponse(buffer, filename=f"account-info-{timenow}.pdf", as_attachment=False)

        # show alert message
        print(form.is_valid())
        print(form.errors)

        return redirect("colo-form")

    form = COLO_FORMS(
        initial={"inv_no": "xx-xx-xxxxxx-xxx", "os": "windows server"})
    context = {
        "title": title,
        "form": form
    }

    return render(request, 'request.html', context)


def VPNHome(request):

    title = "แบบฟอร์มการขอรับบริการ Co-Location"
    iso = "IDT-FM-IF-010"

    if request.method == "POST":

        form = VPN_FORMS(request.POST)
        print(form.data)

        if form.is_valid():

            fullname = form.cleaned_data["fname_th"] + \
                " " + form.cleaned_data["lname_th"]

            payload = form.cleaned_data
            payload["fullname"] = fullname
            payload["desc"] = str(
                form.cleaned_data["desc"]).replace("\r\n", " ")

            payload["form_title"] = title
            payload["form_iso_no"] = iso

            buffer = account_request_form(payload)

            timenow = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            return FileResponse(buffer, filename=f"{iso}-info-{timenow}.pdf", as_attachment=False)

        # show alert message
        print(form.is_valid())
        print(form.errors)

        return redirect("vpn-form")

    form = VPN_FORMS()
    context = {
        "title": title,
        "form": form
    }

    return render(request, 'request.html', context)


def ACCOUNTHome(request):

    title = "แบบฟอร์มการขอบัญชีผู้ใช้งานเครือข่ายอินเทอร์เน็ตแบบชั่วคราว"
    iso = "IDT-FM-IF-007"

    if request.method == "POST":

        form = ACCOUNT_FORMS(request.POST)
        print(form.data)

        if form.is_valid():

            fullname = form.cleaned_data["fname_th"] + \
                " " + form.cleaned_data["lname_th"]

            payload = form.cleaned_data
            payload["fullname"] = fullname
            # payload["desc"] = str(
            #     form.cleaned_data["desc"]).replace("\r\n", " ")

            payload["form_title"] = title
            payload["form_iso_no"] = iso

            buffer = account_request_form(payload)

            timenow = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            return FileResponse(buffer, filename=f"account-info-{timenow}.pdf", as_attachment=False)

        # show alert message
        print(form.is_valid())
        print(form.errors)

        return redirect("account-form")

    form = ACCOUNT_FORMS()
    context = {
        "title": title,
        "form": form
    }

    return render(request, 'request.html', context)


def GUESTHome(request):
    form = GUEST_FORMS()
    context = {
        "title": "แบบฟอร์มขอใช้อินเทอร์เน็ต สำหรับผู้เข้าอบรม / โครงการความร่วมมือ",
        "form": form
    }
    return render(request, "request.html", context)


def DOMAINHome(request):
    form = DOMAIN_FORMS()
    context = {
        "title": "แบบฟอร์มการขอรับบริการ Domain",
        "form": form
    }
    return render(request, "request.html", context)
