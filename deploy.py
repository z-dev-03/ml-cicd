import os, shutil, pickle, sys, numpy as np
print("=== DEPLOY START ===")

# Create ALL folders
folders = ["deploy/blue", "deploy/green", "deploy/prod"]
for f in folders: os.makedirs(f, exist_ok=True)

# Blue-Green LOGIC
env_file = "deploy/prod/env.txt"
current_env = "blue" if not os.path.exists(env_file) else open(env_file).read().strip()
new_env = "green" if current_env == "blue" else "blue"

print(f"SWITCH: {current_env} to {new_env}")

# STEP 1: Deploy to new environment
shutil.copy("model.pkl", f"deploy/{new_env}/model.pkl")
print(f"Deployed {new_env}")

# STEP 2: Test it works
model = pickle.load(open(f"deploy/{new_env}/model.pkl", "rb"))
test_result = model.predict(np.array([[4]]))[0]
print(f"Test result: {test_result}")

if abs(test_result - 8.0) > 0.1:
    print("TEST FAILED")
    sys.exit(1)

# STEP 3: Switch production
shutil.copy(f"deploy/{new_env}/model.pkl", "deploy/prod/model.pkl")
open(env_file, "w").write(new_env)
print(f"PRODUCTION NOW: {new_env}")
print("=== DEPLOY DONE ===")
