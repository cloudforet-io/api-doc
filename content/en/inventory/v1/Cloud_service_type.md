---
title: "Cloud_service_type"
linkTitle: "Cloud_service_type"
weight: 3
bookFlatSection: true
---
# [Cloud_service_type](#Cloud_service_type)
desc: A CloudServiceType is a classification with hierarchical information of `CloudService`. A CloudServiceType provides information about which `group` a specific `Resource` belongs to and which `Services` are in it.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Cloud_service_type


**CloudServiceType Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudServiceType#create) | [CreateCloudServiceTypeRequest](CloudServiceType#createcloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**update**](./CloudServiceType#update) | [UpdateCloudServiceTypeRequest](CloudServiceType#updatecloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**delete**](./CloudServiceType#delete) | [CloudServiceTypeRequest](CloudServiceType#cloudservicetyperequest) | [Empty](./CloudServiceType#empty) |
| [**get**](./CloudServiceType#get) | [GetCloudServiceTypeRequest](CloudServiceType#getcloudservicetyperequest) | [CloudServiceTypeInfo](./CloudServiceType#cloudservicetypeinfo) |
| [**list**](./CloudServiceType#list) | [CloudServiceTypeQuery](CloudServiceType#cloudservicetypequery) | [CloudServiceTypesInfo](./CloudServiceType#cloudservicetypesinfo) |
| [**stat**](./CloudServiceType#stat) | [CloudServiceTypeStatQuery](CloudServiceType#cloudservicetypestatquery) | [Struct](./CloudServiceType#struct) |



    
<br>

### create

> **POST** /inventory/v1/cloud-service-type/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/cloud-service-type/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/cloud-service-type/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/cloud-service-type/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/cloud-service-type/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/cloud-service-type/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CloudServiceTypeInfo
* **cloud_service_type_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **group** (string)  `Required` 

    
* **cloud_service_type_key** (string)  `Required` 

    
* **service_code** (string)  `Required` 

    
* **is_primary** (bool)  `Required` 

    
* **is_major** (bool)  `Required` 

    
* **resource_type** (string)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### CloudServiceTypeQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **cloud_service_type_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **group** (string)  `Required` 

  *is_required: false*

    
* **cloud_service_type_key** (string)  `Required` 

  *is_required: false*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypeStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CloudServiceTypesInfo
* **results** (CloudServiceTypeInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCloudServiceTypeRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: true*

    
* **group** (string)  `Required` 

  *is_required: true*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetCloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateCloudServiceTypeRequest
* **cloud_service_type_id** (string)  `Required` 

  *is_required: true*

    
* **service_code** (string)  `Required` 

  *is_required: false*

    
* **is_primary** (bool)  `Required` 

  *is_required: false*

    
* **is_major** (bool)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **metadata** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
