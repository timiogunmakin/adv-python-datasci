import my_module
import pandas as pd

def test_invocation():
    features, target = my_module.get_features_and_target(
        csv_file='../data/adult-census.csv',
        target_col='class'
    )
    
def test_return_types():
    features, target = my_module.get_features_and_target(
        csv_file='../data/adult-census.csv',
        target_col='class'
    )
    assert isinstance(features, pd.DataFrame)
    assert isinstance(target, pd.Series)

def test_cols_make_sense():
    features, target = my_module.get_features_and_target(
        csv_file='../data/adult-census.csv',
        target_col='class'
    )
    # Load the data ourselves so we can double-check the columns
    df = pd.read_csv('../data/adult-census.csv')
    assert target.name in df.columns
    # Use a list comprehension to check all the feature columns
    assert all([feature_col in df.columns for feature_col in features])