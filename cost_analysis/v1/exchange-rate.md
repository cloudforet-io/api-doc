---
description:  
---
# Exchange rate

>  **Package : spaceone.api.cost_analysis.v1**

## ExchangeRate

{% hint style="info" %}
**ExchangeRate Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**set**](exchange-rate.md#set)|   [SetExchangeRateRequest](exchange-rate.md#setexchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |  |
| 2 | [**reset**](exchange-rate.md#reset)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |  |
| 3 | [**get**](exchange-rate.md#get)|   [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |  |
| 4 | [**list**](exchange-rate.md#list)|   [ExchangeRateQuery](exchange-rate.md#exchangeratequery) |   [ExchangeRateInfo](exchange-rate.md#exchangerateinfo) |  | 
 

 
### set
> **POST** /cost-analysis/v2/exchange-rate/{currency}/set
>


| Type | Message |
| :--- | :--- |
| Request | [SetExchangeRateRequest](exchange-rate.md#setexchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### reset
> **POST** /cost-analysis/v2/exchange-rate/{currency}/reset
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### get
> **GET** /cost-analysis/v2/exchange-rate/{currency}
>


| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateRequest](exchange-rate.md#exchangeraterequest) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v2/exchange-rates
>
> **POST** /cost-analysis/v2/exchange-rates/search



| Type | Message |
| :--- | :--- |
| Request | [ExchangeRateQuery](exchange-rate.md#exchangeratequery) |
| Response |  [ExchangeRateInfo](exchange-rate.md#exchangerateinfo)  |


## 

## Message

### ExchangeRateInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | currency |string | |
| 2 | rate |float | |
| 3 | is_default |bool | |
| 4 | domain_id |string | |

### ExchangeRateQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | domain_id |string|✅| |

### ExchangeRateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | currency |string|✅| |
| 2 | domain_id |string|✅| |

### ExchangeRatesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ExchangeRateInfo](exchange-rate.md#exchangerateinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SetExchangeRateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | currency |string|✅| |
| 2 | rate |float|✅| |
| 3 | domain_id |string|✅| |
