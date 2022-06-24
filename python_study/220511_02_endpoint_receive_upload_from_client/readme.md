
First start the server:
```
python app.py
```

Then in another terminal we can run the client01.py script, which simulates the client making requests.
```
python client01.py 
```

The expected answer would be:

```
Upload completed successfully!
+-----------------------------------------------------------+
URL: http://localhost:5000/
Status Code: 200


HTTP Response Header:
Server:
        Werkzeug/2.1.2 Python/3.9.12
Date:
        Wed, 11 May 2022 20:47:11 GMT
Content-Type:
        application/octet-stream
Content-Length:
        336
Connection:
        close


HTTP Response Body:
--725f9fa102d0df7ede5ce86a9ec00c9b
Content-Disposition: form-data; name="form_field_name"; filename="file01.json"

{
    "message": "this is an important message to be sent",
    "obs": "this comes from another endpoitn",
    "array": ["and it will be tested for another project", "end"]
}
--725f9fa102d0df7ede5ce86a9ec00c9b--


+-----------------------------------------------------------+
```