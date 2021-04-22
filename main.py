from nanos_api import get_campaign_details, get_client_details, render_tax_invoice
from stripe_setup import stripe


def exempt_value(customer_country):
    # assuming customer_country can be either switzerland or any other country
    if customer_country == "switzerland":
        return "none"
    return "exempt"


def update_stripe_vat(id):
    """
    :param id: nanos id from nanos api/database
    :return:
    """
    client_details = get_client_details(id)
    stripe.Customer.modify(
        client_details['stripe_customer_id'],
        metadata={"tax_exempt": exempt_value(client_details['country'])}
    )


def tax_invoice(campaign_id):
    """
    :param campaign_id: campaign id provided to generate tax invoice
    :return:
    """
    campaign = get_campaign_details(campaign_id)
    stripe_charge = stripe.Charge.retrieve(campaign['stripe_charge_id'],
                                           expand=['invoice'])
    address_obj = stripe_charge['billing_details']['address']
    address = '{}, {}, {}, {}, {}, {}'.format(address_obj['postal_code'],
                                              address_obj['line1'],
                                              address_obj['line2'],
                                              address_obj['city'],
                                              address_obj['state'],
                                              address_obj['country'])
    invoice_amount = stripe_charge['invoice']['amount_paid']
    vat_amount = 0.077 * invoice_amount
    render_tax_invoice(
        client_name=stripe_charge['billing_details']['name'],
        email=stripe_charge['billing_details']['email'],
        address=address,
        campaign_name=campaign['campaign_name'],
        invoice_currency=stripe_charge['invoice']['currency'],
        invoice_amount=invoice_amount,
        vat_amount=vat_amount,
        net_amount=invoice_amount - vat_amount
    )


if __name__ == '__main__':
    update_stripe_vat(21)
    tax_invoice(12)
