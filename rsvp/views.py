from django.shortcuts import render
from .forms import RSVPForm, EmailCheckForm, GuestForm, NotAttendingForm
from .models import MEALS, RSVP, AccessCode, Guest, NotAttending
from django.views.generic.base import ContextMixin, View, TemplateResponseMixin
from django.views.generic.edit import CreateView
from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.forms.formsets import BaseFormSet
from django.forms.formsets import formset_factory
from email import send_access_code, send_confirmation_email
import datetime
import random
import string


class AjaxEmailCheck(CreateView):
    form_class = RSVPForm
    template_name = 'rsvp/ajax/email_check.html'
    is_ajax = True

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            email = self.cleaned_data["email"]
            try:
                rsvp = RSVP.objects.get(email=email)
                form.instance = rsvp
            except RSVP.DoesNotExist:
                pass


class AccessCodeMixin(object):
    def validate_access_code(self, rsvp, access_code):
        if access_code == None:
            ac = []
        else:
            ac = AccessCode.objects.filter(rsvp=rsvp, access_code=access_code, expires__gt=datetime.datetime.utcnow())
        if len(ac) == 0:
            if access_code == None:
                expired = AccessCode.objects.filter(rsvp=rsvp, access_code=access_code).order_by('-expires').first()
            else:
                expired = None
            return False, expired, AccessCode.objects.filter(rsvp=rsvp, expires__gt=datetime.datetime.utcnow()).order_by('-expires').first()
        else:
            return True, ac[0], ac[0]


class RSVPDetails(View, TemplateResponseMixin, ContextMixin, AccessCodeMixin):
    template_name = "rsvp/rsvp_details.html"
    invalid_code_template = "rsvp/invalid_code.html"

    is_ajax = False

    GuestFormSet = formset_factory(GuestForm, extra=0)

    def get_guest_data(self, rsvp):
        guests = Guest.objects.filter(rsvp=rsvp)
        output = []
        for guest in guests:
            output.append(guest)
        extra = rsvp.num_guests_allowed - len(output)
        for i in range(extra):
            output.append(Guest())
        return output

    def get_rsvp_data(self, rsvp_id, access_code):
        try:
            rsvp = RSVP.objects.get(pk=rsvp_id)
        except RSVP.DoesNotExist:
            raise Http404("RSVP does not exist")

        valid, expires, working = self.validate_access_code(rsvp, access_code)

        if not valid:
            context = self.get_context_data()
            context["rsvp"] = rsvp
            context["expired"] = expires
            context["working"] = working
            self.template_name = self.invalid_code_template
        else:
            rsvp_form = RSVPForm(instance=rsvp)

            try:
                not_attending = NotAttending.objects.get(rsvp=RSVP)
                not_attending_form = NotAttendingForm(prefix='na', instance=not_attending)
            except NotAttending.DoesNotExist:
                not_attending_form = NotAttendingForm(prefix='na')

            guests = self.get_guest_data(rsvp)
            guest_data = [{'name': g.name, 'meal': g.meal}
                for g in guests]

            context = self.get_context_data(form=rsvp_form)
            context["rsvp"] = rsvp
            context["access_code"] = working
            context["not_attending_form"] = not_attending_form
            context["guest_formset"] = self.GuestFormSet(initial=guest_data)
            context["meal_choices"] = MEALS
            context["ajax"] = self.is_ajax
        return context

    def get(self, request, *args, **kwargs):
        if kwargs.has_key("access_code"):
            access_code = kwargs["access_code"]
        else:
            access_code = request.GET.get("access_code", None)
        context = self.get_rsvp_data(kwargs["pk"], access_code)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_rsvp_data(kwargs["pk"], kwargs["access_code"])
        try:
            rsvp = RSVP.objects.get(pk=kwargs["pk"])
        except RSVP.DoesNotExist:
            raise Http404("RSVP does not exist")

        valid, expires, working = self.validate_access_code(rsvp, kwargs["access_code"])

        if not valid:
            context = self.get_context_data()
            context["rsvp"] = rsvp
            context["expired"] = expires
            context["working"] = working
            self.template_name = self.invalid_code_template
            return self.render_to_response(context)
        else:
            NotAttending.objects.filter(rsvp=rsvp).delete()
            Guest.objects.filter(rsvp=rsvp).delete()
            rsvp_form = RSVPForm(request.POST, instance=rsvp)
            
            if int(request.POST["attending"]) == 1:
                guest_formset = self.GuestFormSet(request.POST)

                if rsvp_form.is_valid() and guest_formset[0].is_valid():
                    print rsvp_form.cleaned_data["message"]
                    print rsvp_form.cleaned_data["telephone"]
                    rsvp_form.save()
                    guests = []
                    for guest_form in guest_formset:
                        if guest_form.is_valid():
                            name = guest_form.cleaned_data.get('name')
                            meal = guest_form.cleaned_data.get('meal')
                            guest = Guest(rsvp=rsvp, name=name, meal=meal)
                            guest.save()
                            guests.append(guest)
                    context = self.get_context_data()
                    context["access_code"] = working
                    context["guests"] = guests
                    context["rsvp"] = rsvp
                    self.template_name = "rsvp/confirmation.html"
                    return self.render_to_response(context)
                else:
                    context = self.get_context_data(form=rsvp_form)
                    context["rsvp"] = rsvp
                    context["not_attending_form"] = NotAttendingForm(prefix='na')
                    context["guest_formset"] = guest_formset
                    context["meal_choices"] = MEALS
                    context["ajax"] = self.is_ajax
                    return self.render_to_response(context)
            else:
                not_attending = NotAttending(rsvp=rsvp)
                not_attending_form = NotAttendingForm(request.POST, prefix='na', instance=not_attending)
                if rsvp_form.is_valid() and not_attending_form.is_valid():
                    rsvp_form.save()
                    not_attending_form.save()
                    not_attending = NotAttending.objects.get(rsvp=rsvp)
                    context = self.get_context_data()
                    context["access_code"] = working
                    context["not_attending"] = not_attending
                    context["rsvp"] = rsvp
                    self.template_name = "rsvp/confirmation.html"
                    return self.render_to_response(context)
                else:
                    guests = self.get_guest_data(rsvp)
                    guest_data = [{'name': g.name, 'meal': g.meal}
                        for g in guests]

                    context = self.get_context_data(form=rsvp_form)
                    context["rsvp"] = rsvp
                    context["not_attending_form"] = not_attending_form
                    context["guest_formset"] = self.GuestFormSet(initial=guest_data)
                    context["meal_choices"] = MEALS
                    context["ajax"] = self.is_ajax
                    return self.render_to_response(context)


