---
description:  
---
# Exchange rate

>  **Package : spaceone.api.cost_analysis.v1**

## ExchangeRate

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
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


| Type | Message |
| :--- | :--- |
| Request | [SetExchangeRateRequest](exchange-rate.md#setexchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### reset
> **POST** /cost-analysis/v1/exchange-rate/{currency}/reset
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### enable
> **POST** /cost-analysis/v1/exchange-rate/{currency}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### disable
> **POST** /cost-analysis/v1/exchange-rate/{currency}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### get
> **GET** /cost-analysis/v1/exchange-rate/{currency}
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/exchange-rates
>
> **POST** /cost-analysis/v1/exchange-rates/search



| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateQuery](exchange-rate.md#exchangeratequery) |
| Response |  [ExchangeRatesInfo](exchange-rate.md#exchangeratesinfo)  |


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
