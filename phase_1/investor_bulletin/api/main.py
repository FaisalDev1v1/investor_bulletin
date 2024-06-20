from fastapi import FastAPI
from api.routes import router


print("PYTHONPATH:", sys.path)
print("Current working directory:", os.getcwd())


app = FastAPI()

app.include_router(router)