class AjaxRSVPDetails(RSVPDetails):
    template_name = "rsvp/ajax/rsvp_details.html"
    is_ajax = True


class EmailCheck(CreateView):
    form_class = EmailCheckForm
    template_name = 'wedding/rsvp.html'
    is_ajax = True

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        try:
            rsvp = RSVP.objects.get(email=form.data["email"])
            form.instance = rsvp
            self.object = rsvp
            # response redirect here?
            print "Found existing"
        except RSVP.DoesNotExist:
            self.object = self.form.save()
            print self.object
            pass
        if form.is_valid():
            email = self.cleaned_data["email"]
            try:
                rsvp = RSVP.objects.get(email=email)
                self.object = rsvp
                form.instance = rsvp
                print "Found existing"
            except RSVP.DoesNotExist:
                self.object = self.form.save()
                print self.object
                pass
            return self.form_valid(form)
        else:
            print "oops"
            self.object = None
            return self.form_invalid(form)


def generate_access_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))


def get_access_code(rsvp):
    access_code = AccessCode.objects.filter(rsvp=rsvp, expires__gt=datetime.datetime.utcnow())
    if len(access_code) == 0:
        expires = datetime.datetime.utcnow() + datetime.timedelta(hours=48)
        access_code = AccessCode(rsvp=rsvp, access_code=generate_access_code(), expires=expires)
        access_code.save()
        return access_code, True
    else:
        return access_code[0], False


def email_check(request):
    email = request.GET.get("email", None)
    if email:
        email = email.lower()
        try:
            rsvp = RSVP.objects.get(email=email)
        except RSVP.DoesNotExist:
            rsvp = RSVP(email=email)
            rsvp.save()
        access_code, is_new = get_access_code(rsvp)
        if is_new:
            send_access_code(rsvp, access_code)
        c = {
            "rsvp": rsvp,
            "access_code": access_code,
            "is_new": is_new
        }
        template = loader.get_template('rsvp/ajax/access_code.html')
    else:
        c = {}
        template = loader.get_template('rsvp/rsvp.html')
    return HttpResponse(template.render(Context(c)))


def ajax_access_code(request):
    template = loader.get_template('rsvp/ajax/access_code.html')
    c = {}
    c.update(csrf(request))
    return HttpResponse(template.render(Context(c)))


def access_email(request):
    access_code = AccessCode(access_code="OUTATIME")
    rsvp = RSVP(id=1)
    template = loader.get_template('email/password.html')
    return HttpResponse(template.render(Context({"access_code":access_code, "rsvp": rsvp})))


def send_link(request, rsvp_id):
    try:
        rsvp = RSVP.objects.get(pk=rsvp_id)
    except RSVP.DoesNotExist:
        raise Http404()

    access_code, is_new = get_access_code(rsvp)
    send_access_code(rsvp, access_code)
    c = {
            "rsvp": rsvp,
            "access_code": access_code,
            "is_new": is_new
        }
    template = loader.get_template('rsvp/send_link.html')
    return HttpResponse(template.render(Context(c)))


def send_confirmation(request, rsvp_id, access_code):
    try:
        rsvp = RSVP.objects.get(pk=int(rsvp_id))
        ac = AccessCode.objects.get(rsvp=rsvp, access_code=access_code)
        guests = Guest.objects.filter(rsvp=rsvp)
    except RSVP.DoesNotExist:
        raise Http404()
    except AccessCode.DoesNotExist:
        raise Http404()

    send_confirmation_email(rsvp, guests)
    template = loader.get_template('rsvp/complete.html')
    return HttpResponse(template.render({}))
