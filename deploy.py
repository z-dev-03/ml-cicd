import os,shutil,pickle,sys,numpy as np

print("DEPLOY")

os.makedirs("deploy/blue",exist_ok=True)
os.makedirs("deploy/green",exist_ok=True)
os.makedirs("deploy/prod",exist_ok=True)

f="deploy/prod/env.txt"
c="blue"if not os.path.exists(f)else open(f).read().strip()
n="green"if c=="blue"else"blue"

print(f"{c}→{n}")
shutil.copy("model.pkl",f"deploy/{n}/model.pkl")

m=pickle.load(open(f"deploy/{n}/model.pkl","rb"))
if abs(m.predict([[4]])[0]-8)>0.1:sys.exit(1)

shutil.copy(f"deploy/{n}/model.pkl","deploy/prod/model.pkl")
open(f,"w").write(n)
print(f"LIVE:{n}")
