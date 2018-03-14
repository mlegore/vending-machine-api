## Instructions

Requires >= python 2.7
No other dependencies
Run with

```
python start.py
```

Endpoint will run at ```http://localhost:8080```

## Endpoints

```
GET /v1/products
```
Returns a products_response

```
GET /v1/products/<id>
```
Returns the product_response entry for product id

```
POST /v1/purchase
```
Post to this endpoint with json body
ensure header ```Content-type: application/json``` is set

## Schemas

product_response
```
{
	name: <Name of product>,
	price: <price in decimal>,
	available: <bool indicating if product is in stock>
	[description: <optional description>]
}
```

products_response
```
{
	products: product_response[],
	currency: <currency the vending machine uses>
}
```

purchase_request
```
{
	'cc_number': <string credit card number>,
	'expiration': <cc expiration date>,
	'security_code': <cc security code>,
	'product_id': <id of product to purchase>,
}
```

purchase_response
```
{
	product: product_response,
	redeem_code: <string redemption code>
}
```
