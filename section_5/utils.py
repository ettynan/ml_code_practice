import pandas as pd

def feature_engineering(raw_data: pd.DataFrame) -> pd.DataFrame:

    preprocessed_data = raw_data.copy(deep=True)

    preprocessed_data.columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact',
                               'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'class']

    # client data preprocessing
    preprocessed_data['has_default'] = preprocessed_data.default.apply(
        lambda x : 0 if x == 'no' else 1 if x == 'yes' else -1
    )

    preprocessed_data['has_housing_loan'] = preprocessed_data.housing.apply(
        lambda x : 0 if x == 'no' else 1 if x == 'yes' else -1
    )

    preprocessed_data['has_personal_loan'] = preprocessed_data.loan.apply(
        lambda x : 0 if x == 'no' else 1 if x == 'yes' else -1
    )

    marital_dummies = pd.get_dummies(preprocessed_data.marital, prefix = 'marital')
    preprocessed_data = pd.concat([preprocessed_data, marital_dummies], axis = 1)

    job_dummies = pd.get_dummies(preprocessed_data.job, prefix = 'job')
    preprocessed_data = pd.concat([preprocessed_data, job_dummies], axis = 1)

    edu_dummies = pd.get_dummies(preprocessed_data.education, prefix = 'edu')
    preprocessed_data = pd.concat([preprocessed_data, edu_dummies], axis = 1)

    preprocessed_data.drop(columns= ['default', 'housing', 'loan', 'marital', 'job', 'education'], inplace=True)

    # last contact data preprocessing
    contact_dummies = pd.get_dummies(preprocessed_data.contact, prefix = 'contact_type')
    preprocessed_data = pd.concat([preprocessed_data, contact_dummies], axis = 1)

    month_dummies = pd.get_dummies(preprocessed_data.month, prefix = 'month')
    preprocessed_data = pd.concat([preprocessed_data, month_dummies], axis = 1)

    preprocessed_data.drop(columns= ['contact', 'month'], inplace=True)

    # other attributes preprocessing
    poutcome_dummies = pd.get_dummies(preprocessed_data.poutcome, prefix = 'prev_camp_outcome')
    preprocessed_data = pd.concat([preprocessed_data, poutcome_dummies], axis = 1)

    preprocessed_data.drop(columns= ['poutcome'], inplace=True)

    # target preprocessing
    preprocessed_data['target'] = preprocessed_data['class'].apply(lambda x : 0 if x == '1' else 1)
    preprocessed_data.drop(columns = ['class'], inplace=True)

    return preprocessed_data