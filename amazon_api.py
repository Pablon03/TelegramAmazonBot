from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.models.search_items_request import SearchItemsRequest
from paapi5_python_sdk.models.search_items_resource import SearchItemsResource
from paapi5_python_sdk.rest import ApiException
from response_parser import parse_response
from consts import *

# function that search amazon products
def search_items(keywords, search_index="All", item_page=1):
    default_api = DefaultApi(
        access_key=AMAZON_ACCESS_KEY,
        secret_key=AMAZON_SECRET_KEY,
        host=AMAZON_HOST,
        region=AMAZON_REGION,
    )

    """ Especifica la categoria en la que buscar para hacer la consulta """
    """ Para más detalles, Link: https://webservices.amazon.com/paapi5/documentation/use-cases/organization-of-items-on-amazon/search-index.html """

    """ Especifica la cantidad de productos que serán recogidos en cada búsqueda """
    item_count = 20

    """ Elige los recursos que tu quieres de SearchItemsResouce enum """
    """ Para más detalles, Link: https://webservices.amazon.com/paapi5/documentation/search-items.html#resources-parameter """
    search_items_resource = [
        SearchItemsResource.ITEMINFO_TITLE,
        SearchItemsResource.OFFERS_LISTINGS_PRICE,
        SearchItemsResource.IMAGES_PRIMARY_LARGE,
        SearchItemsResource.OFFERS_LISTINGS_SAVINGBASIS,
        SearchItemsResource.ITEMINFO_FEATURES,
        SearchItemsResource.OFFERS_LISTINGS_PROMOTIONS,
        SearchItemsResource.OFFERS_LISTINGS_CONDITION,
        SearchItemsResource.OFFERS_LISTINGS_ISBUYBOXWINNER,
    ]

    """ Formando la consulta """
    try:
        search_items_request = SearchItemsRequest(
            partner_tag=PARTNER_TAG,
            partner_type=PartnerType.ASSOCIATES,
            keywords=keywords,
            search_index=search_index,
            item_count=item_count,
            resources=search_items_resource,
            item_page=item_page,
        )
    except ValueError as exception:
        print("Error formando SearchItemsRequest: ", exception)
        return

    try:
        """Haciendo request"""
        response = default_api.search_items(search_items_request)
        print("Request recibida")
        res = parse_response(response)

        if response.errors is not None:
            print("\nEscribiendo errores:\Escribiendo el primer error de la lista de errores")
            print("Error code", response.errors[0].code)
            print("Error message", response.errors[0].message)
        return res

    except ApiException as exception:
        print("Error calling PA-API 5.0!")
        print("Status code:", exception.status)
        print("Errors :", exception.body)
        print("Request ID:", exception.headers["x-amzn-RequestId"])

    except TypeError as exception:
        print("TypeError :", exception)

    except ValueError as exception:
        print("ValueError :", exception)

    except Exception as exception:
        print("Exception :", exception)
