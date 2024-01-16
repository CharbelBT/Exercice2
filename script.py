import os
import yaml


with open('.github/workflows/manual.yml', 'r') as file:
    config = yaml.safe_load(file)

env_var1 = config['env']['a']
env_var2 = config['env']['b']

os.environ['ENV_VAR1'] = env_var1
os.environ['ENV_VAR2'] = env_var2

print("La multiplication de a et b est : ", os.environ['ENV_VAR1']*os.environ['ENV_VAR2'])
