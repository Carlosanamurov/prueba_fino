from fastapi.testclient import TestClient
from main import app  # Asegúrate de que esto apunte correctamente a tu archivo con la app de FastAPI

client = TestClient(app)

def test_sincronizar_endpoint():
    response = client.post("/sincronizar")
    print("STATUS CODE:", response.status_code)
    print("RESPONSE JSON:", response.json())

    assert response.status_code == 200
    assert "resultado" in response.json()
if __name__ == "__main__":
    test_sincronizar_endpoint()