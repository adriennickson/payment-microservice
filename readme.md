# Payments Management Microservice
&copy;[DIEHLI](https://diehli.com/)

Microservice for invoice and payment management.

## Services so integrate

### Stripe
Ongoing

### PayPal
Todo

### WeCasHup
Todo

## Run test:
```shell
pip3 install -r requirements.txt -r requirements-dev.txt
./manage.py test --settings diehli_finance.settings.test
```

## Run app:
```shell
cp .env.example .env
```
Edit file with the right keys

```shell
docker compose up -d
```
And go to [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
