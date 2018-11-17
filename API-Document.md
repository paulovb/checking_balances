**Create an Account**
----
* **URL**

  api/v1/accounts/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 
* **Data Params**

  ```
  {
    "name": "Gabriela Lima",
    "email": "gabriela.lima@mail.com"
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{ id : 1 }`
 
* **Error Response:**

  None

**Deposit Money in an Account**
----
* **URL**

  api/v1/deposit/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 
* **Data Params**

  ```
  {
    "account_id": 1,
    "notes": "Any note",
    "value": 1000.000
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** 
    `{
        "account_id": 1, 
        "account_name": "Gabriela Lima", 
        "account_email": "gabriela.lima@mail.com", 
        "account_balance": 1000.0, 
        "transactions": [
          {"transaction_id": 1, "operation": "deposit", "date": "2018-11-17 03:34:27.639778+00:00", "value": 1000.0, "last_balance": 0.0, "notes": "Any note"}
        ]
    }`
 
* **Error Response:**

  None


**Deposit Money in an Account**
----
* **URL**

  api/v1/withdraw/

* **Method:**

  `POST`
  
*  **URL Params**

   None
 
* **Data Params**

  ```
  {
    "account_id": 1,
    "notes": "Any note",
    "value": 500.000
  }
  ```

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** 
    `{
        "account_id": 1, 
        "account_name": "Gabriela Lima", 
        "account_email": "gabriela.lima@mail.com", 
        "account_balance": 500.0, 
        "transactions": [
          {"transaction_id": 1, "operation": "deposit", "date": "2018-11-17 03:34:27.639778+00:00", "value": 1000.0, "last_balance": 0.0, "notes": "Any note"},
          {"transaction_id": 2, "withdraw": "deposit", "date": "2018-11-17 03:36:55.546724+00:00", "value": 500.0, "last_balance": 1000.0, "notes": "Any note"}
        ]
    }`
 
* **Error Response:**

  When the money doesn't enough
  
  * **Code:** 203 <br />