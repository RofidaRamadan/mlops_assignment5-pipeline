import mlflow
import random

mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    accuracy = 0.90   

    mlflow.log_metric("accuracy", accuracy)

    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)

    with open("accuracy.txt", "w") as f:
        f.write(str(accuracy))

    print("Accuracy:", accuracy)