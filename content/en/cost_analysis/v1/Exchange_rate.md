---
title: "Exchange_rate"
linkTitle: "Exchange_rate"
weight: 3
bookFlatSection: true
---
# [Exchange_rate](#Exchange_rate)
desc: An ExchangeRate is a resource defining the exchange rate of currencies. This resource can set a custom exchange rate for a specific domain, separately from the exchange rate of the default domain set in `config`.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Exchange_rate


**ExchangeRate Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**set**](./ExchangeRate#set) | [SetExchangeRateRequest](ExchangeRate#setexchangeraterequest) | [ExchangeRateInfo](./ExchangeRate#exchangerateinfo) |
| [**reset**](./ExchangeRate#reset) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](./ExchangeRate#exchangerateinfo) |
| [**enable**](./ExchangeRate#enable) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](./ExchangeRate#exchangerateinfo) |
| [**disable**](./ExchangeRate#disable) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](./ExchangeRate#exchangerateinfo) |
| [**get**](./ExchangeRate#get) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](./ExchangeRate#exchangerateinfo) |
| [**list**](./ExchangeRate#list) | [ExchangeRateQuery](ExchangeRate#exchangeratequery) | [ExchangeRatesInfo](./ExchangeRate#exchangeratesinfo) |



    
<br>

### set

> **POST** /cost-analysis/v1/exchange-rate/set
>




 {{< tabs " set " >}}




{{< /tabs >}}

    
<br>

### reset

> **POST** /cost-analysis/v1/exchange-rate/reset
>




 {{< tabs " reset " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /cost-analysis/v1/exchange-rate/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /cost-analysis/v1/exchange-rate/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/exchange-rate/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/exchange-rate/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ExchangeRateInfo
* **currency** (string)  `Required` 

    
* **rate** (float)  `Required` 

    
* **state** (State)  `Required` 

    
* **is_default** (bool)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### ExchangeRateQuery
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ExchangeRateRequest
* **currency** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ExchangeRatesInfo
* **results** (ExchangeRateInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### SetExchangeRateRequest
* **currency** (string)  `Required` 

  *is_required: true*

    
* **rate** (float)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
