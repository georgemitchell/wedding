from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView


def index(request):
    # Load the template myblog/templates/index.html
    template = loader.get_template('wedding/home.html')
    context = Context({})

    return HttpResponse(template.render(context))


def couple(request):
    template = loader.get_template('wedding/couple.html')
    return HttpResponse(template.render(Context({})))


def story(request):
    template = loader.get_template('wedding/story.html')
    return HttpResponse(template.render(Context({})))


def people(request):
    template = loader.get_template('wedding/people.html')
    return HttpResponse(template.render(Context({})))


def wedding(request):
    template = loader.get_template('wedding/wedding.html')
    return HttpResponse(template.render(Context({})))


def gifts(request):
    template = loader.get_template('wedding/gifts.html')
    return HttpResponse(template.render(Context({})))


def travel(request):
    template = loader.get_template('wedding/travel.html')
    return HttpResponse(template.render(Context({})))


def traverse_city(request):
    template = loader.get_template('wedding/traverse_city.html')
    return HttpResponse(template.render(Context({})))


def leelanau(request):
    template = loader.get_template('wedding/leelanau.html')
    return HttpResponse(template.render(Context({})))


def old_mission(request):
    template = loader.get_template('wedding/old_mission.html')
    return HttpResponse(template.render(Context({})))


class RSVPCreateView(CreateView):
    form_class = None
    success_url = None
    is_ajax = False

    def get_successful_json_data(self, model_instance, context):
        return {
            "success": True,
            "created_id": model_instance.id
        }

    def get(self, request, *args, **kwargs):
        form = None #self.form_class()
        self.object = None
        context = super(RSVPCreateView, self).get_context_data(**kwargs)
        return render(request, "base.html", {'form': form})

    def post(self, request, *args, **kwargs):
        self.object = None
        if self.form_class is None:
            raise RuntimeError('View requires form_class argument to be set')
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            model_instance = form.save()
            if self.is_ajax:
                return JsonResponse(self.get_successful_json_data(model_instance, self.get_context_data()))
            else:
                return redirect(self.success_url)
        else:
            fields = []
            for field in form:
                if len(field.errors) > 0:
                    entry = {"id": field.id_for_label, "label": field.label, "errors": []}
                    for error in field.errors:
                        entry["errors"].append(error)
                    fields.append(entry)
            if self.is_ajax:
                json = {
                    "success": False,
                    "errors": fields
                }
                return JsonResponse(json)
            return render(request, self.template_name, {'form': form})

