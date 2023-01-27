# PaymentGatewayIntegration

# for documentation after runing project on local visit http://localhost:8000/docs

* testing payment gateway integration 
* route /test/payment_gateway
```{
  "amount": 100,
  "purpose": "string",
  "buyer_name": "string",
  "send_email": true,
  "email": "ashutoshuniyal21@gmail.com"
}```


* for checking payment status
* route /orderstatus -> required query parameter order_id returned by /test/payment_gateway
