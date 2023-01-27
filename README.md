# PaymentGatewayIntegration

# for documentation after runing project on local visit http://localhost:8000/docs

* admin info for login for creating product route -> login/admin
```
{
email: nitinuniyal21@gmail.com 
password: 9410197255
}
```
* creating product admin  route authentication req-> /create_product
{
  "name": "string",
  "amount": 0,
  "discription": "string"
}```

```
* user account login route -> login/user
```
{
  "email": "email",
  "password": "string"
}
```
* signup for user route -> /signup
```
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```
* order product for user route -> /order_product   authentication req
```
{
  "product_id": 0,
  "purpose": "string"
}
```
* list all product ordered by user route -> /all_user_ordered_product

* list all product available /list_all_product

# testing payment gateway integration 
* route /test/payment_gateway
```
{
  "amount": 100,
  "purpose": "string",
  "buyer_name": "string",
  "send_email": true,
  "email": "ashutoshuniyal21@gmail.com"
}
```


* for checking payment status
* route /orderstatus -> required query parameter order_id returned by /test/payment_gateway


