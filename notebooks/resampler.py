import pandas as pd
import numpy as np
from sklearn.utils import resample

class UpSampler:
    def __init__(self, random_state=1):      
        self.random_state = random_state  
    
    def fit(self, X, y):
        return self  # Required for pipeline compatibility
    
    def fit_resample(self, X, y):
        # Get majority and minority classes (works for numpy arrays and pandas Series)
        unique_classes, counts = np.unique(y, return_counts=True)
        majority_class = unique_classes[np.argmax(counts)]
        minority_class = unique_classes[np.argmin(counts)]
        
        # Separate majority and minority
        X_major = X[y == majority_class]
        y_major = y[y == majority_class]
        X_minor = X[y == minority_class]
        y_minor = y[y == minority_class]
        
        # Upsample minority class to match majority size
        X_minor_res, y_minor_res = resample(
            X_minor,
            y_minor,
            replace=True,
            n_samples=len(y_major),
            random_state=self.random_state
        )
        
        # Combine (handles both DataFrames and arrays)
        if isinstance(X, pd.DataFrame):
            X_combined = pd.concat([X_major, X_minor_res], axis=0)
        else:
            X_combined = np.vstack([X_major, X_minor_res])

        # Combine y, y is an np.ndarray    
        y_combined = np.concatenate([y_major, y_minor_res])
        
        return X_combined, y_combined


class DownSampler:
    def __init__(self, random_state=1):      
        self.random_state = random_state  
    
    def fit(self, X, y):
        return self  # Required for pipeline compatibility
    
    def fit_resample(self, X, y):
        # Get majority and minority classes
        unique_classes, counts = np.unique(y, return_counts=True)
        majority_class = unique_classes[np.argmax(counts)]
        minority_class = unique_classes[np.argmin(counts)]
        
        # Separate minority
        X_minor = X[y == minority_class]
        y_minor = y[y == minority_class]
        X_major = X[y == majority_class]
        y_major = y[y == majority_class]
        
        # Downsample majority to match minority size
        X_major_res, y_major_res = resample(
            X_major,
            y_major,
            replace=False,
            n_samples=len(y_minor),
            random_state=self.random_state
        )
        
        # Combine (handles both DataFrames and arrays)
        if isinstance(X, pd.DataFrame):
            X_combined = pd.concat([X_minor, X_major_res], axis=0)
        else:
            X_combined = np.vstack([X_minor, X_major_res])

        # Combine y, y is an np.ndarray    
        y_combined = np.concatenate([y_minor, y_major_res])
        
        return X_combined, y_combined