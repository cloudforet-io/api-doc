---
title: "Offering"
linkTitle: "Offering"
weight: 3
bookFlatSection: true
---
# [Offering](#Offering)



>  **Package : spaceone.api.mzc_service_api.v1**

<br>
<br>

## Offering





**Offering Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Offering#create) | [OfferingCreateRequest](Offering#offeringcreaterequest) | [OfferingInfo](Offering#offeringinfo) |
| [**update**](./Offering#update) | [OfferingUpdateRequest](Offering#offeringupdaterequest) | [OfferingInfo](Offering#offeringinfo) |
| [**delete**](./Offering#delete) | [OfferingRequest](Offering#offeringrequest) | [Empty](Offering#empty) |
| [**get**](./Offering#get) | [OfferingRequest](Offering#offeringrequest) | [OfferingInfo](Offering#offeringinfo) |
| [**list**](./Offering#list) | [OfferingSearchQuery](Offering#offeringsearchquery) | [OfferingsInfo](Offering#offeringsinfo) |
| [**stat**](./Offering#stat) | [OfferingStatQuery](Offering#offeringstatquery) | [Struct](Offering#struct) |



    
<br>

### create





> **POST** /mzc-service-api/v1/offering/create
>






    
<br>

### update





> **POST** /mzc-service-api/v1/offering/update
>






    
<br>

### delete





> **POST** /mzc-service-api/v1/offering/delete
>






    
<br>

### get





> **POST** /mzc-service-api/v1/offering/get
>






    
<br>

### list





> **POST** /mzc-service-api/v1/offering/list
>






    
<br>

### stat





> **POST** /mzc-service-api/v1/offering/stat
>






    


<br>
<br>

## Message



### OfferingCreateRequest
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **price** (float)  

    
* **currency** (string)  

    
* **description** (string)  

    
* **terms** (string)  

    
* **website_url** (string)  

    
* **tags** (Struct)  

    <br>

### OfferingInfo
* **offering_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **category** (string)   `Required` 

    
* **status** (OfferingStatus)   `Required` 

    
* **price** (float)   `Required` 

    
* **currency** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **terms** (string)   `Required` 

    
* **website_url** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### OfferingRequest
* **offering_id** (string)   `Required` 

    <br>

### OfferingSearchQuery
* **query** (Query)  

    
* **offering_id** (string)  

    
* **name** (string)  

    
* **status** (OfferingStatus)  

    <br>

### OfferingStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### OfferingUpdateRequest
* **offering_id** (string)   `Required` 

    
* **name** (string)  

    
* **status** (OfferingStatus)  

    
* **price** (float)  

    
* **currency** (string)  

    
* **description** (string)  

    
* **terms** (string)  

    
* **website_url** (string)  

    
* **tags** (Struct)  

    <br>

### OfferingsInfo
* **results** (OfferingInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
