# mocking the api results

def get_client_details(id):
    """
    a mock function/response of the get_client_detail endpoint from nanos api
    :param id: client's id
    :return: client's detail
    """
    return {
        'name': 'John Doe',
        'country': 'switzerland',
        'vat_number': '12443',
        'stripe_customer_id': 'st_23dav_dasera'
    }


def list_all_campaigns():
    """
    a mock function/response of the list_all_campaigns endpoint from nanos api
    :return: list of campaigns ints
    """
    return [1, 100, 125, 126, 127]


def get_campaign_details(id):
    """
    a mock function/response of the get_campaign_details endpoint from nanos api
    :param id:
    :return: a campaign details
    """
    return {
        'name': 'Campai'
    }


def render_tax_invoice(client_name, email, address, campaign_name, invoice_currency, invoice_amount,
                       vat_amount, net_amount):
    """
    a mock function/response of the render_tax_invoice endpoint from nanos api
    :param client_name:
    :param email:
    :param address:
    :param campaign_name:
    :param invoice_currency:
    :param invoice_amount:
    :param vat_amount:
    :param net_amount:
    :return: a generated tax invoice
    """
    return
