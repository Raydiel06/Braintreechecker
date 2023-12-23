import braintree

def check_and_load_credit_card(api_key: str, card_number: str, expiration_date: str, cvv: str):
    """
    Checks and loads a credit card using the Braintree API.

    This function utilizes the Braintree API to check the validity of a credit card
    and load it into the system for further processing.

    Parameters:
    - api_key (str): The API key for accessing the Braintree API.
    - card_number (str): The credit card number to be checked and loaded.
    - expiration_date (str): The expiration date of the credit card in the format "MM/YY".
    - cvv (str): The CVV (Card Verification Value) of the credit card.

    Returns:
    dict: A dictionary containing the result of the credit card check and load operation.
          The dictionary will have the following keys:
          - 'success': A boolean indicating whether the operation was successful or not.
          - 'message': A string providing additional information about the result.

    Raises:
    - braintree.exceptions.AuthenticationError: If the provided API key is invalid or unauthorized.
    - braintree.exceptions.NotFoundError: If the Braintree API endpoint is not found.
    - braintree.exceptions.ServerError: If there is an error on the Braintree server.
    - braintree.exceptions.UnexpectedError: If an unexpected error occurs during the API request.

    Examples:
    >>> api_key = 'YOUR_API_KEY'
    >>> card_number = '4111111111111111'
    >>> expiration_date = '12/23'
    >>> cvv = '123'
    >>> result = check_and_load_credit_card(api_key, card_number, expiration_date, cvv)
    >>> print(result)
    {'success': True, 'message': 'Credit card successfully checked and loaded.'}
    """

    # Configure the Braintree API with the provided API key
    braintree.Configuration.configure(braintree.Environment.Sandbox, api_key)

    # Create a payment method request with the credit card details
    payment_method_request = {
        "credit_card": {
            "number": card_number,
            "expiration_date": expiration_date,
            "cvv": cvv
        }
    }

    try:
        # Check the credit card using the Braintree API
        result = braintree.PaymentMethod.create(payment_method_request)

        # Check if the credit card check was successful
        if result.is_success:
            return {
                'success': True,
                'message': 'Credit card successfully checked and loaded.'
            }
        else:
            return {
                'success': False,
                'message': 'Credit card check failed. Please check the provided details.'
            }
    except braintree.exceptions.AuthenticationError as e:
        raise braintree.exceptions.AuthenticationError("Invalid or unauthorized API key.")
    except braintree.exceptions.NotFoundError as e:
        raise braintree.exceptions.NotFoundError("Braintree API endpoint not found.")
    except braintree.exceptions.ServerError as e:
        raise braintree.exceptions.ServerError("Error on the Braintree server.")
    except braintree.exceptions.UnexpectedError as e:
        raise braintree.exceptions.UnexpectedError("Unexpected error during API request.")

# Example usage of the check_and_load_credit_card function:

api_key = 'YOUR_API_KEY'
card_number = '4111111111111111'
expiration_date = '12/23'
cvv = '123'

result = check_and_load_credit_card(api_key, card_number, expiration_date, cvv)
print(result)