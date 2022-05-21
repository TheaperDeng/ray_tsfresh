import sys
sys.path.append("..")

import tsfresh
from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, load_robot_execution_failures
from tsfresh import extract_features
from tsfresh import select_features
from tsfresh.utilities.dataframe_functions import impute
from ray_tsfresh import RayDistributor

if __name__ == '__main__':
    distributor = RayDistributor(n_workers=4)
    download_robot_execution_failures()
    timeseries, y = load_robot_execution_failures()
    extracted_features = extract_features(timeseries, column_id="id",
                                          column_sort="time", distributor=distributor)
    impute(extracted_features)
    features_filtered = select_features(extracted_features, y)
    print(type(features_filtered))
