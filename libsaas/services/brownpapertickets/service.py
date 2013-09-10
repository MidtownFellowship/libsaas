from libsaas import http, xml

from libsaas.filters import auth
from libsaas.services import base

from . import events as ev
from . import orders as ordr
# from . import invoices as inv
# from . import coupons as coup
# from . import transactions as tx
# from . import adjustments as ads
# from . import subscriptions as subs


class BrownPaperTickets(base.Resource):
    """
    """
    def __init__(self, developer_id):
        """
        Create a Brown Paper Tickets service.

        :var developer_id: Your Brown Paper Tcikets developer id.
        :vartype developer_id: str
        """
        self.apiroot = 'https://www.brownpapertickets.com/api2'

        self.developer_id = developer_id
        # REVIEW ME What if we're not using any type of auth?
        # Just POST?
        # self.add_filter(auth.BasicAuth(developer_id, ''))
        self.add_filter(self.add_developer_id)

    def get_url(self):
        return self.apiroot

    def add_developer_id(self, request):
        request.params.update({'id': self.developer_id})
    # def use_xml(self, request):
    #     request.headers['Content-Type'] = 'application/xml'
    #     request.headers.setdefault('Accept', 'application/xml')

    #     if request.method.upper() not in http.URLENCODE_METHODS:
    #         request.params = xml.dict_to_xml(request.params)

    @base.resource(ev.Events)
    def events(self):
        """
        Return the resource corresponding to all events.
        """
        return ev.Events(self)

    @base.resource(ev.Event)
    def event(self, event_id):
        """
        Return the resource corresponding to a single plan.
        """
        return ev.Event(self, event_id)

    @base.resource(ordr.Orders)
    def orders(self, account, event_id):
        """
        Return the resource corresponding to all orders for an event.
        """
        return ordr.Orders(self, account=account, event_id=event_id)

    # @base.resource(acc.Account)
    # def account(self, account_code):
    #     """
    #     Return the resource corresponding to a single account.
    #     """
    #     return acc.Account(self, account_code)

    # @base.resource(ads.Adjustment)
    # def adjustment(self, uuid):
    #     """
    #     Return the resource corresponding to a single adjustment.
    #     """
    #     return ads.Adjustment(self, uuid)

    # @base.resource(coup.Coupons)
    # def coupons(self):
    #     """
    #     Return the resource corresponding to all coupons.
    #     """
    #     return coup.Coupons(self)

    # @base.resource(coup.Coupon)
    # def coupon(self, coupon_code):
    #     """
    #     Return the resource corresponding to a single coupon.
    #     """
    #     return coup.Coupon(self, coupon_code)

    # @base.resource(inv.Invoices)
    # def invoices(self):
    #     """
    #     Return the resource corresponding to all invoices.
    #     """
    #     return inv.Invoices(self)

    # @base.resource(inv.Invoice)
    # def invoice(self, invoice_number):
    #     """
    #     Return the resource corresponding to a single invoice.
    #     """
    #     return inv.Invoice(self, invoice_number)

    # @base.resource(subs.Subscriptions)
    # def subscriptions(self):
    #     """
    #     Return the resource corresponding to all subscriptions.
    #     """
    #     return subs.Subscriptions(self)

    # @base.resource(subs.Subscription)
    # def subscription(self, uuid):
    #     """
    #     Return the resource corresponding to a single subscription.
    #     """
    #     return subs.Subscription(self, uuid)

    # @base.resource(tx.Transactions)
    # def transactions(self):
    #     """
    #     Return the resource corresponding to all transactions.
    #     """
    #     return tx.Transactions(self)

    # @base.resource(tx.Transaction)
    # def transaction(self, uuid):
    #     """
    #     Return the resource corresponding to a single transaction.
    #     """
    #     return tx.Transaction(self, uuid)
