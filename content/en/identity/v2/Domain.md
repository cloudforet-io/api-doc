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
| [**get_meta_data**](./Domain#get_meta_data) | [GetDomainMetadataRequest](Domain#getdomainmetadatarequest) | [DomainMetadataInfo](Domain#domainmetadatainfo) |
| [**get_public_key**](./Domain#get_public_key) | [AuthenticationRequest](Domain#authenticationrequest) | [AuthenticationResponse](Domain#authenticationresponse) |
| [**list**](./Domain#list) | [DomainSearchQuery](Domain#domainsearchquery) | [DomainsInfo](Domain#domainsinfo) |
| [**stat**](./Domain#stat) | [DomainStatQuery](Domain#domainstatquery) | [Struct](Domain#struct) |



    
<br>

### create










    
<br>

### update










    
<br>

### delete










    
<br>

### enable










    
<br>

### disable










    
<br>

### get










    
<br>

### get_meta_data










    
<br>

### get_public_key










    
<br>

### list










    
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

    <br>

### CreateDomainRequest
* **name** (string)   `Required` 

    
* **admin** (Admin)   `Required` 

    
* **tags** (Struct)  

    <br>

### DomainInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **deleted_at** (string)   `Required` 

    <br>

### DomainMetadataInfo
* **domain_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **metadata** (Struct)   `Required` 

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

### GetDomainMetadataRequest
* **name** (string)   `Required` 

    <br>

### UpdateDomainRequest
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>
