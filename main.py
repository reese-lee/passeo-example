import newrelic.agent
from passeo import passeo
newrelic.agent.initialize('newrelic.ini')

@newrelic.agent.background_task()
def execute_task(): 
    print("here we go")
    print("generate something")
    print(passeo().generate(length=10, numbers=True, symbols=True, uppercase=True, lowercase=False, space=True, save=True))
    print("Strenth check")
    print(passeo().strengthcheck("Passeo"))

if __name__ == "__main__":
    execute_task()