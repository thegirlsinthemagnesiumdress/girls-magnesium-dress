from django.http import JsonResponse, Http404
from django.views import View
from django.template.loader import get_template


class Filters:
    @staticmethod
    def by_id(queryset, id_arg, request):
        return queryset.filter(pk=id_arg)


class APIView(View):
    model = None
    form = None
    filters = {} # Dictionary of QS param: filter func, which is passed the queryset, querystring param and request
    template = None # Optional template to include in the response
    is_singular = False # Whether this is a single ID

    manager = "objects"

    def _convert_to_dictionary(self, instance):
        form = self.form(instance=instance)
        return form.initial

    def _build_json_content(self, queryset):
        if self.is_singular:
            if len(queryset[:2]) > 1:
                raise ValueError("Too many objects returned")

            instance = queryset.first()
            if not instance:
                raise Http404("Instance does not exist")
            queryset = [instance]

        content = {}

        template = None
        if self.template:
            template = get_template(self.template)

        result_count = 0
        for instance in queryset:
            data = self._convert_to_dictionary(instance)
            data["pk"] = instance.pk

            if template:
                data["__html__"] = template.render(
                    { "instance": instance },
                    self.request
                )

            # If this API just returns a singular result, return this one now
            if self.is_singular:
                content["data"] = data
                return content

            content.setdefault("items", []).append(data)
            result_count += 1

        content["count"] = result_count
        return content

    def get(self, request, **kwargs):
        queryset = getattr(self.model, self.manager).all()
        for k, v in self.filters.items():
            if k in kwargs:
                queryset = v(queryset, kwargs[k], request=request)
            elif k in request.GET:
                queryset = v(queryset, request.GET[k], request=request)

        content = self._build_json_content(queryset)
        return JsonResponse(content)
