from abc import ABC, abstractmethod
from typing import Any

class AbstractModel(ABC):

    @abstractmethod
    def model_definition(self):
        """define the mode"""
        pass

    @abstractmethod
    def fit(self, X_train, y_train):
        """fit the model to the given training data."""
        pass

    @abstractmethod
    def predict(self, X_test):
        """use the trained model to predict the given test data. For classification task, this should be the label"""
        pass

    @abstractmethod
    def predict_proba(self, X_test):
        """use the trained model to predict the given test data. For classification task, it needs to be probability pf each label"""
        pass

    @abstractmethod
    def get_params(self) -> Any:
        """retrieve the parameters of the trained model."""
        pass
