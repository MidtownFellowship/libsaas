from libsaas.services import base

from . import resource


# class AddonsBase(resource.RecurlyResource):

#     path = 'add_ons'


# class Addons(AddonsBase):

#     def update(self, *args, **kwargs):
#         raise base.MethodNotSupported()

#     def delete(self, *args, **kwargs):
#         raise base.MethodNotSupported()


# class Addon(AddonsBase):

#     def create(self, *args, **kwargs):
#         raise base.MethodNotSupported()


class EventsBase(resource.BrownPaperTicketsResource):

    path = 'eventlist'


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


# class Event(EventsBase):
#     # REVIEW ME Am I doing something "extra" for this?
#     def create(self, *args, **kwargs):
#         raise base.MethodNotSupported()

#     # @base.resource(Addons)
#     # def addons(self):
#     #     """
#     #     Return the resource corresponding to all the add-ons for the plan.
#     #     """
#     #     return Addons(self)

#     # @base.resource(Addon)
#     # def addon(self, add_on_code):
#     #     """
#     #     Return the resource corresponding to a single plan's add-on.
#     #     """
#     #     return Addon(self, add_on_code)
