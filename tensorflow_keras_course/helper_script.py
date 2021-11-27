"""
This is a helper script, all the functions that we
write in here are used to declutter other scripts.
"""


def convert_loan_status_into_numeric(loan_status: str) -> int:
    """
    Transforms a string for the status of the loan into an
    integer that we can use for model training and model
    evalution.

    Example
    ------
    ```
    loan_status = "Fully Paid"
    hs.convert_loan_status_into_numeric(loan_status)
    # return 0
    
    loan_status = "Charged Off"
    convert_loan_status_into_numeric(loan_status)
    # return 1
    ```
    """
    loan_status = loan_status.lower()
    output = None
    if loan_status in  ["fully paid"]:
        output = 0
    elif loan_status in  ["charged off"]:
        output = 1
    return output













