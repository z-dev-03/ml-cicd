import os, shutil, pickle, sys, numpy as np

print("=== Deployment Started ===")

# Create folders
os.makedirs("deploy/blue", exist_ok=True)
os.makedirs("deploy/green", exist_ok=True)
os.makedirs("deploy/prod", exist_ok=True)

# Check current production environment
env_file = "deploy/prod/env.txt"
if os.path.exists(env_file):
    current = open(env_file).read().strip()
else:
    current = "green"

# Toggle environment
target = "blue" if current == "green" else "green"
target_folder = f"deploy/{target}"

print(f"Deploying to {target}")

# Copy model to target environment
shutil.copy("model.pkl", f"{target_folder}/model.pkl")

# Test model (health check)
model = pickle.load(open(f"{target_folder}/model.pkl", "rb"))
pred = model.predict(np.array([[4]]))[0]
print(f"Health check: {pred:.1f}")

if abs(pred - 8.0) > 0.1:
    print("Health check FAILED")
    sys.exit(1)

# Switch production to new environment
shutil.copy(f"{target_folder}/model.pkl", "deploy/prod/model.pkl")
open(env_file, "w").write(target)

print(f"Production switched to {target}")
print("=== Deployment Complete ===")
