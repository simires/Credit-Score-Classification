from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder


def criar_ordinal_encoder():

    return OrdinalEncoder(
        categories=[
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ],
            [
                "Bad",
                "Standard",
                "Good"
            ]
        ]
    )



def criar_onehot_encoder():

    return OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )