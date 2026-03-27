from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler

def create_preprocessor(X, encoding_option, scaling_option):

    num_cols = X.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = X.select_dtypes(include=["object"]).columns

    if scaling_option == "StandardScaler":
        scaler = StandardScaler()
    elif scaling_option == "MinMaxScaler":
        scaler = MinMaxScaler()
    else:
        scaler = "passthrough"

    if encoding_option == "One-Hot Encoding":
        encoder = OneHotEncoder(handle_unknown="ignore")
    else:
        encoder = "passthrough"

    preprocessor = ColumnTransformer([
        ("num", scaler, num_cols),
        ("cat", encoder, cat_cols)
    ])

    return preprocessor