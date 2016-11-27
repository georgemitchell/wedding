from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView

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

