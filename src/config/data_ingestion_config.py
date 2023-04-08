import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    data_source_path: str=os.path.join('data/interim',"student_data.csv")
    train_data_path: str=os.path.join('data/interim',"train.csv")
    test_data_path: str=os.path.join('data/interim',"test.csv")
    raw_data_path: str=os.path.join('data/interim',"data.csv")