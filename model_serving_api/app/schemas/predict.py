from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validation import CreditCardDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    #predictions: Optional[List[float]]
    predictions: int


class MultipleCreditCardDataInputs(BaseModel):
    inputs: List[CreditCardDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "CLIENTNUM": 768805383,
                        "Customer_Age": 31,
                        "Dependent_count": 1,
                        "Months_on_book": 18,
                        "Total_Relationship_Count": 3,
                        "Months_Inactive_12_mon": 1,
                        "Contacts_Count_12_mon": 3,
                        "Credit_Limit": 3399.0,
                        "Total_Revolving_Bal": 1800,
                        "Avg_Open_To_Buy": 1599.0,
                        "Total_Amt_Chng_Q4_Q1": 0.752,
                        "Total_Trans_Amt": 13148,
                        "Total_Trans_Ct": 121,
                        "Total_Ct_Chng_Q4_Q1": 0.806,
                        "Avg_Utilization_Ratio": 0.530,
                        "Gender": "F",
                        "Education_Level": "High School",
                        "Marital_Status": "Single",
                        "Income_Category": "Less than $40K",
                        "Card_Category": "Blue",
                        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1": 0.000093,
                        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2": 0.99994,
                    }
                ]
            }
        }