---
title: "Package"
linkTitle: "Package"
weight: 3
bookFlatSection: true
---
# [Package](#Package)



>  **Package : spaceone.api.identity.v2**

<br>
<br>

## Package





**Package Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Package#create) | [CreatePackageRequest](Package#createpackagerequest) | [PackageInfo](Package#packageinfo) |
| [**update**](./Package#update) | [UpdatePackageRequest](Package#updatepackagerequest) | [PackageInfo](Package#packageinfo) |
| [**delete**](./Package#delete) | [PackageRequest](Package#packagerequest) | [Empty](Package#empty) |
| [**set_default**](./Package#set_default) | [PackageRequest](Package#packagerequest) | [PackageInfo](Package#packageinfo) |
| [**change_order**](./Package#change_order) | [ChangePackageOrderRequest](Package#changepackageorderrequest) | [PackageInfo](Package#packageinfo) |
| [**get**](./Package#get) | [PackageRequest](Package#packagerequest) | [PackageInfo](Package#packageinfo) |
| [**list**](./Package#list) | [PackageSearchQuery](Package#packagesearchquery) | [PackagesInfo](Package#packagesinfo) |
| [**stat**](./Package#stat) | [PackageStatQuery](Package#packagestatquery) | [Struct](Package#struct) |



    
<br>

### create





> **POST** /identity/v2/package/create
>






    
<br>

### update





> **POST** /identity/v2/package/update
>






    
<br>

### delete





> **POST** /identity/v2/package/delete
>






    
<br>

### set_default





> **POST** /identity/v2/package/set-default
>






    
<br>

### change_order





> **POST** /identity/v2/package/change-order
>






    
<br>

### get





> **POST** /identity/v2/package/get
>






    
<br>

### list





> **POST** /identity/v2/package/list
>






    
<br>

### stat





> **POST** /identity/v1/package/stat
>






    


<br>
<br>

## Message



### ChangePackageOrderRequest
* **package_id** (string)   `Required` 

    
* **order** (int32)   `Required` 

    <br>

### CreatePackageRequest
* **name** (string)   `Required` 

    
* **description** (string)  

    
* **tags** (Struct)  

    <br>

### PackageInfo
* **package_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **order** (int32)   `Required` 

    
* **is_default** (bool)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PackageRequest
* **package_id** (string)   `Required` 

    <br>

### PackageSearchQuery
* **query** (Query)  

    
* **package_id** (string)  

    
* **name** (string)  

    <br>

### PackageStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### PackagesInfo
* **results** (PackageInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePackageRequest
* **package_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **tags** (Struct)  

    <br>
