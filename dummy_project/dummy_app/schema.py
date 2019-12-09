from django import forms
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class KNValuesForm(forms.Form):
    kn_value1 = forms.CharField(
        label="kn_value1", max_length=10, required=True)
    kn_value2 = forms.CharField(
        label="kn_value2", max_length=10, required=True)
    kn_value3 = forms.CharField(
        label="kn_value3", max_length=10, required=True)
    kn_value4 = forms.CharField(
        label="kn_value4", max_length=10, required=True)


class KNClassification(Base):
    __tablename__ = 'kn_classification_data'
    id = Column(Integer, primary_key=True)
    prediction = Column(Integer, nullable=False)
    name_in_dataset = Column(String, nullable=False)
    kn_score = Column(Float, nullable=False)


kn_engine = create_engine('sqlite:///KnClassificationDatabase.db')
Base.metadata.create_all(kn_engine)
