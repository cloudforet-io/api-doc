---
title: "Domain"
linkTitle: "Domain"
weight: 3
bookFlatSection: true
---
# [Domain](#Domain)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Domain





**Domain Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Domain#create) | [CreateDomainRequest](Domain#createdomainrequest) | [DomainInfo](Domain#domaininfo) |
| [**update**](./Domain#update) | [UpdateDomainRequest](Domain#updatedomainrequest) | [DomainInfo](Domain#domaininfo) |
| [**delete**](./Domain#delete) | [DomainRequest](Domain#domainrequest) | [Empty](Domain#empty) |
| [**enable**](./Domain#enable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**disable**](./Domain#disable) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**get**](./Domain#get) | [DomainRequest](Domain#domainrequest) | [DomainInfo](Domain#domaininfo) |
| [**get_auth_info**](./Domain#get_auth_info) | [GetDomainAuthRequest](Domain#getdomainauthrequest) | [DomainAuthInfo](Domain#domainauthinfo) |
| [**get_public_key**](./Domain#get_public_key) | [AuthenticationRequest](Domain#authenticationrequest) | [AuthenticationResponse](Domain#authenticationresponse) |
| [**list**](./Domain#list) | [DomainSearchQuery](Domain#domainsearchquery) | [DomainsInfo](Domain#domainsinfo) |
| [**stat**](./Domain#stat) | [DomainStatQuery](Domain#domainstatquery) | [Struct](Domain#struct) |



    
<br>

### create





> **POST** /identity/v2/domain/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateDomainRequest](./Domain#createdomainrequest)

* **name** (string)   `Required` 


* **admin** (Admin)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{
 "name": "wonny-dev",
 "admin": {
   "user_id": "wonny@cloudforet.io",
   "name": "Wonny",
   "password": "Password1234!",
   "email": "wonny@cloudforet.io",
   "language": "en",
   "timezone": "UTC"
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainInfo](#DOMAININFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "state": "ENABLED",
 "created_at": "2024-11-12T02:24:01.233Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update





> **POST** /identity/v2/domain/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateDomainRequest](./Domain#updatedomainrequest)

* **domain_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainInfo](#DOMAININFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "state": "ENABLED",
 "created_at": "2024-11-12T02:24:01.233Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete





> **POST** /identity/v2/domain/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[DomainRequest](./Domain#domainrequest)

* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### enable





> **POST** /identity/v2/domain/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[DomainRequest](./Domain#domainrequest)

* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainInfo](#DOMAININFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "state": "ENABLED",
 "created_at": "2024-11-12T02:24:01.233Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable





> **POST** /identity/v2/domain/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[DomainRequest](./Domain#domainrequest)

* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainInfo](#DOMAININFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "state": "ENABLED",
 "created_at": "2024-11-12T02:24:01.233Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get





> **POST** /identity/v2/domain/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[DomainRequest](./Domain#domainrequest)

* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainInfo](#DOMAININFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **tags** (Struct)   `Required` 

* **created_at** (string)   `Required` 

* **deleted_at** (string)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "state": "ENABLED",
 "created_at": "2024-11-12T02:24:01.233Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_auth_info

+noauth



> **POST** /identity/v2/domain/get-auth-info
>





 {{< tabs " get_auth_info " >}}

 {{< tab "Request Example" >}}



[GetDomainAuthRequest](./Domain#getdomainauthrequest)

* **name** (string)   `Required` 





{{< highlight json >}}
{
 "name": "wonny-dev"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainAuthInfo](#DOMAINAUTHINFO)
* **domain_id** (string)   `Required` 

* **name** (string)   `Required` 

* **external_auth_state** (ExternalAuthState)   `Required` 

* **metadata** (Struct)   `Required` 

* **config** (Struct)   `Required` 



{{< highlight json >}}
{
 "domain_id": "domain-a1b2c3d4e5f6",
 "name": "wonny-dev",
 "external_auth_state": "DISABLED",
 "metadata": {},
 "config": {
     "settings": {
       "unified_cost_config": {
         "aggregation_day": 15.0,
         "currency": "KRW",
         "custom_exchange_rate": {},
         "exchange_date": 15.0,
         "exchange_rate_mode": "AUTO",
         "exchange_source": "Yahoo! Finance",
         "is_exchange_last_day": false,
         "is_last_day": false,
         "run_hour": 0.0
       }
     }
 }
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_public_key










    
<br>

### list





> **POST** /identity/v2/domain/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[DomainSearchQuery](./Domain#domainsearchquery)

* **query** (Query)  


* **domain_id** (string)  


* **name** (string)  


* **state** (State)  





{{< highlight json >}}
{
 "query": {
   "filter": [{
     "k": "tag.env",
     "v": "dev",
     "o": "eq"
   }],
   "sort": [{
     "key": "created_at",
     "desc": true
   }]
 }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DomainsInfo](#DOMAINSINFO)
* **results** (DomainInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
 "results": [
 {
   "domain_id": "domain-a1b2c3d4e5f6",
   "name": "wonny-dev1",
   "state": "ENABLED",
   "created_at": "2024-11-12T02:24:01.233Z"
 },
 {
   "domain_id": "domain-g7h8i9j1k2l3",
   "name": "wonny-dev2",
   "state": "ENABLED",
   "created_at": "2024-11-01T03:34:01.233Z"
 }
 ],
 "total_count": 2
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat










    


<br>
<br>

## Message



### Admin
* **user_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **password** (string)   `Required` 

    
* **email** (string)  

    
* **language** (string)  

    
* **timezone** (string)  

    
* **tags** (Struct)  

    
* **reset_password** (bool)  

    <br>

### CreateDomainRequest
* **name** (string)   `Required` 

    
* **admin** (Admin)   `Required` 

    
* **tags** (Struct)  

    <br>

### DomainAuthInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **external_auth_state** (ExternalAuthState)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **config** (Struct)   `Required` 

    <br>

### DomainInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### DomainRequest
* **domain_id** (string)   `Required` 

    <br>

### DomainSearchQuery
* **query** (Query)  

    
* **domain_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    <br>

### DomainStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### DomainsInfo
* **results** (DomainInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetDomainAuthRequest
* **name** (string)   `Required` 

    <br>

### UpdateDomainRequest
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
