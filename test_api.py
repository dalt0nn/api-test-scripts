   #Signup API Automated Tests
   #Valid Signup
response = requests.post("https://api.lendsqr.com/api/signup", json={"email": "test@example.com", "password": "SecurePassword123", "name": "Test User"})
     assert response.status_code == 201
     assert "Signup successful" in response.json()["message"]
     
   #Invalid Signup (missing password)
response = requests.post("https://api.lendsqr.com/api/signup", json={"email": "test@example.com", "name": "Test User"})
     assert response.status_code == 400
     assert "Invalid input" in response.json()["error"]

   #Login API Automated Tests
   #Valid Login
response = requests.post("https://api.lendsqr.com/api/login", json={"email": "test@example.com", "password": "SecurePassword123"})
     assert response.status_code == 200
     assert "token" in response.json()

   #Invalid Login (incorrect password)
response = requests.post("https://api.lendsqr.com/api/login", json={"email": "test@example.com", "password": "WrongPassword"})
     assert response.status_code == 401
     assert "Invalid credentials" in response.json()["error"]

   #Retrieving API Keys Automated Tests**
   #Valid API Key Retrieval
headers = {"Authorization": "Bearer valid_token"}
     response = requests.get("https://api.lendsqr.com/api/user/api-keys", headers=headers)
     assert response.status_code == 200
     assert "apiKey" in response.json()

   #Invalid API Key Retrieval
headers = {"Authorization": "Bearer invalid_token"}
     response = requests.get("https://api.lendsqr.com/api/user/api-keys", headers=headers)
     assert response.status_code == 403
     assert "Access denied" in response.json()["error"]
