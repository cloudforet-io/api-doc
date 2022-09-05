---
description: An ExchangeRate is a resource defining the exchange rate of currencies. This resource can set a custom exchange rate for a specific domain, separately from the exchange rate of the default domain set in `config`.
---
# Exchange rate

>  **Package : spaceone.api.cost_analysis.v1**

## ExchangeRate

{% hint style="info" %}
**ExchangeRate Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**set**](exchange-rate.md#set)|   [SetExchangeRateRequest](exchange-rate.md#setexchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |
| [**reset**](exchange-rate.md#reset)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |
| [**enable**](exchange-rate.md#enable)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |
| [**disable**](exchange-rate.md#disable)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |
| [**get**](exchange-rate.md#get)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |
| [**list**](exchange-rate.md#list)|   [ExchangeRateQuery](exchange-rate.md#exchangeratequery) |   [ExchangeRatesInfo](exchange-rate.md#exchangeratesinfo) | 
 

 
### set
> **POST** /cost-analysis/v1/exchange-rate/{currency}/set
>

> Overrides a value of a specific ExchangeRate. This method is used to change the ExchangeRate in a specific domain. You can set the `currency` and `rate` of the resource.

| Type | Message |
| :--- | :--- |
| Request | [SetExchangeRateRequest](exchange-rate.md#setexchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "currency": "KRW",
    "rate": 1300
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "currency": "KRW",
    "rate": 1300.0,
    "state": "ENABLED",
    "is_default": true
}
```
{% endtab %}
{% endtabs %}
 
 

 
### reset
> **POST** /cost-analysis/v1/exchange-rate/{currency}/reset
>

> Resets a value of a specific ExchangeRate and changes the ExchangeRate to the ExchangeRate of the `default` domain.

| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "currency": "KRW"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "currency": "KRW",
    "rate": 1242.7,
    "state": "ENABLED",
    "is_default": true,
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **POST** /cost-analysis/v1/exchange-rate/{currency}/enable
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **POST** /cost-analysis/v1/exchange-rate/{currency}/disable
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/exchange-rate/{currency}
>

> Gets a specific ExchangeRate. Prints detailed information about the ExchangeRate, including  `currency` and `rate`.

| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "currency": "KRW"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "currency": "KRW",
    "rate": 1242.7,
    "state": "ENABLED",
    "is_default": true,
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/exchange-rates
>
> **POST** /cost-analysis/v1/exchange-rates/search


> Gets a list of all ExchangeRates. You can use a query to get a filtered list of ExchangeRates.

| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateQuery](exchange-rate.md#exchangeratequery) |
| Response |  [ExchangeRatesInfo](exchange-rate.md#exchangeratesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "currency": "JPY",
            "rate": 129.8,
            "state": "ENABLED",
            "is_default": true,
            "domain_id": "domain-58010aa2e451"
        },
        {
            "currency": "KRW",
            "rate": 1242.7,
            "state": "ENABLED",
            "is_default": true,
            "domain_id": "domain-58010aa2e451"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}


## 

## Message

### ExchangeRateInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">currency</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">rate</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_default</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ExchangeRateQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |

### ExchangeRateRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| currency |string|✔| |
| domain_id |string|✔| |

### ExchangeRatesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ExchangeRateInfo](exchange-rate.md#exchangerateinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SetExchangeRateRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| currency |string|✔| |
| rate |float|✔| |
| domain_id |string|✔| |
