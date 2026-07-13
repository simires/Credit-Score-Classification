from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt


def metricas(y_test, predicoes):
    resultados = {
        "Accuracy": accuracy_score(y_test, predicoes),
        "Precision (weighted)": precision_score(
            y_test,
            predicoes,
            average="weighted"
        ),
        "Recall (weighted)": recall_score(
            y_test,
            predicoes,
            average="weighted"
        ),
        "F1-score (weighted)": f1_score(
            y_test,
            predicoes,
            average="weighted"
        ),
        "F1-score (macro)": f1_score(
            y_test,
            predicoes,
            average="macro"
        )
    }
    
    for metrica, valor in resultados.items():
        print(f"{metrica}: {valor:.4f}")


def matriz_confusao(modelo_rf, y_test, predicoes):
    cm = confusion_matrix(y_test, predicoes)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=modelo_rf.classes_
    )
    
    disp.plot(
        values_format="d"
    )
    
    plt.title("Matriz de Confusão - Random Forest")
    plt.show()