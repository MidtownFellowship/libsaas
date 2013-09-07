from libsaas.services import base
from libsaas import http, parsers
from . import resource

class DatesBase(resource.BrownPaperTicketsResource):

    path = 'datelist'

    @base.apimethod
    def get(self, event_id=None):
        param_names = None
        params = base.get_params(param_names, locals())
        request = http.Request('GET', self.get_url(), params)
        return request, parsers.parse_xml

    def get_url(self):
        return "{}/{}".format(self.parent.parent.apiroot, self.path)

class Dates(DatesBase):

    def __init__(self, parent, event_id=None):
        super(Dates, self).__init__(parent)
        self.event_id = event_id
        self.add_filter(self.add_event_id)

    def add_event_id(self, request):
        request.params.update({'event_id': self.event_id})

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Date(DatesBase):

    def __init__(self, parent, object_id):
        date_id = object_id
        object_id = None
        super(Date, self).__init__(parent, object_id)
        self.date_id = date_id
        self.add_filter(self.add_date_id)


    def add_date_id(self, request):
        request.params.update({'date_id': self.date_id})

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()


class EventsBase(resource.BrownPaperTicketsResource):

    path = 'eventlist'
    @base.apimethod

    def get(self, client=None, cursor=None, per_page=None):
        """
        For single-object resources, fetch the object's data. For collections,
        fetch all of the objects.

        :var cursor: For collections, where should paging start. If left as
            `None`, the first page is returned.
        :vartype cursor: int

        :var per_page: For collections, how many objects sould be returned. The
            maximum is 200. If left as `None`, 50 objects are returned.
        :vartype per_page: int
        """
        param_names = None
        params = base.get_params(param_names, locals())
        request = http.Request('GET', self.get_url(), params)
        return request, parsers.parse_xml


class AllEvents(EventsBase):
    # Will fail if we call it
    # Ref https://github.com/jacobwegner/libsaas/issues/1
    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Events(EventsBase):
    # REVIEW ME Which methods are supported?  I think just GET
    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Event(EventsBase):
    def __init__(self, parent, object_id):
        event_id = object_id
        object_id = None
        super(Event, self).__init__(parent, object_id)
        self.event_id = event_id
        self.add_filter(self.add_event_id)


    def add_event_id(self, request):
        request.params.update({'event_id': self.event_id})

    # REVIEW ME Am I doing something "extra" for this?
    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    @base.resource(Dates)
    def dates(self):
        """
        Return the resource corresponding to all the add-ons for the plan.
        """
        return Dates(self, event_id=self.event_id)

    @base.resource(Date)
    def date(self, date_id):
        """
        Return the resource corresponding to a single plan's add-on.
        """
        return Date(self, date_id)
