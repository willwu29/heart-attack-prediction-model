import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, \
    accuracy_score, f1_score, precision_score, recall_score,  roc_auc_score



class ModelEvaluator:
    def __init__(self, model, is_neural_network=False):
        self.model= model
        self.is_neural_network = is_neural_network
        self.y_pred_proba_train = None
        self.y_pred_proba_test = None
        self.y_pred_train = None
        self.y_pred_test = None

    @staticmethod
    def false_positive_rate(y_test, y_pred):
        """"
        Calcualte the False Positive Rate
        fpr = fp / (fp + tn) where fp stands for false positives, and tn stands for true negatives

        Args:
            y_test(np.ndarray or pd.Series): True labels
            y_pred(np.ndarray or pd.Series): Predicted labels

        Returns:
            float: False positive rate
        """
        fp = ((y_test == 0) & (y_pred == 1)).sum()
        tn = ((y_test == 0) & (y_pred == 0)).sum()

        if (fp + tn) == 0:
            return 0
        else:
            return fp / (fp + tn)


    def evaluate(self, X_train, X_test, y_train, y_test, thresholds=0.5):
        """
        Prints model evaluation metrics for both training and test datasets.
        This function computes the predictions, and displays various classification metrics, including:
        confusion matrix, classification report, recall, false positive rate, accuracy, precision,
        F1, and AUC. It visualizes theconfusion matrix for the test data as well.

        Args:
            X_train (array): Feature set for the training data.
            X_test (array): Feature set for the test data.
            y_train (array): True labels for the training data.
            y_test (array): True labels for the test data.
            model (machine learning model): The trained model to evaluate.
            is_neural_network (bool): If True, use a different prediction method suitable for neural networks.

        Returns:
            This function does not return anything, it just display the confusion matrix, confusion table and all other metrics
        """
        # Generate predictions
        if self.is_neural_network:
            self.y_pred_proba_train = self.model.predict(X_train)
            self.y_pred_proba_test = self.model.predict(X_test)
        else:
            self.y_pred_proba_train = self.model.predict_proba(X_train)[:, 1]
            self.y_pred_proba_test = self.model.predict_proba(X_test)[:, 1]

        # Hard predictions
        self.y_pred_train = np.where(self.y_pred_proba_train > thresholds, 1, 0).flatten()
        self.y_pred_test = np.where(self.y_pred_proba_test > thresholds, 1, 0).flatten()

        # Print evaluation metrics
        print_line = "\n" + "===========" * 6

        # Confusion Matrix for Test Data
        print('Confusion matrices:', print_line)
        plt.figure(figsize=(3, 3))
        conf_matrix = confusion_matrix(y_test, self.y_pred_test)
        ConfusionMatrixDisplay(confusion_matrix=conf_matrix).plot()
        plt.title('Confusion Matrix\nTest Data')
        plt.grid(False)
        plt.show()

        # Classification Report
        report_test = classification_report(y_test, self.y_pred_test)
        print('Test Data Classification Report:', print_line, report_test)

        # Recall Scores
        print('Recall Score:')
        print(f'Train: {recall_score(y_train, self.y_pred_train):.3f}')
        print(f'Test: {recall_score(y_test, self.y_pred_test):.3f}', print_line)

        # False Positive Rate
        print('False Positive Rate:')
        print(f'Train: {self.false_positive_rate(y_train, self.y_pred_train):.3f}')
        print(f'Test: {self.false_positive_rate(y_test, self.y_pred_test):.3f}', print_line)

        # AUC Score
        print('AUC Score:')
        print(f'Train: {roc_auc_score(y_train, self.y_pred_proba_train):.3f}')
        print(f'Test: {roc_auc_score(y_test, self.y_pred_proba_test):.3f}', print_line)

        # Accuracy
        print('Accuracy Score:')
        print(f'Train: {accuracy_score(y_train, self.y_pred_train):.3f}')
        print(f'Test: {accuracy_score(y_test, self.y_pred_test):.3f}', print_line)

        # Precision
        print('Precision Score:')
        print(f'Train: {precision_score(y_train, self.y_pred_train):.3f}')
        print(f'Test: {precision_score(y_test, self.y_pred_test):.3f}', print_line)

        # F1 Score
        print('F1 Score:')
        print(f'Train: {f1_score(y_train, self.y_pred_train):.3f}')
        print(f'Test: {f1_score(y_test, self.y_pred_test):.3f}', print_line)






    def plot_roc_auc_curve(self, X_train, X_test, y_train, y_test):
        """
        Plot the ROC curve and calculate the AUC for the training and test datasets.

        Args:
            X_train (array-like): Feature set for the training data.
            X_test (array-like): Feature set for the test data.
            y_train (array-like): True labels for the training data.
            y_test (array-like): True labels for the test data.

        Returns:
            None: Displays the ROC curve plot.
        """

        # Generate predictions
        if self.is_neural_network:
            self.y_pred_proba_train = self.model.predict(X_train)
            self.y_pred_proba_test = self.model.predict(X_test)
        else:
            self.y_pred_proba_train = self.model.predict_proba(X_train)[:, 1]
            self.y_pred_proba_test = self.model.predict_proba(X_test)[:, 1]

        # Create a range of thresholds
        thresholds = np.linspace(0, 1, num=51)

        # Create tpr and fpr lists to store the value of these metrics with corresponding threshold
        tpr_train_list = []
        fpr_train_list = []
        tpr_test_list = []
        fpr_test_list = []

        for threshold in thresholds:
            # Make hard predictions
            y_pred_train = np.where(self.y_pred_proba_train > threshold, 1, 0).flatten()
            y_pred_test = np.where(self.y_pred_proba_test > threshold, 1, 0).flatten()

            # Calculate tpr and fpr
            tpr_train = recall_score(y_train, y_pred_train)
            fpr_train = self.false_positive_rate(y_train, y_pred_train)
            tpr_test = recall_score(y_test, y_pred_test)
            fpr_test = self.false_positive_rate(y_test, y_pred_test)

            # Append tpr and fpr to the list
            tpr_train_list.append(tpr_train)
            fpr_train_list.append(fpr_train)
            tpr_test_list.append(tpr_test)
            fpr_test_list.append(fpr_test)

        # Get (AUC)
        auc_train = np.round(roc_auc_score(y_train, self.y_pred_proba_train), 3)
        auc_test = np.round(roc_auc_score(y_test, self.y_pred_proba_test), 3)

        # Create Labels
        train_label = f'Train AUC: {auc_train}'
        test_label = f'Test AUC: {auc_test}'

        # Set Seaborn style
        sns.set_style('darkgrid')  # Set the style to darkgrid

        # Plot the ROC curve
        plt.figure(figsize=(10, 6))
        plt.plot(fpr_train_list, tpr_train_list, marker='.', label=train_label, c='#0066CC')  # Train ROC Curve
        plt.plot(fpr_test_list, tpr_test_list, marker='.', label=test_label, c='#FF8000')      # Test ROC Curve
        plt.plot([0, 1], [0, 1], lw=2, linestyle="--", c='#9933FF')  # Diagonal line for uninformative classifier
        plt.title('ROC Curve and AUC Score')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate / Recall')
        plt.legend()
        plt.show()

    
    def make_predictions(self, X_train, X_test, thresholds=0.5):
        """
        Generates predictions for training and test datasets based on the thredhold, the default threhold
        is set at 0.5.

        Args:
            X_train (array): Feature set for the training data.
            X_test (array): Feature set for the test data.
            thresholds (float): The threshold for classifying positive predictions.

        Returns:
            tuple: A tuple containing:
                - y_pred_train (array): Predicted labels for the training data.
                - y_pred_test (array): Predicted labels for the test data.
        """
        # Generate probability predictions
        if self.is_neural_network:
            y_pred_proba_train = self.model.predict(X_train)
            y_pred_proba_test = self.model.predict(X_test)
        else:
            y_pred_proba_train = self.model.predict_proba(X_train)[:, 1]
            y_pred_proba_test = self.model.predict_proba(X_test)[:, 1]

        # Hard predictions
        y_pred_train = np.where(y_pred_proba_train > thresholds, 1, 0).flatten()
        y_pred_test = np.where(y_pred_proba_test > thresholds, 1, 0).flatten()

        return y_pred_train, y_pred_test
