---
title: "Organization"
linkTitle: "Organization"
weight: 3
bookFlatSection: true
---
# [Organization](#Organization)



>  **Package : spaceone.api.mzc_service_api.v1**

<br>
<br>

## Organization





**Organization Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Organization#create) | [OrganizationCreateRequest](Organization#organizationcreaterequest) | [OrganizationInfo](Organization#organizationinfo) |
| [**update**](./Organization#update) | [OrganizationUpdateRequest](Organization#organizationupdaterequest) | [OrganizationInfo](Organization#organizationinfo) |
| [**enable**](./Organization#enable) | [OrganizationRequest](Organization#organizationrequest) | [OrganizationInfo](Organization#organizationinfo) |
| [**disable**](./Organization#disable) | [OrganizationRequest](Organization#organizationrequest) | [OrganizationInfo](Organization#organizationinfo) |
| [**delete**](./Organization#delete) | [OrganizationRequest](Organization#organizationrequest) | [Empty](Organization#empty) |
| [**get**](./Organization#get) | [OrganizationRequest](Organization#organizationrequest) | [OrganizationInfo](Organization#organizationinfo) |
| [**list**](./Organization#list) | [OrganizationSearchQuery](Organization#organizationsearchquery) | [OrganizationsInfo](Organization#organizationsinfo) |
| [**stat**](./Organization#stat) | [OrganizationStatQuery](Organization#organizationstatquery) | [Struct](Organization#struct) |



    
<br>

### create





> **POST** /mzc-service-api/v1/organization/create
>






    
<br>

### update





> **POST** /mzc-service-api/v1/organization/update
>






    
<br>

### enable





> **POST** /mzc-service-api/v1/organization/enable
>






    
<br>

### disable





> **POST** /mzc-service-api/v1/organization/disable
>






    
<br>

### delete





> **POST** /mzc-service-api/v1/organization/delete
>






    
<br>

### get





> **POST** /mzc-service-api/v1/organization/get
>






    
<br>

### list





> **POST** /mzc-service-api/v1/organization/list
>






    
<br>

### stat





> **POST** /mzc-service-api/v1/organization/stat
>






    


<br>
<br>

## Message



### OrganizationCreateRequest
* **name** (string)   `Required` 

    
* **description** (string)  

    
* **industry** (string)  

    
* **registration_number** (string)  

    
* **country** (string)  

    
* **address** (string)  

    
* **contact_person** (string)  

    
* **contact_email** (string)  

    
* **contact_phone** (string)  

    
* **tags** (Struct)  

    <br>

### OrganizationInfo
* **org_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (OrganizationState)   `Required` 

    
* **description** (string)   `Required` 

    
* **industry** (string)   `Required` 

    
* **registration_number** (string)   `Required` 

    
* **country** (string)   `Required` 

    
* **address** (string)   `Required` 

    
* **contact_person** (string)   `Required` 

    
* **contact_email** (string)   `Required` 

    
* **contact_phone** (string)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### OrganizationRequest
* **org_id** (string)   `Required` 

    <br>

### OrganizationSearchQuery
* **query** (Query)  

    
* **org_id** (string)  

    
* **name** (string)  

    
* **state** (OrganizationState)  

    <br>

### OrganizationStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### OrganizationUpdateRequest
* **org_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)  

    
* **industry** (string)  

    
* **registration_number** (string)  

    
* **country** (string)  

    
* **address** (string)  

    
* **contact_person** (string)  

    
* **contact_email** (string)  

    
* **contact_phone** (string)  

    
* **tags** (Struct)  

    <br>

### OrganizationsInfo
* **results** (OrganizationInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>
