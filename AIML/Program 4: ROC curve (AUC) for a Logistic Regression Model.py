from sklearn.metrics import roc_auc_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0.2, 0.8, 0.6, 0.3, 0.9]

def calculate_auc(y_true, y_pred):
    auc = roc_auc_score(y_true, y_pred)
    return auc

auc_score = calculate_auc(y_true, y_pred)

print("Area Under the ROC Curve (AUC): {:.2f}".format(auc_score))
