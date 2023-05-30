---
title: "ExchangeRate"
linkTitle: "ExchangeRate"
weight: 3
bookFlatSection: true
---
# [ExchangeRate](#ExchangeRate)
An ExchangeRate is a resource defining the exchange rate of currencies. This resource can set a custom exchange rate for a specific domain, separately from the exchange rate of the default domain set in `config`.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## ExchangeRate





**ExchangeRate Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**set**](./ExchangeRate#set) | [SetExchangeRateRequest](ExchangeRate#setexchangeraterequest) | [ExchangeRateInfo](ExchangeRate#exchangerateinfo) |
| [**reset**](./ExchangeRate#reset) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](ExchangeRate#exchangerateinfo) |
| [**enable**](./ExchangeRate#enable) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](ExchangeRate#exchangerateinfo) |
| [**disable**](./ExchangeRate#disable) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](ExchangeRate#exchangerateinfo) |
| [**get**](./ExchangeRate#get) | [ExchangeRateRequest](ExchangeRate#exchangeraterequest) | [ExchangeRateInfo](ExchangeRate#exchangerateinfo) |
| [**list**](./ExchangeRate#list) | [ExchangeRateQuery](ExchangeRate#exchangeratequery) | [ExchangeRatesInfo](ExchangeRate#exchangeratesinfo) |



    
<br>

### set

Overrides a value of a specific ExchangeRate. This method is used to change the ExchangeRate in a specific domain. You can set the `currency` and `rate` of the resource.



> **POST** /cost-analysis/v1/exchange-rate/set
>





 {{< tabs " set " >}}

 {{< tab "Request Example" >}}



[SetExchangeRateRequest](./ExchangeRate#setexchangeraterequest)

* **currency** (string)   `Required` 


* **rate** (float)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRateInfo](#EXCHANGERATEINFO)
* **currency** (string)   `Required` 

* **rate** (float)   `Required` 

* **state** (State)   `Required` 

* **is_default** (bool)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300.0,
   "state": "ENABLED",
   "is_default": true
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### reset

Resets a value of a specific ExchangeRate and changes the ExchangeRate to the ExchangeRate of the `default` domain.



> **POST** /cost-analysis/v1/exchange-rate/reset
>





 {{< tabs " reset " >}}

 {{< tab "Request Example" >}}



[ExchangeRateRequest](./ExchangeRate#exchangeraterequest)

* **currency** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "currency": "KRW"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRateInfo](#EXCHANGERATEINFO)
* **currency** (string)   `Required` 

* **rate** (float)   `Required` 

* **state** (State)   `Required` 

* **is_default** (bool)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300.0,
   "state": "ENABLED",
   "is_default": true
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable





> **POST** /cost-analysis/v1/exchange-rate/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[ExchangeRateRequest](./ExchangeRate#exchangeraterequest)

* **currency** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "currency": "KRW"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRateInfo](#EXCHANGERATEINFO)
* **currency** (string)   `Required` 

* **rate** (float)   `Required` 

* **state** (State)   `Required` 

* **is_default** (bool)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300.0,
   "state": "ENABLED",
   "is_default": true
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /cost-analysis/v1/exchange-rate/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[ExchangeRateRequest](./ExchangeRate#exchangeraterequest)

* **currency** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "currency": "KRW"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRateInfo](#EXCHANGERATEINFO)
* **currency** (string)   `Required` 

* **rate** (float)   `Required` 

* **state** (State)   `Required` 

* **is_default** (bool)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300.0,
   "state": "ENABLED",
   "is_default": true
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Gets a specific ExchangeRate. Prints detailed information about the ExchangeRate, including  `currency` and `rate`.



> **POST** /cost-analysis/v1/exchange-rate/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[ExchangeRateRequest](./ExchangeRate#exchangeraterequest)

* **currency** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "currency": "KRW"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRateInfo](#EXCHANGERATEINFO)
* **currency** (string)   `Required` 

* **rate** (float)   `Required` 

* **state** (State)   `Required` 

* **is_default** (bool)   `Required` 

* **domain_id** (string)   `Required` 



{{< highlight json >}}
{
   "currency": "KRW",
   "rate": 1300.0,
   "state": "ENABLED",
   "is_default": true
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all ExchangeRates. You can use a query to get a filtered list of ExchangeRates.



> **POST** /cost-analysis/v1/exchange-rate/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ExchangeRateQuery](./ExchangeRate#exchangeratequery)

* **domain_id** (string)   `Required` 





{{< highlight json >}}
{

}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ExchangeRatesInfo](#EXCHANGERATESINFO)
* **results** (ExchangeRateInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### ExchangeRateInfo
* **currency** (string)   `Required` 

    
* **rate** (float)   `Required` 

    
* **state** (State)   `Required` 

    
* **is_default** (bool)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ExchangeRateQuery
* **domain_id** (string)   `Required` 

    <br>

### ExchangeRateRequest
* **currency** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### ExchangeRatesInfo
* **results** (ExchangeRateInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### SetExchangeRateRequest
* **currency** (string)   `Required` 

    
* **rate** (float)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>
