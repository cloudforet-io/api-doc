---
title: "Contract"
linkTitle: "Contract"
weight: 3
bookFlatSection: true
---
# [Contract](#Contract)



>  **Package : spaceone.api.mzc_service_api.v1**

<br>
<br>

## Contract





**Contract Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Contract#create) | [ContractCreateRequest](Contract#contractcreaterequest) | [ContractInfo](Contract#contractinfo) |
| [**update**](./Contract#update) | [ContractUpdateRequest](Contract#contractupdaterequest) | [ContractInfo](Contract#contractinfo) |
| [**terminate**](./Contract#terminate) | [ContractRequest](Contract#contractrequest) | [Empty](Contract#empty) |
| [**get**](./Contract#get) | [ContractRequest](Contract#contractrequest) | [ContractInfo](Contract#contractinfo) |
| [**list**](./Contract#list) | [ContractSearchQuery](Contract#contractsearchquery) | [ContractsInfo](Contract#contractsinfo) |
| [**stat**](./Contract#stat) | [ContractStatQuery](Contract#contractstatquery) | [Struct](Contract#struct) |



    
<br>

### create





> **POST** /mzc-service-api/v1/contract/create
>






    
<br>

### update





> **POST** /mzc-service-api/v1/contract/update
>






    
<br>

### terminate





> **POST** /mzc-service-api/v1/contract/terminate
>






    
<br>

### get





> **POST** /mzc-service-api/v1/contract/get
>






    
<br>

### list





> **POST** /mzc-service-api/v1/contract/list
>






    
<br>

### stat





> **POST** /mzc-service-api/v1/contract/stat
>






    


<br>
<br>

## Message



### ContractCreateRequest
* **org_id** (string)   `Required` 

    
* **offering_id** (string)   `Required` 

    
* **start_date** (string)   `Required` 

    
* **end_date** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **signed_date** (string)  

    
* **renewal_type** (ContractRenewalType)  

    
* **tags** (Struct)  

    <br>

### ContractInfo
* **contract_id** (string)   `Required` 

    
* **org_id** (string)   `Required` 

    
* **offering_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **status** (ContractStatus)   `Required` 

    
* **description** (string)   `Required` 

    
* **start_date** (string)   `Required` 

    
* **end_date** (string)   `Required` 

    
* **signed_date** (string)   `Required` 

    
* **renewal_type** (ContractRenewalType)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### ContractRequest
* **contract_id** (string)   `Required` 

    <br>

### ContractSearchQuery
* **query** (Query)  

    
* **contract_id** (string)  

    
* **org_id** (string)  

    
* **offering_id** (string)  

    
* **status** (ContractStatus)  

    
* **renewal_type** (ContractRenewalType)  

    <br>

### ContractStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### ContractUpdateRequest
* **contract_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **start_date** (string)  

    
* **end_date** (string)  

    
* **signed_date** (string)  

    
* **renewal_type** (ContractRenewalType)  

    
* **tags** (Struct)  

    <br>

### ContractsInfo
* **results** (ContractInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
